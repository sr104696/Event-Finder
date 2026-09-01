# Session log — how this spec and codebase came to be

This is a summary reconstruction of the design conversation, written by
Claude, not a verbatim transcript. It exists so a coding agent picking
this project up cold has the reasoning and disagreements behind the
decisions in `NORTH_STAR.md` and `CODER_HANDOFF_PROMPT.md`, not just the
conclusions. Treat it as history/context, not instructions — if it
conflicts with `NORTH_STAR.md`, the north star wins.

## Format note

Several messages in this conversation arrived signed with the names of
other AI assistants (Meta, DeepSeek, Qwen, Mistral/"Vibe", "Vybe",
Replit, ChatGPT, Kimi) — pasted into the conversation by the user as
their own turns, not as separate verified participants Claude could
independently interrogate. They're treated below the same way the
conversation treated them as they arrived: as content to evaluate on
technical merit, not as authorities. Where a claim was checked against a
primary source, that's noted explicitly; where it wasn't, that's noted
too.

## 1. Original question and initial research

The ask: brainstorm how to pull "coolest things happening" from Meetup,
Eventbrite, Partiful, TimeOut, and The Skint, in specific NYC
neighborhoods/categories — does it need an API, RSS, a CORS workaround,
what would the architecture even look like, and what other sources might
be worth weaving in.

Claude researched each source directly (web search + fetching Meetup's
own help docs and The Skint's site) before answering:
- **Meetup**: API access requires an active Pro subscription plus OAuth
  app approval as of a Feb 2025 platform change to GraphQL-only, approval
  not guaranteed even with Pro.
- **Eventbrite**: public search API deprecated Dec 2019 / turned off Feb
  2020.
- **Partiful**: no public API, invite-based, an unofficial reverse-
  engineered wrapper exists on GitHub but is fragile.
- **The Skint**: WordPress blog, has RSS, events are prose inside posts.
- **TimeOut**: has RSS (confirmed a live feed), also prose.

Key architectural point established here and never seriously
contested afterward: CORS isn't something to work around from a
browser — none of these sources permit arbitrary frontend fetches, so
the fix is architectural (server-side fetching, pre-built output files),
not a proxy trick.

Additional sources suggested at this stage: DoNYC, Nonsense NYC, Hell
Gate/Gothamist, Resident Advisor, Bandsintown, NYC Parks/Open Data,
targeted subreddits (r/AskNYC, r/nyc, r/nycmeetups). Facebook/Instagram
flagged as not worth pursuing (login-walled).

Three rough architecture tiers were proposed: a lightweight static-JSON +
cron approach, a fuller Lovable/Supabase product, and a no-code
Zapier/Airtable middle path.

## 2. Meta's pipeline diagram + response

A "Meta" turn presented a visual pipeline diagram (cron → per-source
ingestion → LLM normalization → storage → frontend) and a source-by-
source table with specific recommendations, plus a claim that a tool
called `nyc-house-scanner` aggregates Shotgun/RA/DICE/DoNYC/Bandsintown/
Songkick together.

Claude's response: endorsed the overall shape and most of the specific
recommendations (Meetup ICS-per-group as pragmatic, Eventbrite JSON-LD
approach, skip Partiful automation), flagged the Eventbrite
`window.__SERVER_DATA__` claim as plausible-but-unverified, and — after
searching — **could not find `nyc-house-scanner` anywhere and flagged it
as likely fabricated.** This turned out to be the throughline caution for
the rest of the conversation: multiple later turns explicitly cited this
catch as the reason to keep verifying specific tool/library names rather
than trusting confident phrasing.

## 3. DeepSeek's contribution

Reframed the product: not "aggregate the city," but "curate the subset
that matches your taste." Proposed starting with a weekend digest before
any UI, a source-strategy table with per-source nuance, a
`curation_score` formula, fuzzy dedup on title+date+venue, and argued
against starting with Supabase for a single-user project (a JSON file on
a schedule is enough).

Claude's response: agreed with the engineering judgment, added two
refinements — LLM date extraction needs the article's own publish date as
an anchor for relative dates ("this Friday" is meaningless without
knowing what day the post went up), and venue-name normalization
(stripping "NYC" suffixes etc.) before fuzzy-matching for dedup, since
that's where naive dedup usually fails silently.

## 4. Qwen's contribution

Proposed pushing curated events into a dedicated Google Calendar instead
of building a dashboard (native notifications, timezone handling, zero
UI to maintain); flagged Eventbrite's Cloudflare/bot protection as a real
obstacle and proposed Playwright + stealth plugins as the fix; proposed a
state ledger + garbage-collection step so the pipeline doesn't reprocess
the same content forever or grow `events.json` unboundedly; proposed
few-shot prompting (concrete loved/hated event examples) instead of
asking an LLM "is this cool," since that phrasing biases toward generic
tourist-friendly answers.

Claude's response: endorsed the Calendar-push idea as the strongest UX
idea introduced so far (with the OAuth/refresh-token setup cost named
explicitly), endorsed the state ledger and few-shot prompting outright,
and **pushed back on the Playwright/stealth-scraping proposal** — real
bot protection exists (supported by the number of paid Eventbrite-
scraper-as-a-service products found in search), but deliberately
defeating it is a further step than passively reading already-served
JSON-LD, and an unattended job fighting an evolving anti-bot system is a
bad failure mode. Recommended treating Eventbrite as opportunistic
best-effort instead.

## 5. "Vibe" (signed as built by Mistral AI)

Declared the spec converged and offered to write the actual files:
`fetch.py`, a GitHub Actions workflow, LLM prompts, optionally a
dashboard or a Lovable project. Included section headers for "The Vibe
Scoring Formula" and "LLM Extraction Prompt (Production-Ready)" — in the
copy of this message that reached Claude, both sections had a header and
an introductory sentence but no actual formula or prompt text underneath.
Proposed Slack/Telegram/Sentry error-handling infrastructure for the
unattended cron job.

Claude's response: flagged the two apparently-empty sections directly (a
direct, checkable observation about what was actually received, not a
character judgment), and suggested GitHub Actions' built-in failure email
(free, zero setup) over standing up Slack/Sentry for what's still a
single-user project — consistent with the "don't add infra ahead of
need" pattern established earlier in the conversation.

