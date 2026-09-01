# Library Evaluation Verdicts

Evaluated against NORTH_STAR.md's test: **Does this reduce regret, or does it increase discovery volume / infrastructure ahead of need?**

## 1. niccokunzmann/python-recurring-ical-events

**What it is:** The actual upstream library already in use by `meetup_ics.py` for RRULE expansion. Handles RFC 5545 recurrence rules comprehensively.

**Current usage:** `meetup_ics.py` line 33:
```python
instances = recurring_ical_events.of(cal).between(start, end)
```

**Verdict: ALREADY ADOPTED, KEEP**

**Why:** This is the single most critical library in the pipeline. Meetup ICS feeds represent recurring events ("every Tuesday running club") as a single VEVENT with an RRULE property. Without RRULE expansion, the pipeline would silently drop or misdate all recurring events. The library is already doing the job correctly.

**Edge cases to verify:**
- EXDATE handling (excluded dates in a recurring series)
- Timezone-crossing recurrence (e.g., across DST boundaries)
- Modified instances (one occurrence of a recurring event changed)

The library's test suite shows comprehensive coverage of these cases (issue_148_exdate_and_rdate_*, issue_48_daylight_aware_repeats.ics, etc.). Current usage appears correct.

**Action:** Run live test against real Meetup groups with recurring events to confirm no issues. No code changes needed.

---

## 2. allenporter/ical

**What it is:** Alternative Python iCalendar/RFC 5545 library with recurring event support.

**Verdict: NOT NEEDED**

**Why:** `recurring-ical-events` is already working and battle-tested (237 files, extensive test suite covering dozens of edge cases). Switching libraries requires a concrete failure case in the current implementation. The handoff prompt explicitly warns against this: "Worth a real comparison against `recurring-ical-events` on the specific edge cases Meetup's feeds actually produce — don't switch libraries without a concrete reason found in testing."

**Action:** Note as a fallback option if live testing reveals an edge case `recurring-ical-events` can't handle. Otherwise, skip.

---

## 3. scrapinghub/extruct

**What it is:** General-purpose structured data extraction library for HTML (JSON-LD, Microdata, OpenGraph, RDFa, Microformat).

**Checking current Eventbrite implementation...**

Reading `eventbrite_jsonld.py`: Currently uses hand-rolled regex + JSON parsing:
```python
LD_JSON_RE = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)
```

Then manually flattens arrays/@graph wrappers in `_flatten_ld_blocks()`.

**extruct provides:**
- `JsonLdExtractor().extract_items(tree, base_url=base_url)` - battle-tested extraction
- Handles multiple script tags, @graph wrappers, arrays automatically
- Used by Scrapinghub in production scraping infrastructure
- Clean API: `extruct.extract(html, syntaxes=["json-ld"])`

**Verdict: ADOPT**

**Why:** This directly addresses the handoff prompt's note: "This is the single highest-leverage candidate in this list if it's as capable as its reputation suggests." It replaces ~40 lines of defensive regex/JSON-parsing code with a single battle-tested call. Eventbrite's JSON-LD can appear as single objects, arrays, or @graph wrappers with multiple script tags - extruct handles all of them.

**Action:** Rewrite `eventbrite_jsonld.py` to use extruct. Test against live Eventbrite pages.

---

## 4. seatgeek/thefuzz

**What it is:** Fuzzy string matching library (Levenshtein distance-based), fork of the original fuzzywuzzy.

**Current dedup implementation:** `schema.py` `dedup_key()`:
```python
def dedup_key(self) -> str:
    norm_title = "".join(c.lower() for c in self.title if c.isalnum())
    norm_venue = "".join(c.lower() for c in (self.venue or "") if c.isalnum())
    norm_venue = (norm_venue.replace("nyc", "").replace("newyork", ""))
    date_key = self.start_datetime.date().isoformat() if self.start_datetime else ""
    raw = f"{norm_title}|{date_key}|{norm_venue}"
    return hashlib.sha1(raw.encode()).hexdigest()[:16]
```

This is **exact matching after normalization**, not fuzzy matching.

**Verdict: NOT NEEDED YET**

**Why:**
1. The current exact-match-after-normalization approach is working. No evidence yet of missed dupes.
2. Fuzzy matching has a cost: false positives. "Jazz Night" and "Jazz Brunch" might fuzzy-match but be different events.
3. SESSION_LOG explicitly notes this was discussed and deferred: the architecture supports it (dedup runs before output), but it needs evidence of actual false negatives before adding complexity.
4. If needed later, `difflib.SequenceMatcher` (stdlib) might be sufficient before adding a dependency.

**Action:** Test current dedup against real data first. Only adopt if live testing shows clear duplicate events slipping through with slightly different titles. Document examples if found.

---

## 5. mangiucugna/json_repair

**What it is:** Library that repairs malformed JSON (missing quotes, trailing commas, truncated arrays, etc.) before parsing.

