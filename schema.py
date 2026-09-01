"""
Canonical event schema for the NYC curation pipeline.

Every adapter (Meetup, RSS/LLM, Eventbrite, Reddit, Bandsintown, Partiful)
normalizes into this shape before dedup/scoring/output. Keeping this in one
place is what lets the rest of the pipeline stay source-agnostic.
"""
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional
import hashlib


@dataclass
class Event:
    title: str
    start_datetime: datetime                    # timezone-aware, America/New_York
    end_datetime: Optional[datetime] = None      # timezone-aware; None if unknown
    venue: Optional[str] = None
    neighborhood: Optional[str] = None           # normalized to a fixed NYC list, see neighborhoods.py
    price_tier: Optional[str] = None             # "free" | "$" | "$$" | "$$$" | None if unknown
    category_tags: list[str] = field(default_factory=list)
    editorial_blurb: Optional[str] = None

    source: str = ""                  # e.g. "meetup", "skint", "timeout", "eventbrite", "reddit", "bandsintown", "partiful"
    source_url: str = ""
    image_url: Optional[str] = None

    source_quality: int = 3           # 1-5, set per-adapter (Meetup ICS=5, LLM-extracted prose=3, etc.)
    date_confidence: float = 1.0      # 0-1. 1.0 for structured sources (ICS/JSON-LD), lower for LLM guesses.
    extraction_status: str = "ok"     # "ok" | "needs_review" | "rejected"

    llm_vibe_match: Optional[float] = None  # 0-100, set by rss_llm adapter from the few-shot prompt; None for structured sources
    vibe_score: Optional[float] = None      # 0-10 final ranking score, filled in by pipeline.score(), not by adapters

    def dedup_key(self) -> str:
        """Fuzzy-dedup input: normalized title + date + venue, hashed for storage/lookup."""
        norm_title = "".join(c.lower() for c in self.title if c.isalnum())
        norm_venue = "".join(c.lower() for c in (self.venue or "")
                              if c.isalnum())
        norm_venue = (norm_venue.replace("nyc", "")
                                 .replace("newyork", ""))
        date_key = self.start_datetime.date().isoformat() if self.start_datetime else ""
        raw = f"{norm_title}|{date_key}|{norm_venue}"
        return hashlib.sha1(raw.encode()).hexdigest()[:16]

    def to_dict(self) -> dict:
        d = asdict(self)
        d["start_datetime"] = self.start_datetime.isoformat() if self.start_datetime else None
        d["end_datetime"] = self.end_datetime.isoformat() if self.end_datetime else None
        return d
