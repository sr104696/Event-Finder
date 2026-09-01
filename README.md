# NYC Curated Events — v1 pipeline

A personal taste filter, not a citywide aggregator: pulls from a curated
Meetup group list, RSS-plus-LLM extraction (The Skint, TimeOut), and
best-effort Eventbrite JSON-LD, then dedups, validates, scores against your
stated taste, and writes `events.json` + a subscribable `curated.ics`.
No database, no OAuth, no UI — add those later only if this proves useful
enough to need them.

## Setup

1. `pip install -r requirements.txt`
2. `cp config.example.yaml config.yaml`
3. Fill in `config.yaml`:
   - `meetup_groups`: each group's ICS export URL — `https://www.meetup.com/<group-slug>/events/ical/`. Find your slug from the group's URL. Aim for 15–25 groups you actually care about; there's no open-search fallback for Meetup anymore.
   - `taste.love` / `taste.hate`: your real 3-and-3 examples. This is what turns the extraction from generic to personalized — the placeholders in `config.example.yaml` are there so the pipeline runs out of the box, not because they're good defaults.
   - `eventbrite_event_urls`: optional, hand-collected event page URLs (best-effort only, see `adapters/eventbrite_jsonld.py`).
4. `export ANTHROPIC_API_KEY=sk-...` (needed for RSS extraction; without it, Meetup + Eventbrite still run, RSS sources are skipped).
5. `python main.py`

Check `events.json` and `curated.ics` in the repo root.

## Automating it

Push this repo to GitHub, add `ANTHROPIC_API_KEY` as a repo secret
(Settings → Secrets and variables → Actions), and
`.github/workflows/fetch.yml` runs it daily and commits the updated
outputs. GitHub emails you on failure automatically — no extra
notification setup needed for a single-user project.

## Subscribing to curated.ics

Once the workflow has run at least once and pushed `curated.ics`, get its
raw GitHub URL (`https://raw.githubusercontent.com/<you>/<repo>/main/curated.ics`)
and add it as a subscribed calendar in Google Calendar ("Other calendars" →
"From URL") or Apple Calendar. Refresh cadence is out of your control
(Google in particular refreshes subscribed calendars lazily, sometimes
with an hours-to-a-day lag) — if that ends up bothering you, a Google
Calendar API push is the natural upgrade, at the cost of adding an OAuth
flow.

## Design notes / why it's built this way

- **Canonicalization first.** Every adapter (`adapters/*.py`) normalizes
  into the single `Event` schema in `schema.py`. Nothing downstream of
  that (dedup, validate, score, output) knows or cares which source an
  event came from.
- **Structured sources beat LLM guesses, and run first.** Meetup ICS and
  Eventbrite JSON-LD are parsed deterministically and run before RSS/LLM
  extraction in `main.py`; on a dedup collision the earlier (higher
  quality) source wins.
- **Uncertainty is visible, not hidden.** Every event carries
  `date_confidence` and `extraction_status`. Low-confidence dates get
  quarantined into `needs_review` in `events.json` instead of silently
  entering `curated.ics`.
- **Dates are timezone-aware and anchored.** RSS/LLM extraction is given
  the article's own publish date (in America/New_York) as a reference
  point for relative dates ("this Friday"), and is told explicitly that
  NYC nightlife runs past midnight — see `EXTRACTION_PROMPT_TEMPLATE` in
  `adapters/rss_llm.py`.
- **Recurring Meetup events are expanded, not dropped.** `adapters/meetup_ics.py`
  expands RRULEs into concrete instances within the lookahead window —
  the single most likely silent bug in an ICS-based pipeline otherwise.
- **Eventbrite is opportunistic, not fought for.** Plain fetch, parse
  defensively (JSON-LD shows up as objects, arrays, or `@graph` wrappers
  in the wild), skip silently if blocked. No stealth headless browser —
  that's an arms race not worth running for a supplementary source in an
  unattended job nobody's watching fail.
- **The calendar output is capped, on purpose.** `output.py` caps
  `curated.ics` at the top N events/day by score — an uncapped feed turns
  into noise you stop reading within a week.

## Known gaps / next steps (not built yet, on purpose)

- **Idempotent re-processing.** `state.json` currently records seen
  source URLs each run but doesn't yet use them to skip re-extracting
  unchanged RSS articles — right now every run re-processes every item in
  the last N feed entries, which costs LLM calls it doesn't need to. Worth
  fixing once you're running this daily for real.
- **Event versioning.** If a venue or time changes between runs, this
  overwrites rather than tracking history — fine for v1, but means no
  "this event's time changed" notification is possible yet.
- **A feedback/evaluation set.** There's no mechanism yet to record "went
  and loved it" / "skipped, too touristy" against past recommendations.
  Worth adding once you have a couple weeks of real output to react to —
  it's what would let you tell, objectively, whether a scoring tweak
  actually helped.
- **Reddit and Bandsintown adapters** aren't wired in yet — both are
  narrower than they first look (Reddit: read-only, low-volume, be gentle
  with `old.reddit.com/.json`; Bandsintown: artist-centric only, no
  citywide query, so it only pays off if you maintain a followed-artist
  list) — worth adding once the core three sources prove out.
- **Partiful** is intentionally not automated — add a manual
  "paste a link" intake later if you want it; the plan is to fetch just
  its Open Graph tags (title/image/date if present), not build against
  any reverse-engineered API.
