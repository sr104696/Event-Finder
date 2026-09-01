"""
State management using SQLite for idempotent re-processing and field-change tracking.

Implements:
- Gap #1: Content-hash-based ledger to skip unchanged RSS articles
- Gap #3: Lightweight field-change tracking for venue/time/price changes

Why SQLite over JSON:
- Queryable: "show me events that changed this week" is a SELECT, not a full-file scan
- Atomic updates: no risk of corrupted state.json from partial writes
- Still just a file: state.db commits alongside events.json in GitHub Actions
- No server, no service, no operational complexity
"""
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Optional
from zoneinfo import ZoneInfo

from sqlite_utils import Database

from schema import Event

NY_TZ = ZoneInfo("America/New_York")
STATE_DB_PATH = Path("state.db")


def get_db() -> Database:
    """Get or create the state database with required tables."""
    db = Database(STATE_DB_PATH)
    
    # Article processing ledger (Gap #1)
    if "articles" not in db.table_names():
        db["articles"].create({
            "url": str,
            "content_hash": str,
            "last_processed": str,
            "source": str,
        }, pk="url", if_not_exists=True)
        db["articles"].create_index(["content_hash"], if_not_exists=True)
    
    # Event change tracking (Gap #3)
    if "event_changes" not in db.table_names():
        db["event_changes"].create({
            "event_id": str,          # Event.dedup_key()
            "field": str,             # "venue", "start_datetime", "price_tier", etc.
            "old_value": str,
            "new_value": str,
            "changed_at": str,
        }, if_not_exists=True)
        db["event_changes"].create_index(["event_id"], if_not_exists=True)
        db["event_changes"].create_index(["changed_at"], if_not_exists=True)
    
    # Event history (for detecting changes)
    if "events" not in db.table_names():
        db["events"].create({
            "event_id": str,
            "title": str,
            "start_datetime": str,
            "end_datetime": str,
            "venue": str,
            "price_tier": str,
            "source_url": str,
            "last_seen": str,
        }, pk="event_id", if_not_exists=True)
    
    return db


def article_hash(content: str) -> str:
    """Hash article content for change detection."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]


def should_process_article(url: str, content: str, source: str) -> bool:
    """
    Check if article needs processing based on content hash.
    Returns True if content changed or never seen before.
    """
    db = get_db()
    content_h = article_hash(content)
    
    existing = db["articles"].rows_where("url = ?", [url])
    existing_row = next(existing, None)
    
    if existing_row is None:
        # Never seen before - process it
        db["articles"].insert({
            "url": url,
            "content_hash": content_h,
            "last_processed": datetime.now(NY_TZ).isoformat(),
            "source": source,
        })
        return True
    
    if existing_row["content_hash"] != content_h:
        # Content changed - update hash and process
        db["articles"].update(url, {
            "content_hash": content_h,
            "last_processed": datetime.now(NY_TZ).isoformat(),
        })
        return True
    
    # Content unchanged - skip processing
    return False


def track_event_changes(event: Event) -> None:
    """
    Compare event against last-seen version and record changes.
    Implements Gap #3: lightweight field-change tracking.
    """
    db = get_db()
    event_id = event.dedup_key()
    
    # Fields we care about changes in
    tracked_fields = {
        "venue": event.venue,
        "start_datetime": event.start_datetime.isoformat() if event.start_datetime else None,
        "end_datetime": event.end_datetime.isoformat() if event.end_datetime else None,
        "price_tier": event.price_tier,
    }
    
    existing = db["events"].rows_where("event_id = ?", [event_id])
    existing_row = next(existing, None)
    
    if existing_row is None:
        # First time seeing this event - just record it
        db["events"].insert({
            "event_id": event_id,
            "title": event.title,
            "start_datetime": tracked_fields["start_datetime"],
            "end_datetime": tracked_fields["end_datetime"],
            "venue": tracked_fields["venue"],
            "price_tier": tracked_fields["price_tier"],
            "source_url": event.source_url,
            "last_seen": datetime.now(NY_TZ).isoformat(),
        })
        return
    
    # Check for changes in tracked fields
    changes = []
    for field, new_value in tracked_fields.items():
        old_value = existing_row[field]
        if old_value != new_value:
            changes.append((field, old_value, new_value))
    
    if changes:
        # Record changes
        changed_at = datetime.now(NY_TZ).isoformat()
        for field, old_val, new_val in changes:
            db["event_changes"].insert({
                "event_id": event_id,
                "field": field,
                "old_value": str(old_val) if old_val is not None else None,
                "new_value": str(new_val) if new_val is not None else None,
                "changed_at": changed_at,
            })
        
        # Update event record
        db["events"].update(event_id, {
            **{field: tracked_fields[field] for field in tracked_fields},
            "last_seen": changed_at,
        })
    else:
        # Just update last_seen timestamp
        db["events"].update(event_id, {
            "last_seen": datetime.now(NY_TZ).isoformat(),
        })


def get_recent_changes(days: int = 7) -> list[dict]:
    """
    Get events that changed in the last N days.
    Useful for a "What Changed This Week" notification.
    """
    db = get_db()
    from datetime import timedelta
    cutoff = datetime.now(NY_TZ) - timedelta(days=days)
    cutoff_iso = cutoff.isoformat()
    
    changes = db.execute("""
        SELECT 
            ec.event_id,
            e.title,
            ec.field,
            ec.old_value,
            ec.new_value,
            ec.changed_at
        FROM event_changes ec
        JOIN events e ON ec.event_id = e.event_id
        WHERE ec.changed_at >= ?
        ORDER BY ec.changed_at DESC
    """, [cutoff_iso]).fetchall()
    
    return [dict(row) for row in changes]


def cleanup_old_data(days: int = 90) -> None:
    """
    Garbage collection: remove events not seen in N days.
    Keeps state.db from growing unbounded.
    """
    db = get_db()
    from datetime import timedelta
    cutoff = datetime.now(NY_TZ) - timedelta(days=days)
    cutoff_iso = cutoff.isoformat()
    
    # Delete old event records
    db.execute("DELETE FROM events WHERE last_seen < ?", [cutoff_iso])
    
    # Delete orphaned change records
    db.execute("""
        DELETE FROM event_changes 
        WHERE event_id NOT IN (SELECT event_id FROM events)
    """)
    
    # Keep article ledger forever (small, useful for debugging)
