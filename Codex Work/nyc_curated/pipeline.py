"""Curation stages plus a small JSON state ledger; no database service."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from .schema import Event

NY_TZ = ZoneInfo("America/New_York")
STATE_VERSION = 2
TRACKED_FIELDS = ("venue", "start_datetime", "end_datetime", "price_tier")


def content_hash(content: str) -> str:
    """Stable hash of the extracted article body, including in-place edits."""
    normalized = "\n".join(line.rstrip() for line in content.replace("\r\n", "\n").split("\n")).strip()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": STATE_VERSION, "content_hashes": {}, "event_snapshots": {}}
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        # Preserve availability; a malformed cache must not publish guessed events.
        return {"version": STATE_VERSION, "content_hashes": {}, "event_snapshots": {}}
    state.setdefault("content_hashes", {})
    state.setdefault("event_snapshots", {})
    state["version"] = STATE_VERSION
    return state


def article_is_unchanged(state: dict[str, Any], url: str, article_text: str) -> bool:
    return bool(url) and state["content_hashes"].get(url) == content_hash(article_text)


def record_article(state: dict[str, Any], url: str, article_text: str) -> None:
    if url:
        state["content_hashes"][url] = content_hash(article_text)


def apply_field_changes(events: list[Event], state: dict[str, Any], now: datetime | None = None) -> None:
    """Attach prior values only when an identified event changed since last run."""
    timestamp = now or datetime.now(NY_TZ)
    snapshots: dict[str, dict[str, str | None]] = state["event_snapshots"]
    for event in events:
        key = event.identity_key()
        current = {
            "venue": event.venue,
            "start_datetime": event.start_datetime.isoformat(),
            "end_datetime": event.end_datetime.isoformat() if event.end_datetime else None,
            "price_tier": event.price_tier,
        }
        prior = snapshots.get(key)
        if prior:
            changed = {name: prior.get(name) for name in TRACKED_FIELDS if prior.get(name) != current.get(name)}
            if changed:
                event.previous_values = changed
                event.changed_at = timestamp
        snapshots[key] = current


def save_state(state: dict[str, Any], path: Path) -> None:
    # Limit only the URL-content ledger. Event snapshots naturally age out with output horizon.
    hashes = state["content_hashes"]
    if len(hashes) > 2_000:
        state["content_hashes"] = dict(list(hashes.items())[-2_000:])
    state["updated_at"] = datetime.now(NY_TZ).isoformat()
    path.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")


def dedup(events: list[Event]) -> list[Event]:
    seen: dict[str, Event] = {}
    for event in events:
        seen.setdefault(event.dedup_key(), event)
    return list(seen.values())


def expire(events: list[Event], lookahead_days: int = 14, now: datetime | None = None) -> list[Event]:
    current = now or datetime.now(NY_TZ)
    horizon = current + timedelta(days=lookahead_days)
    return [event for event in events if current <= event.start_datetime <= horizon]


def score_cold_start(
    events: list[Event], *, preferred_neighborhoods: set[str], preferred_categories: set[str]
) -> list[Event]:
    """Rank explainable stated filters first; model vibe is only a tiebreaker."""
    normalized_neighborhoods = {value.lower() for value in preferred_neighborhoods}
    normalized_categories = {value.lower() for value in preferred_categories}
    for event in events:
        score = 0.0
        if event.neighborhood and event.neighborhood.lower() in normalized_neighborhoods:
            score += 4.0
        if normalized_categories.intersection(tag.lower() for tag in event.category_tags):
            score += 3.0
        if event.price_tier == "free":
            score += 1.5
        elif event.price_tier == "$":
            score += 0.5
        # Never let a speculative LLM preference outrank explicit cold-start filters.
        score += (event.llm_vibe_match or 0.0) / 1000.0
        event.vibe_score = round(min(10.0, score), 2)
    return events
