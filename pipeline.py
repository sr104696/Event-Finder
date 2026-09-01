"""
Dedup, expiry, scoring, and state tracking -- the unglamorous middle of the
pipeline that determines whether this is a usable feed or a noisy mess.
"""
import json
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from schema import Event

NY_TZ = ZoneInfo("America/New_York")
STATE_PATH = Path("state.json")


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


def score(events: list[Event]) -> list[Event]:
    """Deterministic vibe_score, 0-10. LLM-extracted sources already carry
    a vibe_match (0-100) from the extraction prompt where available; this
    blends that with source_quality and price so ranking isn't purely
    vibes from a single LLM call."""
    for e in events:
        base = 5.0
        if e.price_tier == "free":
            base += 2.0
        elif e.price_tier == "$":
            base += 0.5

        base += (e.source_quality - 3) * 0.5  # source_quality 1-5 -> +/-1.0

        if e.llm_vibe_match is not None:
            base += (e.llm_vibe_match / 100) * 3.0 - 1.5  # centers around 0 contribution at vibe_match=50

        e.vibe_score = round(max(0.0, min(10.0, base)), 2)
    return events


def load_seen_urls() -> set[str]:
    if STATE_PATH.exists():
        return set(json.loads(STATE_PATH.read_text()).get("seen_urls", []))
    return set()


def save_seen_urls(urls: set[str]) -> None:
    # keep the ledger from growing forever -- cap at last 2000 seen URLs
    trimmed = list(urls)[-2000:]
    STATE_PATH.write_text(json.dumps({"seen_urls": trimmed, "updated_at": datetime.now(NY_TZ).isoformat()}))
