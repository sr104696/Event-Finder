# NYC Curated Events — Jules Work Pipeline

A personal taste filter for NYC events built in accordance with `NORTH_STAR.md`.

## Features Implemented in this Rework (`Jules Work/`)

1. **Content-Hash State Ledger (Gap 1)**:
   - Uses SQLite (`state.db`) to record article body SHA-256 hashes (`is_article_unchanged()`), allowing idempotent re-processing that skips unchanged articles while detecting in-place listicle updates.
2. **Cold-Start Ranking (Gap 2)**:
   - Ranks events primarily using explicit user preference filters (neighborhoods, categories, price tier, source quality) with `llm_vibe_match` acting as a tiebreaker prior to historical feedback data.
3. **Lightweight Field-Change Tracking (Gap 3)**:
   - Tracks changes to venue or start times across pipeline runs in `state.db`, populating `previous_venue`, `previous_start_datetime`, and `changed_at` on `Event` objects.
4. **Resilient LLM Parse Handling (`json_repair`)**:
   - `adapters/rss_llm.py` utilizes `json_repair` to fix minor LLM syntax slips before parsing.
5. **Robust Structured Data Extraction (`extruct`)**:
   - `adapters/eventbrite_jsonld.py` uses `extruct` for JSON-LD script extraction.
6. **Fuzzy Event Deduplication (`thefuzz`)**:
   - `pipeline.dedup()` uses `thefuzz` string distance matching on event titles and venues.

## Directory Structure

```
Jules Work/
  schema.py           - Event dataclass with change-tracking fields
  state.py            - SQLite state ledger & field-change tracking
  pipeline.py         - Deduplication (thefuzz), validation, cold-start scoring
  output.py           - Output writers for events.json and curated.ics
  main.py             - Orchestrator script
  library-verdicts.md - Deep evaluation of 14 ingested open-source libraries
  decision-log.md     - Detailed decision log and rationale
  adapters/
    meetup_ics.py        - Meetup ICS fetcher with RRULE recurrence expansion
    rss_llm.py           - RSS + LLM extraction with json_repair
    eventbrite_jsonld.py - Defensive Eventbrite JSON-LD parser with extruct
```

## Running Tests

From the repository root:
```bash
python -m pytest "Jules Work"
```
