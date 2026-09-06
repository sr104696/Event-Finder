"""
Tests for extruct JSON-LD extraction and fuzzy deduplication with thefuzz.
"""
from datetime import datetime
from zoneinfo import ZoneInfo
from schema import Event
from pipeline import dedup
from adapters.eventbrite_jsonld import _flatten_ld_blocks

NY_TZ = ZoneInfo("America/New_York")


def test_extruct_ld_blocks():
    html = """
    <html>
    <head>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Event",
      "name": "Extruct Test Party",
      "startDate": "2026-10-01T20:00:00Z",
      "location": {"@type": "Place", "name": "House of Yes"}
    }
    </script>
    </head>
    </html>
    """
    blocks = _flatten_ld_blocks(html)
    assert len(blocks) >= 1
    assert any(b.get("name") == "Extruct Test Party" for b in blocks)


def test_fuzzy_dedup():
    now = datetime.now(NY_TZ)
    e1 = Event(
        title="Live Indie Concert at Brooklyn Steel",
        start_datetime=now,
        venue="Brooklyn Steel",
        source_quality=5,
    )
    e2 = Event(
        title="Live Indie Concert @ Brooklyn Steel!",
        start_datetime=now,
        venue="Brooklyn Steel",
        source_quality=3,
    )

    deduped = dedup([e1, e2])
    assert len(deduped) == 1
    assert deduped[0].source_quality == 5
