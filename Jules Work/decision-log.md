# Decision Log & Architectural Rationale — Jules Work

This document captures the engineering decisions, library evaluations, and gap list implementation details completed by Jules.

---

## 1. Governing Principle Alignment (`NORTH_STAR.md`)

Every change and library adoption was evaluated against the primary test:
> **"Does this reduce regret, or does it add discovery volume or infrastructure ahead of evidence it's needed?"**

---

## 2. Gap List Implementation Details

### Gap 1: Content Hash State Ledger (`Jules Work/state.py`)
- **Problem**: Previously, `state.json` only tracked seen source URLs. RSS articles (e.g. on The Skint or TimeOut) are edited in place under the same URL as new weekend events get posted. Re-extracting unchanged articles wasted LLM API tokens, while ignoring updated URLs led to missed events.
- **Solution**: Implemented SHA-256 body content hashing stored in a zero-infrastructure SQLite database (`state.db`). `is_article_unchanged(url, body)` ensures re-extraction happens only when the actual prose content changes.

### Gap 2: Cold-Start Ranking (`Jules Work/pipeline.py`)
- **Problem**: During initial deployment when no user feedback log exists, relying heavily on `llm_vibe_match` introduces noise from single-prompt LLM variance.
- **Solution**: Updated `pipeline.score()` to prioritize explicit user filters (neighborhood matches, category tags, price tiers, source quality) as primary scoring components, using `llm_vibe_match` as a secondary tiebreaker.

### Gap 3: Field-Change Tracking (`Jules Work/state.py` & `Jules Work/schema.py`)
- **Problem**: When venue or datetime details shift between pipeline runs, overwrite-only behavior loses context for downstream notifications.
- **Solution**: Added `previous_venue`, `previous_start_datetime`, and `changed_at` fields to `Event`. `track_field_changes()` compares new incoming events against SQLite `event_history` records and populates change fields when updates occur.

---

## 3. Adopted Libraries & Key Enhancements

1. **`recurring-ical-events`**:
   - Upstream PyPI source verified. Ensures RRULE recurrence in Meetup ICS feeds is accurately expanded into concrete datetime instances within the lookahead window without dropping events.
2. **`json_repair`**:
   - Integrated in `adapters/rss_llm.py`. Fallback for LLM responses with syntax glitches (unclosed quotes, trailing commas), eliminating silent article drop-offs.
3. **`extruct`**:
   - Integrated in `adapters/eventbrite_jsonld.py`. Enhances structured JSON-LD parsing from HTML pages with robust handling of `@graph` wrappers and multi-script tags.
4. **`thefuzz`**:
   - Integrated in `pipeline.dedup()`. Implements Levenshtein-based fuzzy matching on titles and venues to catch duplicate event listings across multiple sources.
5. **`sqlite-utils` / Native `sqlite3`**:
   - Used for zero-infrastructure state tracking (`state.db`), keeping local state structured and queryable without server overhead.

---

## 4. Evaluated and Deferred / Rejected Libraries

- **`allenporter/ical`**: Kept `recurring-ical-events` + `icalendar` as it functions reliably for Meetup ICS.
- **`msgspec` / `pydantic-core`**: Standard `@dataclass` + `pipeline.validate()` maintained per `NORTH_STAR.md` to avoid unnecessary binary validator complexity.
- **`selectolax`**: Deferred until full HTML crawling is needed.
- **`atoma-infer` / `vanilla-calendar-pro`**: Direct LLM APIs and pre-built plain output files (`events.json`, `curated.ics`) satisfy current requirements. Frontend UI is deferred per `NORTH_STAR.md`.

---

## 5. Verification & Testing Summary

- 6 unit tests passing across `test_state.py`, `test_pipeline.py`, `test_changes.py`, `test_json_repair.py`, and `test_extruct_fuzzy.py`.
- Verified live RSS parsing against `https://theskint.com/feed/`.
- Verified synthetic end-to-end execution of `main.py` producing `events.json` and `curated.ics`.
