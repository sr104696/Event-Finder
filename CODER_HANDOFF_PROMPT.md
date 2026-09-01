# NYC Curated Events — handoff prompt for a coding agent / IDE with GitHub access

Paste this whole document as the initial prompt. Alongside it, this
upload includes the full `nyc-curator/` repo — working v1 code,
`NORTH_STAR.md`, and `SESSION_LOG.md` (see below) — and separately, a
`gitingest` export of one or more of my existing GitHub repos that may
contain reusable material. Read the ingest before writing new code, and
prefer extending what's already mine over writing parallel
implementations.

**Read `NORTH_STAR.md` first, before this document.** It's one page and
it's the actual point: this is a personal taste filter, not an events
platform, and every decision below and every future one should be judged
against the test it states — reduce regret, don't maximize discovery
volume. This handoff prompt and `SESSION_LOG.md` explain how the project
got here and what's left to do; `NORTH_STAR.md` is what governs when
those two disagree with a new idea, a diff, or something pulled in from
another repo. If you only have room to internalize one file's worth of
context, make it that one.

**`SESSION_LOG.md`** is a summary of the design conversation that
produced this spec — a genuinely long, multi-turn discussion (including
several turns signed with other AI assistants' names) that repeatedly
converged on the same architecture from different angles, caught at
least one fabricated tool-name claim along the way, and corrected at
least one of its own unverified claims after checking a primary source.
It's context for *why* the decisions below were made, not a second set of
instructions — treat it as history, and defer to `NORTH_STAR.md` and this
document where anything conflicts.

**This repo will grow.** Expect the gitingest export, and possibly future
diffs or PRs proposing changes, to land alongside what's here. Review
all of it seriously — don't dismiss something for arriving late. But run
every proposed addition through the north-star test before merging it in:
if it doesn't serve "a small number of things worth actually going to,"
it's a candidate for a "considered, not adopted" note, not a merge,
however well-argued it is. The main goal stays the north star; everything
else, including this document, serves it.

## What this project is

A personal curation layer over NYC's fragmented events sources — Meetup,
Eventbrite, The Skint, TimeOut, and others — built to answer "what are the
coolest things happening in the categories and neighborhoods I care
about," not to be a general-purpose citywide events database. The product
framing that survived a long design discussion (below) is: **optimize for
reducing regret, not for maximizing discovery.** Success is "I didn't miss
anything I'd have loved," not "I found 400 events."

This spec is the product of an extended multi-model design conversation
(Claude plus several other assistants weighing in in the same thread).
The architecture converged independently from several directions, which
is the reason to trust it's reasonably sound — but treat every claim
below as what it is: either verified against a primary source, tested by
running code, or explicitly marked as an assumption/opinion. Don't
re-derive the architecture from scratch; do stress-test the parts marked
unverified.

## Source landscape (verified, as of Sept 2026)

- **Meetup**: No usable free API. As of Feb 2025 all integrations require
  GraphQL + an active Meetup Pro subscription + OAuth app approval that
  isn't guaranteed even with Pro. Workaround: each public group exposes an
  unauthenticated ICS export at `https://www.meetup.com/<group-slug>/events/ical/`.
  This is a curated-list strategy, not open discovery — there is no
  citywide Meetup search substitute.
- **Eventbrite**: Public search API (`/v3/events/search/`) deprecated Dec
  2019, turned off Feb 2020. What remains serves organizers managing their
  own events, not third-party discovery. Workaround: individual public
  event pages embed schema.org `Event` JSON-LD (`<script
  type="application/ld+json">`) intended for Google's rich results —
  parseable without auth. Eventbrite also has real bot protection, so this
  should be treated as best-effort/opportunistic, not a core source:
  plain fetch, parse defensively, skip silently if blocked. Do not deploy
  stealth headless-browser scraping to force it through — that's an
  unnecessary arms race for a supplementary source in an unattended job.
- **Partiful**: No public API, invite/link-based, not built for
  discovery. An unofficial reverse-engineered wrapper exists on GitHub
  (cerebralvalley/partiful-api) but is fragile and low-reward. Don't
  automate it — take manual link submission (fetch Open Graph tags only:
  title/image/date if present).
- **The Skint / TimeOut**: Both are RSS-available but the RSS content is
  prose (blog posts / listicles), not structured event fields. Requires
  LLM extraction, not parsing.
- **Bandsintown**: Has a real public API, but it's **artist-centric only**
  (query by artist name/ID/Facebook page) — there is no city/location
  query endpoint. Only useful if you maintain a followed-artist list, not
  as citywide concert discovery. (This was asserted incorrectly earlier
  in the design discussion as "a real public API for concerts by
  location" — corrected after checking Bandsintown's actual API docs.)
- **DoNYC**: Itself a pre-aggregated events site with RSS. Useful as a
  supplementary/backup source, not a primary one (it's itself scraping
  many of the same underlying sources).
- **Reddit** (r/AskNYC, r/nyc, r/nycmeetups): No free full API access at
  volume since 2023, but low-volume OAuth is free, and
  `old.reddit.com/r/<sub>/.json` still works unauthenticated at modest
  request rates. Useful for weekly "what's happening this weekend"
  megathreads specifically, not general crawling.
- **Nonsense NYC**: Newsletter, strong fit for the "weird/cool" framing
  of this project. No feed — start with manual curation, automate later
  (e.g. email-parsing) only if it proves worth it.
- **Skip Facebook Events and Instagram** — login-walled, not worth
  fighting.

## CORS note (why nothing here fetches from a browser)

None of these sources send CORS headers permitting arbitrary frontend JS
to fetch them. The fix isn't a CORS workaround (public proxies like
corsproxy.io are unreliable and rate-limited) — it's architectural: all
fetching happens server-side (a cron job, not a browser), and the
frontend, if one ever exists, only ever reads a pre-built JSON/ICS file
that was written to storage ahead of time. No live cross-origin calls at
request time, period.

## What's already built (v1, tested)

A working Python pipeline — see the uploaded `nyc-curator/` files. Layout:

```
nyc-curator/
  NORTH_STAR.md              read first — the product goal and the test for any addition
  SESSION_LOG.md              how this spec was arrived at; context, not instructions
  CODER_HANDOFF_PROMPT.md     this file
  schema.py                 canonical Event dataclass — every adapter normalizes into this
  neighborhoods.py          fixed NYC neighborhood list + best-effort text matcher
  pipeline.py                dedup, 14-day expiry, validate/quarantine, low-confidence
                             filtering, deterministic vibe scoring
  output.py                  writes events.json and a top-N-per-day-capped curated.ics
  main.py                    orchestrator
  config.example.yaml        copy to config.yaml — Meetup group ICS URLs, RSS feeds,
                             taste.love / taste.hate examples, Eventbrite URLs
  requirements.txt
  .github/workflows/fetch.yml   daily cron, GitHub Actions default failure email,
                                 no extra notification infra
  adapters/
    meetup_ics.py            fetches curated Meetup group ICS feeds; expands RRULE
                             recurrence via `recurring-ical-events` (RFC 5545) into
                             concrete instances within the lookahead window — the
                             single most likely silent bug in an ICS pipeline
                             otherwise (a naive parser drops or misdates "every
                             Tuesday" style recurring events)
    rss_llm.py                RSS + LLM extraction for prose sources (Skint/TimeOut).
                             Anchors every extraction to the RSS item's own pubDate
                             (America/New_York) so relative dates ("this Friday")
                             resolve correctly, and explicitly tells the model that
                             NYC nightlife runs past midnight so "11pm-3am" spans two
                             calendar days correctly. Takes love/hate examples as
                             few-shot input for a vibe_match (0-100) score. Uses
                             claude-haiku-4-5 (cheap, high-volume, low-complexity task).
    eventbrite_jsonld.py      best-effort only (see source landscape above). Parses
                             ld+json defensively — real pages show up as a single
                             object, an array, or wrapped in "@graph", with multiple
                             script tags where only one may be type "Event".
  README.md                   setup + design rationale + known gaps (below)
```

**Design principles baked in, not incidental:**
- Canonicalize first — every adapter output is a plain `Event`; nothing
  downstream knows or cares which source it came from.
- Structured sources (ICS, JSON-LD) run before LLM-extracted ones in
  `main.py`, and dedup lets the earlier/higher-quality source win on
  collision — LLM extraction is last resort, not first choice, for
  anything that already has structure.
- Uncertainty is visible: every event carries `date_confidence` and
  `extraction_status`; low-confidence dates are quarantined into a
  `needs_review` list rather than silently entering the calendar output.
- `pipeline.validate()` catches malformed events (missing title, naive/no
  timezone, end-before-start, implausible >18h duration) before scoring.
- Calendar output is capped at top-N events/day by score — uncapped
  output becomes noise nobody reads within a week.
- No database, no OAuth, no embeddings-based dedup (plain fuzzy match on
  normalized title+date+venue instead), no UI yet. This was a deliberate,
  repeated decision across the design discussion, not an oversight — add
  each only once there's evidence v1 needs it.

**Tested, not just written**: dependencies installed cleanly, all modules
compile, and a synthetic run through dedup → expire → validate → score →
write confirmed correct behavior — deduped a same title/date/venue
collision correctly preferring the higher-quality source, expired a past
event, quarantined an end-before-start event and a missing-title event,
and produced valid `events.json`/`curated.ics` output. One real bug was
caught and fixed in this process: `Event`'s `Optional[X]` fields needed
explicit `= None` defaults (a dataclass doesn't infer that from the type
hint alone) — every adapter would have crashed on construction without
the fix. This is already fixed in the uploaded files, but take it as a
signal to actually run this code against real network calls, not just
read it, before trusting it further.

## Known gaps — prioritized, do these next

1. **Idempotent re-processing keyed on content hash, not URL.**
   `state.json` currently records seen source URLs per run but doesn't
   skip re-extraction of unchanged articles — every run currently
   re-processes every RSS item in scope, burning LLM calls it doesn't
   need to. The fix should hash the article body (not just track the
   URL+timestamp), because Skint/TimeOut listicles get edited in place —
   same URL, new events over time — so a URL-or-timestamp-only ledger
   either re-extracts needlessly every day or misses real updates.
2. **Cold-start ranking.** For the first ~2 weeks there's no feedback
   data, so the scorer should rank primarily by explicit filters
   (neighborhood/category/price) rather than lean on `vibe_score` as if
   it already reflects real preference signal — treat `vibe_score` as a
   tiebreaker until a feedback loop exists (#4).
3. **Lightweight field-change tracking**, not full version history: when
   an event's venue/time/price changes between runs, store the previous
   value on the event itself (e.g. `previous_venue`, `changed_at`) so a
   future notification can say "venue changed" — full event-sourcing
   versioning is unnecessary scope for v1.
4. **A feedback/evaluation log.** No mechanism yet to record outcomes
   ("went, loved it" / "skipped, too touristy" / "bad extraction") against
   past recommendations. Worth adding once there are 1-2 weeks of real
   output to react to — this is what would let a future scoring change be
   judged against something other than intuition.
5. **Reddit and Bandsintown adapters** aren't wired into `main.py` yet.
   Reddit: read-only, low-volume, be gentle with `old.reddit.com/.json`,
   target weekend megathreads specifically. Bandsintown: only pays off
   with a maintained followed-artist list, per the corrected understanding
   above — don't build it as a citywide source.
6. **Partiful manual-intake form** not built — deferred by design (see
   source landscape).
7. **Unverified assumption worth testing, not assuming**: that Skint/
   TimeOut publish weekend-relevant content on a Wed–Thu rhythm, which
   would justify a heavier cron cadence Thu–Sun and lighter Mon–Wed
   instead of a flat daily schedule. Check this against actual post
   timestamps from their feeds before optimizing cron cadence around it.

## Two open questions only the user (not the coder) can resolve

Don't invent placeholder answers for these — ask, or leave them as
explicit TODOs:
- The real 3-love / 3-hate calibration examples for the few-shot
  extraction prompt (`config.yaml`'s `taste.love` / `taste.hate` —
  currently filled with generic placeholders so the pipeline runs out of
  the box, but they won't produce personalized output until replaced).
- Which output to prioritize first in practice: the `curated.ics`
  subscription, a delivered digest (email/chat), or holding off on any
  output UI until `events.json` output over a week or two looks good.

## Existing repos worth checking against (candidates, not verified fits)

I found these via search, not from memory — inspect them, don't assume
they're directly reusable:
- [judell/community-calendar](https://github.com/judell/community-calendar) —
  Jon Udell's curator-driven multi-source community events calendar.
  Different domain (general community calendars, not NYC nightlife/arts)
  but worth comparing its ingestion/curation philosophy against this
  project's, especially if it has already solved problems like source
  reliability tracking or curator review workflows.
- [Denperidge/facebook-event-aggregator](https://github.com/Denperidge/facebook-event-aggregator) —
  scrapes events, exports to a static site + `.ics` files, publishes via
  GitHub Pages automatically. Different source (Facebook pages) but
  nearly identical output pattern (ICS + static site + GH Actions) to
  what's built here — worth skimming its GitHub Actions workflow and ICS
  serialization approach.
- [allenporter/ical](https://github.com/allenporter/ical) — an
  alternative Python iCalendar/RFC 5545 library with recurring-event
  support, in case `recurring-ical-events` (currently used) proves
  insufficient for an edge case.

**Now check the uploaded gitingest of my own repos** for: any existing
event-scraping, RSS-parsing, or calendar code I've already written that
should be extended rather than duplicated; any existing personal-project
conventions (project structure, secrets handling, deploy target) this
should match; and anything in my history that suggests a stronger
preference among the open questions above than what's written here.

## Your task

1. Read `NORTH_STAR.md`, then `SESSION_LOG.md`, then this document, then
   the rest of the `nyc-curator/` files, in that order, before writing
   anything.
2. Read the uploaded gitingest export(s) in full and report what, if
   anything, is worth reusing, extending, or is duplicated by this new
   project — assess everything you're given, don't skim past it because
   it arrived in a different format than the rest of this package.
3. Implement gaps #1–#3 above (state ledger by content hash, cold-start
   ranking, lightweight field-change tracking) — these are well-specified
   enough to build without further input.
4. Flag gaps #4–#7 back to me rather than guessing at them.
5. Ask for the two open questions above rather than inventing answers.
6. Do not add a database, OAuth flow, embeddings-based dedup, or UI unless
   you find a concrete reason v1 as specified can't work without one —
   that was a deliberate, repeated decision, not an oversight.
7. For anything not covered by #3–#6 — a suggestion from the gitingest
   repos, a future diff, an idea that shows up later — run it through the
   `NORTH_STAR.md` test before adopting it: does it reduce regret, or
   does it just add discovery volume or infrastructure ahead of evidence
   it's needed? Note what you considered and didn't adopt, and why,
   rather than silently dropping it or silently merging it.
