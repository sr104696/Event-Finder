# Ingested Library Verdicts

This document contains evaluations of the 14 open-source library ingests provided in this repository. Each library is evaluated against the core test in `NORTH_STAR.md`: **"Does this reduce regret, or does it add discovery volume or infrastructure ahead of evidence it's needed?"**

---

## 1. `recurring-ical-events` (`niccokunzmann-python-recurring-ical-events-main.md`)
- **What it actually is**: A Python library that parses iCalendar (RFC 5545) RRULE recurrence specifications and expands recurring events into concrete datetime instances within a lookahead window.
- **North Star Verdict**: **ADOPTED / RECURRING USE CONFIRMED**
- **Justification**: Already integrated in `adapters/meetup_ics.py`. Recurring Meetup events (e.g. weekly language exchanges, monthly tech talks) would be silently dropped or misdated by a naive ICS parser. Drop-offs mean missing events the user would have loved. Upstream source check confirms accurate handling of EXDATE, timezone crossings, and duration calculations.

---

## 2. `allenporter/ical` (`allenporter-ical-main.md`)
- **What it actually is**: An alternative Python iCalendar parsing and rendering library with full RFC 5545 support.
- **North Star Verdict**: **REVIEWED, NOT ADOPTED**
- **Justification**: The existing `icalendar` + `recurring-ical-events` setup handles Meetup ICS feeds cleanly and correctly. Replacing a working library without an identified bug or missing feature would add churn and potential regressions without reducing regret.

---

## 3. `extruct` (`scrapinghub-extruct-master.md`)
- **What it actually is**: A structured metadata extraction library for HTML that parses JSON-LD, Microdata, OpenGraph, RDFa, and Dublin Core tags into clean Python dictionaries.
- **North Star Verdict**: **ADOPTED FOR EVENTBRITE / STRUCTURED HTML**
- **Justification**: Replaces fragile regex/manual JSON-LD script tag scraping in `adapters/eventbrite_jsonld.py`. Handles multi-script blocks, nested `@graph` wrappers, and microdata/OpenGraph fallbacks gracefully. Improves extraction reliability from structured HTML sources.

---

## 4. `thefuzz` (`seatgeek-thefuzz-master.md`)
- **What it actually is**: A fuzzy string matching library based on Levenshtein distance (formerly `fuzzywuzzy`).
- **North Star Verdict**: **EVALUATED & ADOPTED FOR DEDUP (OR STDLIB DIFFLIB EQUIVALENT)**
- **Justification**: Reduces regret by catching duplicate events across different sources where titles or venue names vary slightly (e.g., "Live Music @ House of Yes" vs "House of Yes: Live Music"). Used in `pipeline.py` alongside normalized hash matching.

---

## 5. `json_repair` (`mangiucugna-json_repair-main.md`)
- **What it actually is**: A lightweight Python library that fixes common JSON formatting errors in LLM outputs (missing commas, trailing commas, unclosed quotes, backtick wrappers, single quotes).
- **North Star Verdict**: **ADOPTED FOR RSS LLM ADAPTER**
- **Justification**: `adapters/rss_llm.py` previously performed a plain `json.loads()`, dropping an entire RSS article's extracted events whenever the LLM made a minor syntax error. Adding `json_repair.repair_json()` before parsing prevents silent event loss.

---

## 6. `sqlite-utils` (`simonw-sqlite-utils-main.md`)
- **What it actually is**: A Python utility library and CLI tool for manipulating SQLite databases.
- **North Star Verdict**: **ADOPTED FOR STATE LEDGER & CHANGE TRACKING**
- **Justification**: A local SQLite file (`state.db`) is zero-infrastructure (no background process or database server). It enables Gap 1 (content-hash ledger to skip redundant RSS extractions) and Gap 3 (lightweight field change tracking) with clean query support, fulfilling `NORTH_STAR.md` principles.

---

## 7. `facebook-event-aggregator` (`Denperidge-facebook-event-aggregator-main.md`)
- **What it actually is**: An automated event scraper for Facebook pages that exports `.ics` files and publishes via GitHub Actions.
- **North Star Verdict**: **REVIEWED AS ARCHITECTURAL REFERENCE**
- **Justification**: Facebook is login-walled and out-of-scope for automated scraping per `NORTH_STAR.md`. However, its GitHub Actions workflow pattern and static ICS export structure served as a good sanity check for `output.py` and `.github/workflows/fetch.yml`.

---

## 8. `xmltodict` (`martinblech-xmltodict-master.md`)
- **What it actually is**: A Python module that converts XML data into native Python dictionaries.
- **North Star Verdict**: **REVIEWED, NOT NEEDED AT PRESENT**
- **Justification**: `feedparser` already parses RSS and Atom feeds reliably into python dicts. `xmltodict` is kept as a potential fallback for malformed feeds if standard RSS parsers choke.

---

## 9. `selectolax` (`rushter-selectolax-master.md`)
- **What it actually is**: A fast HTML parser built on the Modest engine.
- **North Star Verdict**: **REVIEWED, DEFERRED**
- **Justification**: Relevant if high-volume HTML scraping of category/listing pages is added in the future. v1 relies on structured ICS, RSS, and targeted JSON-LD, making heavyweight HTML crawling unnecessary.

---

## 10. `dataclasses` (`ericvsmith-dataclasses-master.md`)
- **What it actually is**: Python 3.6 backport of the `dataclasses` module (PEP 557).
- **North Star Verdict**: **REVIEWED, NOT APPLICABLE**
- **Justification**: Target environment is Python 3.12, where `dataclasses` is built into the standard library.

---

## 11. `msgspec` (`msgspec-msgspec-main.md`)
- **What it actually is**: A high-performance serialization and validation library for JSON, MessagePack, TOML, and YAML.
- **North Star Verdict**: **REVIEWED, NOT ADOPTED**
- **Justification**: `schema.py` uses standard library `@dataclass`, and `pipeline.validate()` handles runtime checks. Adding `msgspec` introduces binary dependencies without providing meaningful benefits over the clear, custom validation already in place.

---

## 12. `pydantic-core` (`pydantic-pydantic-core-8a5edab282632443.txt`)
- **What it actually is**: Rust-backed core validation engine for Pydantic v2.
- **North Star Verdict**: **REVIEWED, NOT ADOPTED**
- **Justification**: Alternative to `msgspec`. Plain dataclasses plus `pipeline.validate()` remain preferred per `NORTH_STAR.md` to keep code light, readable, and free from heavy validation framework overhead.

---

## 13. `atoma-infer` (`AtomaAI-atoma-infer-main.md`)
- **What it actually is**: A Rust inference engine and API proxy for LLM deployments.
- **North Star Verdict**: **REVIEWED, NOT APPLICABLE**
- **Justification**: The pipeline uses standard LLM client APIs (Anthropic/Gemini) directly for RSS extraction. Standalone inference infrastructure is out of scope.

---

## 14. `vanilla-calendar-pro` (`uvarov-frontend-vanilla-calendar-pro-main.md`)
- **What it actually is**: A lightweight JavaScript calendar component for browser UIs.
- **North Star Verdict**: **REVIEWED, OUT OF SCOPE FOR V1**
- **Justification**: `NORTH_STAR.md` strictly defers frontend UIs until `events.json` and `curated.ics` prove their value. Noted for potential future phase use.
