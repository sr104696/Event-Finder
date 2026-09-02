"""
Dedup, expiry, scoring, and state tracking with field-change detection.

Implements Gap #3: Lightweight field-change tracking - stores previous values
when venue/time/price changes, enabling "What Changed This Week" notifications.
"""
# Import state management for change tracking
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from schema import Event

sys.path.insert(0, str(Path(__file__).parent / "Kiro Work"))
try:
    from state import cleanup_old_data, track_event_changes
    STATE_TRACKING_AVAILABLE = True
except ImportError:
    STATE_TRACKING_AVAILABLE = False
    print("[pipeline] Warning: state.py not found, change tracking disabled")

NY_TZ = ZoneInfo("America/New_York")


def dedup(events: list[Event]) -> list[Event]:
    """Fuzzy dedup on normalized title+date+venue. First occurrence wins;
    since higher source_quality adapters should generally run first in
    main.py, this naturally prefers the more reliable source on a tie."""
    seen: dict[str, Event] = {}
    for event in events:
        key = event.dedup_key()
        if key not in seen:
            seen[key] = event
    return list(seen.values())


def expire(events: list[Event], lookahead_days: int = 14) -> list[Event]:
    """Drop anything already over, and anything absurdly far out (protects
    against a bad LLM date guess landing 6 months from now)."""
    now = datetime.now(NY_TZ)
    horizon = now + timedelta(days=lookahead_days)
    return [
        e for e in events
        if e.start_datetime and now <= e.start_datetime <= horizon
    ]


def validate(events: list[Event]) -> tuple[list[Event], list[Event]]:
    """Sanity-check each event before it's allowed further into the
    pipeline. Returns (valid, quarantined). Cheap, deterministic checks --
    catches malformed adapter output before it reaches scoring/output,
    which is a lot easier to debug than a bad calendar entry three stages
    downstream."""
    valid, quarantined = [], []
    for e in events:
        reasons = []
        if not e.title or not e.title.strip():
            reasons.append("missing title")
        if not e.start_datetime:
            reasons.append("missing start_datetime")
        elif e.start_datetime.tzinfo is None:
            reasons.append("naive (non-timezone-aware) start_datetime")
        if e.end_datetime and e.start_datetime and e.end_datetime < e.start_datetime:
            reasons.append("end before start")
        if e.end_datetime and e.start_datetime:
            duration_hours = (e.end_datetime - e.start_datetime).total_seconds() / 3600
            if duration_hours > 18:
                reasons.append(f"implausible duration ({duration_hours:.0f}h) -- likely a parsing error")

        if reasons:
            e.extraction_status = "rejected"
            print(f"[validate] quarantined {e.title!r}: {', '.join(reasons)}")
            quarantined.append(e)
        else:
            valid.append(e)
    return valid, quarantined


def filter_low_confidence(events: list[Event], min_confidence: float = 0.6) -> tuple[list[Event], list[Event]]:
    """Split into (publishable, needs_review). Low-confidence dates should
    never silently enter the calendar -- they get held out for a human
    glance instead."""
    good, review = [], []
    for e in events:
        if e.date_confidence >= min_confidence and e.extraction_status != "rejected":
            good.append(e)
        else:
            review.append(e)
    return good, review


def score(events: list[Event], cold_start: bool = False) -> list[Event]:
    """
    Deterministic vibe_score, 0-10. LLM-extracted sources already carry
    a vibe_match (0-100) from the extraction prompt where available; this
    blends that with source_quality and price so ranking isn't purely
    vibes from a single LLM call.
    
    Implements Gap #2 (cold-start ranking): if cold_start=True, weights
    explicit filters (neighborhood, category, price) higher than vibe_match
    since there's no feedback data yet to trust the LLM scoring.
    """
    for e in events:
        base = 5.0
        if e.price_tier == "free":
            base += 2.0
        elif e.price_tier == "$":
            base += 0.5

        base += (e.source_quality - 3) * 0.5  # source_quality 1-5 -> +/-1.0

        if e.llm_vibe_match is not None:
            if cold_start:
                # Cold start: weight vibe_match less, explicit filters more
                base += (e.llm_vibe_match / 100) * 1.5 - 0.75  # reduced from 3.0
            else:
                # Normal: trust vibe_match
                base += (e.llm_vibe_match / 100) * 3.0 - 1.5

        e.vibe_score = round(max(0.0, min(10.0, base)), 2)
    return events


def track_changes(events: list[Event]) -> None:
    """
    Track field changes for all events (Gap #3).
    Stores previous values when venue/time/price changes.
    """
    if not STATE_TRACKING_AVAILABLE:
        return
    
    for event in events:
        try:
            track_event_changes(event)
        except Exception as e:  # noqa: BLE001 - defensive, state tracking shouldn't break pipeline
            print(f"[pipeline] Failed to track changes for {event.title!r}: {e}")


def cleanup_state(days: int = 90) -> None:
    """
    Run garbage collection on state database.
    Remove events not seen in N days to prevent unbounded growth.
    """
    if not STATE_TRACKING_AVAILABLE:
        return
    
    try:
        cleanup_old_data(days)
        print(f"[pipeline] Cleaned up events older than {days} days from state.db")
    except Exception as e:  # noqa: BLE001 - defensive, cleanup shouldn't break pipeline
        print(f"[pipeline] Failed to cleanup old data: {e}")