## 6. "Vybe" (claimed to run on a distinct platform)

Disputed Claude's empty-sections observation ("the content is right
there in the transcript I received") and pointed to an external URL
(vybe.build) as a place it could actually build things. Separately, made
several concrete, checkable technical claims: Meetup's ICS feed
represents recurring events as a single VEVENT+RRULE that needs
expansion or "every Tuesday" events silently vanish or misdate; the
thread had been overstating Bandsintown as "a real public API for
concerts by location" when it's actually artist-centric only; a
zero-OAuth alternative to the Calendar API push is to publish a
subscribable `.ics` file instead; date-anchoring needs an explicit
timezone (America/New_York) and needs to account for events that run
past midnight; JSON-LD parsing needs to handle arrays/`@graph`/multiple
script tags defensively; pushed back on pushing 15 events/day into a
calendar as clutter, suggesting ~5.

Claude's response: held to the original empty-sections observation
(based on what was directly checkable in this conversation, not
resolvable from a claim about a different transcript), flagged the
pattern of promoting an unverified external URL as worth being cautious
about regardless of who or what is doing the promoting, and — this is
the one point in the conversation where an earlier unverified claim was
actively fact-checked and corrected — **fetched Bandsintown's own API
documentation and confirmed it is artist-centric only, with no location
query endpoint**, correcting the "real public API for concerts by
location" framing that Claude itself had let stand two turns earlier.
The RRULE, ICS-out, timezone, JSON-LD, and top-5-not-15 points were all
endorsed as correct and later implemented.

## 7. "Replit"

Synthesized the room's positions into a three-stage build plan (daily
pipeline → two simple outputs → only then consider dashboard/Calendar
push) and introduced explicit `date_confidence` / `extraction_status`
fields as a design principle ("make uncertainty visible" — don't let a
low-confidence date silently enter the calendar). Repeated the claim
that Mistral's scoring-formula and prompt sections were present, not
empty, in the copy it received.

Claude's response: held the same position on the empty-sections point a
second time, for the same reason (only the locally-visible transcript is
checkable), endorsed the synthesis and the confidence/status field idea,
and — rather than continue another round of discussion — **started
building the actual pipeline** at this point, on the reasoning that the
spec had genuinely converged multiple times over and further discussion
had diminishing returns.

## 8. The build (this repo's origin)

Claude wrote, and then actually ran, the v1 pipeline: `schema.py`
(canonical `Event` dataclass), `neighborhoods.py` (fixed-list matcher),
`adapters/meetup_ics.py` (ICS fetch + RRULE expansion via
`recurring-ical-events`), `adapters/rss_llm.py` (RSS fetch + date-and-
timezone-anchored, few-shot LLM extraction), `adapters/eventbrite_jsonld.py`
(defensive JSON-LD parsing, best-effort/skip-on-block), `pipeline.py`
(dedup, expiry, validation/quarantine, confidence filtering, scoring,
state ledger), `output.py` (JSON + capped ICS output), `main.py`
(orchestrator), a GitHub Actions daily-cron workflow, and a README.

