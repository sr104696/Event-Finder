# North star

Read this first. Read it again if a diff, an imported repo, or a new
idea seems to be pulling the project somewhere else. Everything else in
this repo — code, the session log, the handoff prompt, whatever gets
merged in from other repos — is subordinate to this page, not equal to it.

## The one-sentence goal

A personal taste filter that turns NYC's fragmented, largely API-less
events internet into a small number of things worth actually going to —
not a citywide events database, not a general aggregator, not a startup.

## The test for any proposed addition

**Does this reduce regret, or does it increase discovery volume?**
Regret reduction wins. A pipeline that surfaces 5 events you'd love beats
one that surfaces 400 you have to sift through. If a feature, source, or
architectural piece doesn't serve "on Sunday night, I didn't miss
anything I'd have loved," it's optional at best — and probably a later
phase, not now.

## Non-negotiables (survived repeated re-litigation, don't reopen without cause)

- **Curate, don't crawl.** Meetup groups, RSS sources, everything: a
  hand-picked list beats open-ended discovery. There is no citywide API
  waiting to be found for any of these sources — the curated list *is*
  the product, not a workaround until something better appears.
- **No database, no OAuth, no embeddings-based dedup, no UI** until v1's
  plain-file pipeline (`events.json` + `curated.ics`) proves it's worth
  the added complexity. Each of these was proposed and deferred multiple
  times in the design discussion for the same reason: don't build
  infrastructure ahead of evidence it's needed.
- **Structured sources beat LLM guesses, and run first.** ICS and JSON-LD
  parsing are deterministic and cheap; LLM extraction is for prose
  sources that have no structure to parse, not a default tool.
- **Uncertainty stays visible.** Low-confidence dates get quarantined,
  not silently published. A wrong event on the calendar is worse than a
  missing one.
- **No fighting bot protection.** Eventbrite and anything else behind
  real anti-bot defenses gets a plain fetch, parsed defensively, skipped
  silently if blocked. Not worth an arms race for a supplementary source.

## What "done" looks like for v1

`python main.py` (or the daily GitHub Action) produces a `curated.ics`
you'd actually subscribe to and an `events.json` you'd actually trust,
pulling from a curated Meetup list, Skint/TimeOut via anchored LLM
extraction, and best-effort Eventbrite — nothing more exotic than that.
Everything past that point (Reddit, Bandsintown, a dashboard, a Calendar
API push, an evaluation loop, versioning) is a *later* phase, contingent
on v1 actually being used.

## When other material gets merged in (other repos, diffs, new ideas)

This repo will likely grow to include a gitingest of other repos and
diffs proposing changes. Review all of it — don't ignore something just
because it arrived after this document did. But weigh every proposed
addition against the test above before merging it in. Material that adds
capability without serving the one-sentence goal belongs in a "considered,
not adopted" note, not in the pipeline.
