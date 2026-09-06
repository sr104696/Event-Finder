"""
Meetup adapter: pulls .ics calendar exports from a curated list of groups
you maintain yourself (meetup_groups.yaml), and expands recurring events
(RRULE) into individual instances within the lookahead window.

Why curated + ICS instead of the Meetup API: as of the Feb 2025 platform
change, Meetup's API requires an active Pro subscription plus OAuth app
approval that isn't guaranteed even with Pro. Each group's public ICS
export (https://www.meetup.com/<group-slug>/events/ical/) needs no auth
at all and is the highest-quality structured source in this pipeline --
but it will silently drop or misdate recurring events ("every Tuesday run
club") if you don't expand RRULEs, which is the landmine this adapter
exists to defuse.
"""
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import requests
from icalendar import Calendar
import recurring_ical_events

from schema import Event
from neighborhoods import normalize_neighborhood

NY_TZ = ZoneInfo("America/New_York")
SOURCE_QUALITY = 5  # structured, first-party, no LLM guessing involved


def fetch_group_events(ics_url: str, lookahead_days: int = 14) -> list[Event]:
    """Fetch one group's ICS feed and return normalized, recurrence-expanded
    Events within [now, now + lookahead_days]."""
    resp = requests.get(ics_url, timeout=20)
    resp.raise_for_status()

    cal = Calendar.from_ical(resp.text)

    start = datetime.now(NY_TZ)
    end = start + timedelta(days=lookahead_days)

    # recurring_ical_events expands RRULE/RDATE/EXDATE into concrete
    # instances for us -- this is the step a naive icalendar-only parser
    # skips, which is exactly how "every Tuesday" events go missing.
    instances = recurring_ical_events.of(cal).between(start, end)

    events = []
    for component in instances:
        title = str(component.get("summary", "")).strip()
        if not title:
            continue

        dtstart = component.get("dtstart").dt
        dtend_field = component.get("dtend")
        dtend = dtend_field.dt if dtend_field else None

        if not isinstance(dtstart, datetime):
            # all-day event with no time component -- skip, too ambiguous
            continue
        if dtstart.tzinfo is None:
            dtstart = dtstart.replace(tzinfo=NY_TZ)
        else:
            dtstart = dtstart.astimezone(NY_TZ)
        if isinstance(dtend, datetime):
            dtend = dtend.astimezone(NY_TZ) if dtend.tzinfo else dtend.replace(tzinfo=NY_TZ)
        else:
            dtend = None

        location = str(component.get("location", "")).strip() or None
        description = str(component.get("description", "")).strip()
        url = str(component.get("url", "")).strip() or ics_url

        events.append(Event(
            title=title,
            start_datetime=dtstart,
            end_datetime=dtend,
            venue=location,
            neighborhood=normalize_neighborhood(location),
            price_tier=None,  # Meetup ICS doesn't carry price; leave for scoring to treat as unknown
            category_tags=[],
            editorial_blurb=description[:200] if description else None,
            source="meetup",
            source_url=url,
            source_quality=SOURCE_QUALITY,
            date_confidence=1.0,  # structured calendar data, not an LLM guess
            extraction_status="ok",
        ))

    return events


def fetch_all(group_ics_urls: list[str], lookahead_days: int = 14) -> list[Event]:
    """Fetch every curated group, skipping (and logging) any that fail
    rather than crashing the whole run over one dead link."""
    all_events: list[Event] = []
    for url in group_ics_urls:
        try:
            all_events.extend(fetch_group_events(url, lookahead_days))
        except Exception as e:  # noqa: BLE001 -- intentionally broad, see module docstring
            print(f"[meetup_ics] skipping {url}: {e}")
    return all_events