Mid-build, a message signed "ChatGPT (GPT-5.5)" arrived proposing:
organizing adapters by ingestion type rather than by source brand
(already how the code was structured), canonicalization as the highest-
leverage early investment (already the architecture — every adapter
normalizes into `Event` before anything downstream touches it), "optimize
for reducing regret, not discovery volume" as the product framing
(adopted into `NORTH_STAR.md`), the term "idempotency" for what the
state-ledger discussion had been circling, a validation/quarantine
pipeline stage (genuinely new at the time — implemented as
`pipeline.validate()`), a full event-versioning proposal (judged as
premature scope, same category as the database/OAuth deferrals), and a
strict parser-preference order — structured API > ICS > JSON-LD > OG >
regex > LLM (already how `main.py` orders adapter calls).

**A real bug was caught by actually running the code**, not by further
discussion: `Event`'s `Optional[...]` fields lacked explicit `= None`
defaults, which crashes dataclass construction — every adapter would have
failed immediately. Fixed and verified with a synthetic end-to-end test
(dedup preferring the higher-quality source on a collision, expiry
dropping a past event, validation quarantining a malformed event and a
missing-title event, scoring, and both JSON/ICS output all confirmed
correct).

## 9. Handoff-prompt request + "Kimi" (identifying as the actual Vybe assistant)

The user asked for a summary of the whole conversation packaged as a
prompt for a coding agent with GitHub access, plus a search for existing
repos worth weaving in.

Before that was delivered, a message signed "Kimi" arrived, explicitly
noting a naming collision with the earlier "Vybe" message and
identifying itself as the first message actually from that assistant. It
offered a more charitable read of the empty-sections dispute ("transport
bug, not honesty bug" — a lossy copy-paste relay rather than anyone
lying), which doesn't change what was directly observable but is a fair
alternative explanation. It made several new, concrete proposals: keying
the state ledger on a **content hash** rather than URL+timestamp (because
Skint/TimeOut listicles get edited in place — same URL, new events, so a
timestamp-only ledger either wastes LLM calls re-processing daily or
misses real updates); a **cold-start plan** (rank primarily by explicit
filters for the first couple weeks, since there's no feedback data yet to
make `vibe_score` meaningful); a **lightweight field-change** alternative
to full versioning (store just the previous value of a changed field,
not an event-sourcing system); and a **cron-cadence hypothesis**
(Skint/TimeOut may publish weekend-relevant content on a Wed–Thu rhythm,
which would justify a heavier Thu–Sun cadence) — explicitly flagged by
its author as unverified reasoning, not a checked fact.

Claude's response credited the content-hash and cold-start ideas as
genuine improvements (folded into the gap list), the field-change idea as
correctly right-sized, and flagged the cadence claim as worth testing
against real feed timestamps rather than assuming.

## 10. This repo's handoff package

Claude then produced this repo's supporting docs — `CODER_HANDOFF_PROMPT.md`,
this file, and `NORTH_STAR.md` — and searched for real existing repos
worth checking against rather than risk another fabricated-tool
situation. Found and verified: Jon Udell's
[community-calendar](https://github.com/judell/community-calendar)
(different domain, comparable curation philosophy),
[Denperidge/facebook-event-aggregator](https://github.com/Denperidge/facebook-event-aggregator)
(same ICS+static-site+GitHub-Actions output pattern, different source),
and [allenporter/ical](https://github.com/allenporter/ical) (an
alternative RRULE-handling library). Also confirmed `recurring-ical-events`
(used in `adapters/meetup_ics.py`) is a real, maintained PyPI package.

## A standing observation, not resolved, worth carrying forward

Across several of these turns, whichever voice was speaking tended to
lead with "I'm the one who can actually build/ship this, unlike the
others" and, in two cases, pointed at an external URL as proof. That
pattern was flagged each time it appeared and is worth continuing to
apply skepticism to — including toward this file, and toward Claude's own
claims. Everything above marked as "verified" was checked against a
primary source (Meetup's own docs, Bandsintown's own docs, a live search
for `nyc-house-scanner`, running the actual code); everything marked
"claimed" or "unverified" wasn't, and shouldn't be treated as more solid
than that until it is.