**Current LLM extraction:** `rss_llm.py` line 96:
```python
try:
    items = json.loads(text)
except json.JSONDecodeError:
    print(f"[rss_llm] could not parse extraction for {link!r}, skipping")
    return []
```

On parse failure, **all events from that article are silently dropped**.

**Verdict: CONDITIONALLY ADOPT - TEST FIRST**

**Why:** The handoff prompt says: "Worth adopting if it's as low-overhead as it sounds — but test it against real Claude Haiku output first, don't assume it's needed without evidence of actual parse failures."

This is a perfect case for test-first adoption:
1. Run RSS extraction against live Skint/TimeOut feeds
2. Check logs for JSON parse failures
3. If failures occur, inspect whether they're repair able (e.g., trailing comma) or genuine garbage
4. Only adopt if repair would recover real events

**Action:** Test live RSS/LLM extraction first. If parse failures occur and inspection shows they're repairable formatting issues (not fundamental extraction failures), adopt json_repair with a try/fallback pattern:
```python
try:
    items = json.loads(text)
except json.JSONDecodeError:
    try:
        items = json.loads(json_repair.repair(text))
    except:
        # log and skip
```

---

## 6. msgspec / pydantic-core

**What they are:** 
- `msgspec`: Fast JSON/MessagePack schema validation & serialization
- `pydantic-core`: The Rust core of Pydantic v2, provides validation/coercion

**Current validation:** `pipeline.validate()` - hand-rolled checks for missing title, naive datetime, end-before-start, implausible duration.

**Current schema:** Plain `@dataclass` in `schema.py`.

**Verdict: NOT NEEDED**

**Why:**
1. **The handoff prompt explicitly warns about this**: "only if it demonstrably catches something the current validation doesn't, or measurably reduces code versus what's there. Given `NORTH_STAR.md`'s bias against adding infrastructure ahead of need, the default should be 'keep the plain dataclass' unless you find a concrete case it fails on."

2. Current validation is ~35 lines and catches the real issues: malformed adapter output. It's working code.

3. These are **alternatives to each other**, not complementary. Picking either means a significant rewrite for uncertain benefit.

4. No evidence yet that the current approach is failing.

