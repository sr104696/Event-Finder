# Library evaluation and decision log

## Outcome

I adopted **no new third-party dependency**. The candidate rework implements
three specified gaps with the Python standard library and the existing
`dataclasses` model: a JSON content-hash ledger, lightweight changed-field
metadata, and explicit-filter-first cold-start scoring. This preserves the
north-star plain-file constraint and makes LLM work less wasteful without
increasing discovery volume.

## Source export verdicts

| Export | What the reviewed source is | Decision |
| --- | --- | --- |
| `sqlite-utils` | Full-featured SQLite Python API/CLI with migrations and plugin support. | **Reject for v1.** A JSON ledger covers the stated hashes and snapshots without schema/migration surface. Revisit only if querying history becomes a demonstrated need. |
| `thefuzz` | Fuzzy string matching package, with token-based and Levenshtein scorers. | **Reject for now.** The requested gaps do not require a dependency; fuzzy dedup needs real false-positive/false-negative evidence before risking merged unrelated events. |
| `facebook-event-aggregator` | Facebook scraper plus HTML/ICS exporters and package/workflow tooling. | **Reference only.** Its export shape supports the current ICS-file choice, but its browser/login-oriented input is outside the guarded source policy. |
| `ical` | Typed RFC 5545 parser/model with recurrence and timezone guides. | **Reject.** It overlaps the existing ICS stack; no failing Meetup recurrence demonstrated a migration benefit. |
| `recurring-ical-events` | A recurrence-expansion package with extensive calendar fixtures, including exclusions and DST cases. | **Keep existing dependency.** It is the appropriate focused layer over `icalendar`; the current adapter uses `.between()` to bound expansions. |
| `extruct` | HTML structured-data extractor for JSON-LD, microdata, RDFa, OpenGraph, and more. | **Defer.** It is a credible Eventbrite replacement candidate, but a passive Eventbrite listing fetch returned 405, so there was no accessible event-page corpus to prove better extraction. |
| `vanilla-calendar-pro` | Browser calendar UI component. | **Reject.** A UI is expressly out of scope. |
| `xmltodict` | XML-to-dict utility. | **Reject.** No RSS/ICS parser failure justified a fallback. |
| `atoma-infer` | Rust inference/back-end deployment project. | **Reject.** It adds local model-serving scope rather than improving a small hosted-LLM extraction step. |
| `selectolax` | Cython-backed HTML parser with CSS selectors. | **Defer.** Appropriate only if curated Eventbrite URL discovery becomes a measured HTML-volume problem. |
| `dataclasses` | Pre-stdlib/backport implementation of PEP 557 dataclasses. | **Reject.** Python 3.12 already supplies this API. |
| `json_repair` | Parser/repair library for malformed JSON and LLM output. | **Defer.** The environment has no `ANTHROPIC_API_KEY`, so no real malformed model response was observed. Do not conceal a malformed extraction without evidence and tests. |
| `msgspec` | High-performance typed serialization/validation library with compiled components. | **Reject.** The small plain dataclass plus explicit quarantine checks is clearer and adds no dependency. |
| `pydantic-core` | Rust-backed validation/serialization core used by Pydantic. | **Reject.** It has the same unproven value proposition here as `msgspec`, with greater implementation weight. |

## Live checks performed

* The configured Skint and Time Out RSS endpoints each responded successfully with RSS XML on 2026-09-01.
* A polite, one-shot request to Eventbrite's NYC listing returned HTTP 405. Per the source policy, no browser automation or evasive retry was attempted; Eventbrite parsing was therefore not changed.
* The public `nyc-data-science` Meetup ICS URL returned a valid `text/calendar` response, but its current feed expanded to zero events in a 60-day window. This confirms the fetch/parser path only, not a live recurrence/EXDATE case.
* No `ANTHROPIC_API_KEY` was present, so RSS LLM extraction, JSON-repair efficacy, and a full end-to-end Actions run could not be exercised. There is also no configured Git remote, so a secret cannot be installed, pushed, or dispatched from this checkout.

## Follow-up threshold

Adopt `extruct` only after saving a few normally accessible Eventbrite event-page fixtures and showing it recovers valid Event JSON-LD missed by the existing parser. Adopt `json_repair` only after recorded model output demonstrates recoverable JSON failures. Add SQLite only after JSON state needs real history queries or becomes operationally unreliable.
