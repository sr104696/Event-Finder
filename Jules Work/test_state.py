"""
Tests for state ledger content hashing and SQLite state persistence.
"""
import pytest
from pathlib import Path
from state import get_connection, get_content_hash, is_article_unchanged, record_article


def test_content_hash_ledger(tmp_path: Path):
    db_file = tmp_path / "test_state.db"
    url = "https://theskint.com/weekend-events-post"
    body_v1 = "Join us this Friday for a free party in Bushwick!"
    body_v2 = "UPDATED: Join us this Friday for a free party in Williamsburg!"

    # Initially article is not unchanged
    assert not is_article_unchanged(url, body_v1, db_path=db_file)

    # Record v1
    record_article(url, body_v1, db_path=db_file)
    assert is_article_unchanged(url, body_v1, db_path=db_file)

    # Body changed -> returns False so re-extraction occurs
    assert not is_article_unchanged(url, body_v2, db_path=db_file)

    # Record v2 -> updated, now v2 is unchanged
    record_article(url, body_v2, db_path=db_file)
    assert is_article_unchanged(url, body_v2, db_path=db_file)
    assert not is_article_unchanged(url, body_v1, db_path=db_file)
