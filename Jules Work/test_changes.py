"""
Tests for Gap 3 Field-Change Tracking in state.py
"""
import pytest
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from schema import Event
from state import track_field_changes

NY_TZ = ZoneInfo("America/New_York")


def test_field_change_tracking(tmp_path: Path):
    db_file = tmp_path / "test_changes.db"
    now = datetime.now(NY_TZ)

    e1 = Event(
        title="Jazz Night at Smalls",
        start_datetime=now,
        venue="Smalls Jazz Club",
        price_tier="$",
    )

    # Initial run records event into history
    events_r1 = track_field_changes([e1], db_path=db_file)
    assert events_r1[0].previous_venue is None
    assert events_r1[0].changed_at is None

    # Venue updated on second run for same dedup key
    e1_updated = Event(
        title="Jazz Night at Smalls",
        start_datetime=now,
        venue="Mezzrow",
        price_tier="$",
    )
    # Ensure dedup key matches e1 by adjusting dedup_key matching or passing same initial dedup input
    # In e1 dedup_key, title + date + venue are normalized.
    # To test venue update tracking on an event with matching title+date, let's mock dedup_key or inspect track_field_changes

    # Run track_field_changes with modified venue using same dedup key hash
    e1_updated.dedup_key = lambda: e1.dedup_key()

    events_r2 = track_field_changes([e1_updated], db_path=db_file)
    assert events_r2[0].previous_venue == "Smalls Jazz Club"
    assert events_r2[0].changed_at is not None
