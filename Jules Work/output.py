"""
Writes the two v1 outputs: events.json (for inspection / a future UI) and
curated.ics (a subscribable calendar feed -- no OAuth, no Calendar API
quota, works in Google Calendar, Apple Calendar, or anything else that
eats an .ics URL. Upgrade to a Google Calendar API push later only if the
subscription-refresh lag actually bothers you in practice).
"""
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from icalendar import Calendar, Event as ICSEvent

from schema import Event

NY_TZ = ZoneInfo("America/New_York")


def write_json(events: list[Event], needs_review: list[Event], path: str = "events.json") -> None:
    payload = {
        "generated_at": datetime.now(NY_TZ).isoformat(),
        "events": [e.to_dict() for e in sorted(events, key=lambda e: (-e.vibe_score if e.vibe_score else 0, e.start_datetime))],
        "needs_review": [e.to_dict() for e in needs_review],
    }
    Path(path).write_text(json.dumps(payload, indent=2, default=str))


def write_ics(events: list[Event], path: str = "curated.ics", top_n_per_day: int = 5) -> None:
    """Caps output at top_n_per_day by vibe_score so a subscribed calendar
    doesn't turn into 100+ entries a week -- that's how a curation feed
    stops getting looked at."""
    by_day: dict[str, list[Event]] = {}
    for e in events:
        day = e.start_datetime.date().isoformat()
        by_day.setdefault(day, []).append(e)

    capped: list[Event] = []
    for day_events in by_day.values():
        day_events.sort(key=lambda e: -(e.vibe_score or 0))
        capped.extend(day_events[:top_n_per_day])

    cal = Calendar()
    cal.add("prodid", "-//NYC Curated Events//personal//")
    cal.add("version", "2.0")
    cal.add("x-wr-calname", "NYC Curated")

    for e in capped:
        ics_event = ICSEvent()
        ics_event.add("summary", e.title)
        ics_event.add("dtstart", e.start_datetime)
        ics_event.add("dtend", e.end_datetime or e.start_datetime)
        location_bits = [b for b in [e.venue, e.neighborhood] if b]
        if location_bits:
            ics_event.add("location", ", ".join(location_bits))
        description_bits = [b for b in [e.editorial_blurb, e.source_url] if b]
        if description_bits:
            ics_event.add("description", "\n".join(description_bits))
        ics_event.add("uid", e.dedup_key() + "@nyc-curator")
        cal.add_component(ics_event)

    Path(path).write_bytes(cal.to_ical())