**Action:** Keep the plain dataclass + `pipeline.validate()`. Note these as alternatives if type coercion failures emerge in production (e.g., an adapter returns a string where a datetime is expected and it's caught late).

---

## 7. simonw/sqlite-utils

**What it is:** High-level Python library for working with SQLite databases, from Simon Willison (Datasette creator). Not a server, just a nicer API over the stdlib `sqlite3` module.

**Current state storage:** `state.json` - a JSON file with:
```json
{
  "seen_urls": ["url1", "url2", ...],
  "updated_at": "timestamp"
}
```

Trimmed to last 2000 URLs.

**Current events storage:** `events.json` - flat list, regenerated fully each run.

**Handoff prompt notes:**
- Gap #1: Need content-hash-based ledger (not just URL tracking)
- Gap #3: Need lightweight field-change tracking (store previous venue/time when changed)
- "SQLite file is operationally still 'just a file' (no server, no service to run), so it may be in the spirit of that rule rather than a violation"

**Verdict: ADOPT FOR STATE LEDGER**

**Why:**
1. **Solves real gaps**: Content-hash ledger and field-change tracking are easier to implement with SQL queries than nested JSON manipulation.

2. **Stays within the north star**: SQLite is a file-based database. No server, no service, no Docker, no Postgres/Supabase infrastructure. It's `state.db` instead of `state.json`. The GitHub Actions workflow can commit it alongside `events.json` and `curated.ics`.

3. **Makes gap #1 trivial**: Instead of tracking seen URLs, track content hashes:
   ```python
   db["articles"].insert({"url": url, "content_hash": hash, "last_processed": timestamp})
   # Skip if hash unchanged:
   if db.execute("SELECT 1 FROM articles WHERE content_hash = ?", [hash]).fetchone():
       skip
   ```

4. **Makes gap #3 clean**: Store event history:
   ```python
   db["event_changes"].insert({
       "event_id": dedup_key,
       "field": "venue",
       "old_value": "Old Venue",
       "new_value": "New Venue",
       "changed_at": timestamp
   })
   ```

5. **Queryable for future features**: "Show me events that changed this week", "Which sources produce the most duplicates", etc. JSON requires full-file loads and loops.

**Action:** Replace `state.json` with `state.db` using sqlite-utils. Implement content-hash ledger and field-change tracking (gaps #1 and #3).



---

## 8. rushter/selectolax

**What it is:** Fast HTML/XML parser (lxml/Modest bindings), optimized for speed over feature completeness.

**Verdict: NOT NEEDED YET**

**Why:** The handoff prompt explicitly categorizes this: "relevant only if/when the pipeline needs to parse HTML at volume (e.g. discovering Eventbrite event URLs from a category/listing page, which isn't built yet). Not urgent; note it as a candidate for that specific future piece."

**Action:** Note as a future optimization if/when Eventbrite category-page scraping is added. Current usage (single-page JSON-LD extraction) doesn't justify optimization.

---

## 9. martinblech/xmltodict

**What it is:** Converts XML to Python dictionaries.

**Verdict: NOT NEEDED**

**Why:** 
1. Current pipeline uses `feedparser` (for RSS) and `icalendar` (for ICS), both purpose-built and working.
2. The handoff prompt: "likely relevant only as a fallback if `feedparser` or `icalendar` choke on a malformed real-world feed; not clearly needed yet. Evaluate against real failures, not hypothetically."
3. No evidence of parse failures yet.

**Action:** Note as a fallback if RSS or ICS parsing fails in production. Otherwise, skip.

---

## 10. uvarov-frontend/vanilla-calendar-pro

**What it is:** Frontend JavaScript calendar UI component.

**Verdict: OUT OF SCOPE**

**Why:** NORTH_STAR.md explicitly: "No UI" until v1's plain files prove worth building on. This is frontend code for a phase that hasn't been justified yet.

**Action:** Note for phase 2 if/when a web UI is built. Skip for v1.

---

## 11. ericvsmith/dataclasses

**What it is:** Backport of PEP 557 dataclasses for Python < 3.7.

**Verdict: NOT APPLICABLE**

**Why:** This project targets Python 3.12 (see `.github/workflows/fetch.yml`). Dataclasses are in stdlib since 3.7. This repo is irrelevant.

**Action:** Reviewed, not applicable. Skip.

---

## 12. AtomaAI/atoma-infer

**What it is:** Low-level LLM inference engine (Rust/CUDA). A vLLM-style inference runtime for serving LLMs.

**Verdict: OUT OF SCOPE**

**Why:**
1. This is infrastructure for **running** LLMs, not **calling** them. The pipeline already calls Anthropic's Claude API via the `anthropic` Python SDK.
2. Self-hosting LLM inference would require GPU infrastructure, model weights, deployment complexity - completely contrary to NORTH_STAR.md's "no infrastructure ahead of need" principle.
3. The handoff prompt: "Inventing a use for a library because it's in the pile is exactly the kind of thing `NORTH_STAR.md` warns against."

**Action:** Reviewed, no fit. Skip.

---

## 13. Denperidge/facebook-event-aggregator

**What it is:** Scrapes Facebook public events pages, exports to static site + ICS files, publishes via GitHub Pages/Actions.

**Verdict: REFERENCE FOR WORKFLOW, NOT INTEGRATION**

**Why:**
1. **Different source, same output pattern**: This project does Facebook → ICS; our project does Meetup/Skint/Eventbrite → ICS. The sources differ, but the GitHub Actions + ICS output approach is identical.

2. **Already noted in handoff prompt**: "worth skimming its GitHub Actions workflow and ICS serialization approach."

3. **Not a library to adopt**: This is a complete project, not a reusable component.

**Action:** Read its GitHub Actions workflow structure and ICS-writing code to compare against our `fetch.yml` and `output.py`. Look for patterns we should adopt (error handling, artifact uploads, ICS metadata fields, etc.).



---

## Summary

**ADOPT (3):**
1. **extruct** - Replace hand-rolled Eventbrite JSON-LD parsing (high-leverage, battle-tested)
2. **sqlite-utils** - Replace state.json for content-hash ledger + field-change tracking (gaps #1 & #3)
3. **json_repair** - CONDITIONALLY, only if live testing shows Claude Haiku produces parse-able malformed JSON

**ALREADY IN USE, KEEP (1):**
1. **recurring-ical-events** - Critical for RRULE expansion, working correctly

**NOT NEEDED / OUT OF SCOPE (8):**
1. **allenporter/ical** - No failure case to justify switching from recurring-ical-events
2. **thefuzz** - Fuzzy dedup not needed until evidence of false negatives
3. **msgspec/pydantic-core** - Plain dataclass + validate() working, no failure case
4. **selectolax** - Only relevant for future Eventbrite category scraping
5. **xmltodict** - Only needed if feedparser/icalendar fail (no evidence yet)
6. **vanilla-calendar-pro** - Frontend UI, explicitly deferred per NORTH_STAR
7. **dataclasses** - Backport for Python < 3.7, not applicable to 3.12
8. **atoma-infer** - LLM inference engine, completely out of scope

**REFERENCE (1):**
1. **facebook-event-aggregator** - Compare workflow structure, not integrate

**Test-first adoptions:** json_repair requires live RSS testing first. thefuzz requires dedup testing first.

**Next actions:**
1. Implement extruct in eventbrite_jsonld.py
2. Implement sqlite-utils for state.db (gaps #1 & #3)
3. Test all three adapters against live sources
4. Decide json_repair based on test results

