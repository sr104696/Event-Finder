# Codex isolated rework

This folder is deliberately self-contained: it is a candidate rework and does
not overwrite the original pipeline. The additions retain a plain JSON file
rather than adding SQLite, a server, OAuth, or UI.

## Integration points

1. At RSS fetch time, load `state.json` with `load_state()` and call
   `article_is_unchanged(state, entry.link, summary)` **before** invoking the
   LLM. Skip only an identical content hash; the same URL is re-extracted when
   a publisher edits its article.
2. After a successful LLM extraction, call `record_article()`; do not record a
   failed extraction, so transient model/API failures can retry on the next run.
3. Before JSON/ICS output, call `apply_field_changes(events, state)` to attach
   `previous_values` and `changed_at` to changed events, then `save_state()`.
4. During the first two feedback-free weeks, call `score_cold_start()` with
   explicitly configured neighborhoods and categories. Its LLM score is only a
   fractional tiebreaker, so stated filters govern ordering.

The included tests exercise line-ending-stable content hashes, edited-content
reprocessing, change recording, state persistence, and cold-start ordering.
