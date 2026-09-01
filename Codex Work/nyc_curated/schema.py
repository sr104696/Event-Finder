"""Canonical, serializable event record for the isolated Codex rework."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
import hashlib
from typing import Any


@dataclass
class Event:
    title: str
    start_datetime: datetime
    end_datetime: datetime | None = None
    venue: str | None = None
    neighborhood: str | None = None
    price_tier: str | None = None
    category_tags: list[str] = field(default_factory=list)
    editorial_blurb: str | None = None
    source: str = ""
    source_url: str = ""
    image_url: str | None = None
    source_quality: int = 3
    date_confidence: float = 1.0
    extraction_status: str = "ok"
    llm_vibe_match: float | None = None
    vibe_score: float | None = None
    # A bounded, inspectable alternative to event-sourcing.
    previous_values: dict[str, str | None] = field(default_factory=dict)
    changed_at: datetime | None = None

    def identity_key(self) -> str:
        """Stable event identity for lightweight change tracking (venue may change)."""
        normalized_title = "".join(char.lower() for char in self.title if char.isalnum())
        raw = f"{normalized_title}|{self.start_datetime.date().isoformat()}"
        return hashlib.sha1(raw.encode()).hexdigest()[:16]

    def dedup_key(self) -> str:
        normalized_title = "".join(char.lower() for char in self.title if char.isalnum())
        normalized_venue = "".join(char.lower() for char in self.venue or "" if char.isalnum())
        normalized_venue = normalized_venue.replace("nyc", "").replace("newyork", "")
        raw = f"{normalized_title}|{self.start_datetime.date().isoformat()}|{normalized_venue}"
        return hashlib.sha1(raw.encode()).hexdigest()[:16]

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        for field_name in ("start_datetime", "end_datetime", "changed_at"):
            value = getattr(self, field_name)
            result[field_name] = value.isoformat() if value else None
        return result
