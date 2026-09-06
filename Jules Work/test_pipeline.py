"""
Tests for cold-start ranking in pipeline.py
"""
from datetime import datetime
from zoneinfo import ZoneInfo
from schema import Event
from pipeline import score

NY_TZ = ZoneInfo("America/New_York")


def test_cold_start_ranking():
    now = datetime.now(NY_TZ)
    e1 = Event(
        title="Bushwick Art Party",
        start_datetime=now,
        neighborhood="Bushwick",
        category_tags=["art", "nightlife"],
        price_tier="free",
        llm_vibe_match=60.0,
    )
    e2 = Event(
        title="Generic Midtown Networking",
        start_datetime=now,
        neighborhood="Midtown",
        category_tags=["tech"],
        price_tier="$$$",
        llm_vibe_match=90.0,
    )

    scored = score([e1, e2], preferred_neighborhoods=["Bushwick"], preferred_categories=["art"])
    art_party = next(e for e in scored if e.title == "Bushwick Art Party")
    networking = next(e for e in scored if e.title == "Generic Midtown Networking")

    # Bushwick Art Party should rank higher despite lower LLM vibe match due to explicit neighborhood/category matches
    assert art_party.vibe_score > networking.vibe_score
