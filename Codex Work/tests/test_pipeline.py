from datetime import datetime
from pathlib import Path

from nyc_curated.pipeline import (
    NY_TZ, apply_field_changes, article_is_unchanged, content_hash, load_state,
    record_article, save_state, score_cold_start,
)
from nyc_curated.schema import Event


def event(**changes):
    values = {"title": "Gallery opening", "start_datetime": datetime(2026, 9, 5, 19, tzinfo=NY_TZ), "venue": "A Space"}
    values.update(changes)
    return Event(**values)


def test_content_hash_ignores_line_endings_but_detects_edit(tmp_path: Path):
    state = load_state(tmp_path / "state.json")
    record_article(state, "https://example.test/post", "One\r\nTwo\n")
    assert article_is_unchanged(state, "https://example.test/post", "One\nTwo")
    assert not article_is_unchanged(state, "https://example.test/post", "One\nChanged")
    assert content_hash("One\nTwo") == content_hash("One\r\nTwo\n")
    save_state(state, tmp_path / "state.json")
    assert load_state(tmp_path / "state.json")["content_hashes"]


def test_field_changes_store_old_values_only():
    state = {"content_hashes": {}, "event_snapshots": {}}
    first = event()
    apply_field_changes([first], state, datetime(2026, 9, 1, tzinfo=NY_TZ))
    moved = event(venue="B Space", price_tier="$")
    apply_field_changes([moved], state, datetime(2026, 9, 2, tzinfo=NY_TZ))
    assert moved.previous_values == {"venue": "A Space", "price_tier": None}
    assert moved.changed_at == datetime(2026, 9, 2, tzinfo=NY_TZ)


def test_cold_start_prioritizes_explicit_filters():
    matched = event(neighborhood="Bushwick", category_tags=["music"], price_tier="free", llm_vibe_match=0)
    unmatched = event(title="Other", neighborhood="Chelsea", category_tags=["art"], llm_vibe_match=100)
    score_cold_start([matched, unmatched], preferred_neighborhoods={"Bushwick"}, preferred_categories={"music"})
    assert matched.vibe_score > unmatched.vibe_score
