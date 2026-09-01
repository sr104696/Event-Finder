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


def dedup(events: list[Event], fuzzy_threshold: int = 85) -> list[Event]:
    """Dedup on normalized title+date+venue with fuzzy string matching via thefuzz.
    First occurrence wins (preferring higher source_quality adapters that run first)."""
    try:
        from thefuzz import fuzz
        use_fuzz = True
    except ImportError:
        use_fuzz = False

    kept: list[Event] = []
    seen_keys: set[str] = set()

    for event in events:
        key = event.dedup_key()
        if key in seen_keys:
            continue

        duplicate_found = False
        if use_fuzz and event.start_datetime:
            event_date = event.start_datetime.date().isoformat()
            for existing in kept:
                if existing.start_datetime and existing.start_datetime.date().isoformat() == event_date:
                    title_sim = fuzz.ratio(event.title.lower(), existing.title.lower())
                    venue1 = (event.venue or "").lower()
                    venue2 = (existing.venue or "").lower()
                    venue_sim = fuzz.ratio(venue1, venue2) if (venue1 and venue2) else 100

                    if title_sim >= fuzzy_threshold and venue_sim >= 70:
                        duplicate_found = True
                        break

        if not duplicate_found:
            kept.append(event)
            seen_keys.add(key)

    return kept


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


def score(events: list[Event], preferred_neighborhoods: list[str] = None, preferred_categories: list[str] = None) -> list[Event]:
    """Deterministic vibe_score, 0-10.
    Cold-start aware: when feedback signal is not yet present, ranks primarily by explicit
    filters (neighborhood, category match, price tier, source quality) while using
    llm_vibe_match as a secondary tiebreaker.
    """
    pref_neighs = set(n.lower() for n in (preferred_neighborhoods or []))
    pref_cats = set(c.lower() for c in (preferred_categories or []))

    for e in events:
        base = 5.0
        # Price boost
        if e.price_tier == "free":
            base += 1.5
        elif e.price_tier == "$":
            base += 0.5

        # Explicit filter boosts for Cold-Start ranking
        if e.neighborhood and e.neighborhood.lower() in pref_neighs:
            base += 1.5
        if any(cat.lower() in pref_cats for cat in e.category_tags):
            base += 1.0

        # Source quality weight (+/-1.0)
        base += (e.source_quality - 3) * 0.5

        # Secondary vibe contribution when available
        if e.llm_vibe_match is not None:
            base += (e.llm_vibe_match / 100) * 1.5 - 0.75

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
