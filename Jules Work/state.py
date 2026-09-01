"""
State ledger management using SQLite for content-hash tracking and URL deduplication.
Fulfills Gap 1 (idempotent re-processing keyed on content hash) and Gap 3 (field change tracking).
"""
import sqlite3
import hashlib
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from typing import Optional, Dict

NY_TZ = ZoneInfo("America/New_York")
DB_PATH = Path("state.db")


def get_connection(db_path: Path = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS seen_articles (
                url TEXT PRIMARY KEY,
                content_hash TEXT NOT NULL,
                last_seen TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS event_history (
                dedup_key TEXT PRIMARY KEY,
                title TEXT,
                start_datetime TEXT,
                venue TEXT,
                price_tier TEXT,
                updated_at TEXT
            )
        """)
    return conn


def get_content_hash(text: str) -> str:
    """Computes SHA-256 hash of article body content."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def is_article_unchanged(url: str, content: str, db_path: Path = DB_PATH) -> bool:
    """Returns True if the article URL has been seen before AND its content hash is identical."""
    chash = get_content_hash(content)
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT content_hash FROM seen_articles WHERE url = ?", (url,))
    row = cursor.fetchone()
    conn.close()
    if row and row["content_hash"] == chash:
        return True
    return False


def record_article(url: str, content: str, db_path: Path = DB_PATH) -> None:
    """Records or updates an article's URL, content hash, and timestamp in the SQLite ledger."""
    chash = get_content_hash(content)
    now_iso = datetime.now(NY_TZ).isoformat()
    conn = get_connection(db_path)
    with conn:
        conn.execute("""
            INSERT INTO seen_articles (url, content_hash, last_seen)
            VALUES (?, ?, ?)
            ON CONFLICT(url) DO UPDATE SET
                content_hash = excluded.content_hash,
                last_seen = excluded.last_seen
        """, (url, chash, now_iso))
    conn.close()


def load_seen_urls(db_path: Path = DB_PATH) -> set[str]:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM seen_articles")
    urls = {row["url"] for row in cursor.fetchall()}
    conn.close()
    return urls


def save_seen_urls(urls: set[str], db_path: Path = DB_PATH) -> None:
    now_iso = datetime.now(NY_TZ).isoformat()
    conn = get_connection(db_path)
    with conn:
        for url in urls:
            conn.execute("""
                INSERT INTO seen_articles (url, content_hash, last_seen)
                VALUES (?, '', ?)
                ON CONFLICT(url) DO UPDATE SET last_seen = excluded.last_seen
            """, (url, now_iso))
    conn.close()


def track_field_changes(events: list, db_path: Path = DB_PATH) -> list:
    """Tracks updates to venue or start_datetime across pipeline runs, populating
    previous_venue, previous_start_datetime, and changed_at when changes occur."""
    now_iso = datetime.now(NY_TZ).isoformat()
    conn = get_connection(db_path)
    with conn:
        for e in events:
            key = e.dedup_key()
            cursor = conn.cursor()
            cursor.execute("SELECT title, start_datetime, venue, price_tier FROM event_history WHERE dedup_key = ?", (key,))
            row = cursor.fetchone()

            current_start = e.start_datetime.isoformat() if e.start_datetime else ""
            current_venue = e.venue or ""

            if row:
                old_start = row["start_datetime"] or ""
                old_venue = row["venue"] or ""

                changed = False
                if old_venue and old_venue != current_venue:
                    e.previous_venue = old_venue
                    changed = True
                if old_start and old_start != current_start:
                    e.previous_start_datetime = old_start
                    changed = True

                if changed:
                    e.changed_at = now_iso

                conn.execute("""
                    UPDATE event_history
                    SET title = ?, start_datetime = ?, venue = ?, price_tier = ?, updated_at = ?
                    WHERE dedup_key = ?
                """, (e.title, current_start, current_venue, e.price_tier or "", now_iso, key))
            else:
                conn.execute("""
                    INSERT INTO event_history (dedup_key, title, start_datetime, venue, price_tier, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (key, e.title, current_start, current_venue, e.price_tier or "", now_iso))

    conn.close()
    return events
