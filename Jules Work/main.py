"""
Orchestrator: run all adapters, dedup, expire, score, and write outputs.

Run daily via GitHub Actions (see .github/workflows/fetch.yml). Locally:
    ANTHROPIC_API_KEY=sk-... python main.py
"""
import os
import sys
import yaml
import anthropic

from schema import Event
from adapters import meetup_ics, rss_llm, eventbrite_jsonld
from pipeline import dedup, expire, validate, filter_low_confidence, score
from state import load_seen_urls, save_seen_urls, track_field_changes
from output import write_json, write_ics


def load_config(path: str = "config.yaml") -> dict:
    if not os.path.exists(path):
        print(f"No {path} found -- copy config.example.yaml to {path} and fill it in.")
        sys.exit(1)
    with open(path) as f:
        return yaml.safe_load(f)


def main() -> None:
    config = load_config()
    lookahead_days = config.get("lookahead_days", 14)
    min_confidence = config.get("min_date_confidence", 0.6)

    all_events: list[Event] = []

    # Highest-trust source first: on a dedup collision, the earlier
    # occurrence wins, so structured sources should run before LLM-guessed ones.
    print("Fetching Meetup ICS feeds (with RRULE expansion)...")
    all_events.extend(meetup_ics.fetch_all(config.get("meetup_groups", []), lookahead_days))
    print(f"  -> {len(all_events)} events so far")

    if config.get("eventbrite_event_urls"):
        print("Fetching Eventbrite (best-effort JSON-LD)...")
        eb_events = eventbrite_jsonld.fetch_all(config["eventbrite_event_urls"])
        all_events.extend(eb_events)
        print(f"  -> +{len(eb_events)} (some may have been silently skipped -- see module docstring)")

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if config.get("rss_feeds") and api_key:
        client = anthropic.Anthropic(api_key=api_key)
        love = config.get("taste", {}).get("love", [])
        hate = config.get("taste", {}).get("hate", [])
        for feed in config["rss_feeds"]:
            print(f"Fetching + extracting {feed['name']}...")
            events = rss_llm.fetch_all(feed["url"], feed["name"], client, love, hate)
            all_events.extend(events)
            print(f"  -> +{len(events)} extracted")
    elif config.get("rss_feeds"):
        print("Skipping RSS/LLM extraction: set ANTHROPIC_API_KEY to enable it.")

    print(f"\nTotal before dedup/expiry: {len(all_events)}")
    all_events = dedup(all_events)
    print(f"After dedup: {len(all_events)}")
    all_events = expire(all_events, lookahead_days)
    print(f"After expiry window ({lookahead_days}d): {len(all_events)}")

    all_events, quarantined = validate(all_events)
    if quarantined:
        print(f"Quarantined {len(quarantined)} malformed events (see [validate] lines above)")

    publishable, needs_review = filter_low_confidence(all_events, min_confidence)
    print(f"Publishable: {len(publishable)} | needs review (low date confidence): {len(needs_review)}")

    preferred_neighborhoods = config.get("preferred_neighborhoods", ["Bushwick", "Williamsburg", "Greenpoint", "Lower East Side"])
    preferred_categories = config.get("preferred_categories", ["music", "art", "nightlife", "queer", "comedy"])
    publishable = score(publishable, preferred_neighborhoods=preferred_neighborhoods, preferred_categories=preferred_categories)

    # Gap 3: Field-change tracking
    publishable = track_field_changes(publishable)

    write_json(publishable, needs_review)
    write_ics(publishable)
    print("\nWrote events.json and curated.ics")

    # state ledger -- currently tracks seen source URLs so a future version
    # can skip re-processing unchanged articles; not yet used to short-circuit
    # extraction (see README "next steps"), just recorded each run.
    seen = load_seen_urls()
    seen.update(e.source_url for e in all_events if e.source_url)
    save_seen_urls(seen)


if __name__ == "__main__":
    main()
