# Kiro Work - Implementation of Gaps & Library Adoptions

This directory contains the updated/new modules implementing the three priority gaps from CODER_HANDOFF_PROMPT.md and adopting the libraries evaluated in `library-verdicts.md`.

## Files in this directory

### Documentation
- **library-verdicts.md** - Comprehensive evaluation of all 14 ingested libraries against NORTH_STAR.md
- **README.md** - This file

### New/Updated Modules

#### state.py (NEW - Implements Gaps #1 & #3)
SQLite-based state management replacing state.json.

**Gap #1 - Content-hash-based ledger:**
- `should_process_article()` - Hashes article content, skips re-processing if unchanged
- Prevents wasting LLM calls on unchanged Skint/TimeOut articles

**Gap #3 - Field-change tracking:**
- `track_event_changes()` - Records when venue/time/price changes
- `get_recent_changes()` - Query for "What Changed This Week" notifications
- Stores only changed fields, not full event history (lightweight per spec)

**Why SQLite:**
- Still just a file (state.db, no server/service)
- Queryable with SQL instead of JSON manipulation
- Atomic updates, no corruption risk
- Garbage collection via `cleanup_old_data()`

#### eventbrite_jsonld.py (UPDATED - Library: extruct)
Replaces hand-rolled regex + JSON parsing with extruct's battle-tested JsonLdExtractor.

**Why extruct:**
- Handles @graph wrappers, arrays, multiple script tags automatically
- ~40 lines of defensive code replaced with one library call
- Used in production by Scrapinghub

#### rss_llm.py (UPDATED - Integrates Gap #1)
Integrates content-hash ledger check before LLM extraction.

**Before:** Every RSS article re-extracted on every run (wastes API calls)
**After:** Only extract if article content changed

#### pipeline.py (UPDATED - Integrates Gaps #2 & #3)
**Gap #2 - Cold-start ranking:**
- `score(cold_start=bool)` parameter
- When `cold_start=True`, reduces weight on `vibe_match` (no feedback data yet)
- Weights explicit filters (price, source_quality) higher

**Gap #3 integration:**
- Calls `track_event_changes()` after dedup/validation
- Calls `cleanup_old_data()` for garbage collection

#### requirements.txt (UPDATED)
Added:
- `sqlite-utils>=4.2`
- `extruct>=0.18`

## Integration Instructions

To integrate these into the top-level repo:

1. **Replace existing files:**
   - `eventbrite_jsonld.py` (top-level) ← `Kiro Work/eventbrite_jsonld.py`
   - `rss_llm.py` (top-level) ← `Kiro Work/rss_llm.py`
   - `pipeline.py` (top-level) ← `Kiro Work/pipeline.py`
   - `requirements.txt` (top-level) ← `Kiro Work/requirements.txt`

2. **Add new file:**
   - `state.py` (top-level) ← `Kiro Work/state.py`

3. **Update main.py:**
   ```python
   from pipeline import track_changes, cleanup_state
   
   # After dedup/validation, before scoring:
   track_changes(all_events)
   
   # At end of run:
   cleanup_state(days=90)
   ```

4. **Update .gitignore:**
   Add `state.db` and `state.db-*` (SQLite journal files)

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Testing Status

See decision-log.md for live testing results once completed.

## Not Yet Implemented

**json_repair adoption:** Deferred pending live testing. If Claude Haiku produces parse-able malformed JSON, add:
```python
import json_repair
# in rss_llm.py after json.loads() failure
try:
    items = json.loads(json_repair.repair(text))
except:
    # skip
```

**Cold-start detection:** `main.py` needs logic to detect if this is the first 1-2 weeks of operation and pass `cold_start=True` to `score()`. Could check if state.db is empty or if oldest event < 14 days old.
