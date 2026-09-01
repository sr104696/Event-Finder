"""
RSS + LLM extraction adapter, for prose sources (The Skint, TimeOut, Nonsense
NYC once you're ready to automate it) that list events inside blog-post
paragraphs rather than structured fields.

The two failure modes this exists to avoid:
  1. Relative dates ("this Friday", "tomorrow night") resolving wrong
     because the model doesn't know what day the post was published --
     fixed by anchoring every extraction to the RSS item's own pubDate.
  2. Late-night events getting misdated because "Friday 11pm-3am" actually
     ends Saturday -- fixed by telling the model explicitly, in-prompt,
     that NYC nightlife runs past midnight.
"""
import json
from datetime import datetime
from zoneinfo import ZoneInfo

import feedparser
import anthropic

from schema import Event
from neighborhoods import normalize_neighborhood
from state import is_article_unchanged, record_article

NY_TZ = ZoneInfo("America/New_York")
SOURCE_QUALITY = 3  # structured on arrival, but the fields themselves are LLM-inferred

EXTRACTION_PROMPT_TEMPLATE = """You are extracting concrete, dated events from an NYC events blog post.

This post was published on {anchor_date} (America/New_York timezone). Use this
as your reference point for ALL relative dates ("this weekend", "Friday",
"tomorrow") -- do not guess a different anchor.

Important: NYC nightlife and shows commonly run past midnight. "Friday 11pm-3am"
means the event STARTS Friday night and ENDS early Saturday morning -- set
start_datetime and end_datetime accordingly, not both on the same calendar day.

Here is what you like (weight extraction/tagging toward these, don't force a
match where none exists):
{love_examples}

Here is what you'd skip even if free:
{hate_examples}

Article text:
---
{article_text}
---

Return a JSON array. Each element:
{{
  "title": string,
  "start_datetime": "YYYY-MM-DDTHH:MM:SS" (America/New_York local time, no offset),
  "end_datetime": "YYYY-MM-DDTHH:MM:SS" or null if unknown,
  "venue": string or null,
  "neighborhood": string or null,
  "price_tier": "free" | "$" | "$$" | "$$$" | null,
  "category_tags": array of short lowercase strings (e.g. "music", "art", "queer", "outdoors", "comedy", "market", "nightlife", "weird"),
  "editorial_blurb": one sentence, your own words, why this might be worth going to,
  "date_confidence": float 0-1 -- 1.0 if the date/time was explicit in the text,
      lower (e.g. 0.4) if you had to infer or guess any part of it,
  "vibe_match": float 0-100 -- how well this matches the "what I like" examples above,
      calibrated against the "what I'd skip" examples as the low end
}}

If the article contains no identifiable events, return an empty array []. Do not
invent events that aren't in the text.
"""


def build_prompt(article_text: str, anchor_date: datetime,
                  love_examples: list[str], hate_examples: list[str]) -> str:
    return EXTRACTION_PROMPT_TEMPLATE.format(
        anchor_date=anchor_date.astimezone(NY_TZ).strftime("%A, %B %d, %Y"),
        love_examples="\n".join(f"- {e}" for e in love_examples),
        hate_examples="\n".join(f"- {e}" for e in hate_examples),
        article_text=article_text[:6000],  # keep prompts cheap; most posts don't need more
    )


def extract_events_from_article(client: anthropic.Anthropic, source: str,
                                 title: str, link: str, summary: str,
                                 published: datetime,
                                 love_examples: list[str],
                                 hate_examples: list[str]) -> list[Event]:
    prompt = build_prompt(summary, published, love_examples, hate_examples)

    # Cheap model on purpose -- this is a high-volume, low-complexity
    # extraction task, not a reasoning task.
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text.strip()
    # models sometimes wrap JSON in ```json fences despite instructions -- strip defensively
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]

    try:
        items = json.loads(text)
    except Exception:
        try:
            import json_repair
            repaired = json_repair.repair_json(text)
            items = json.loads(repaired)
        except Exception as e:
            print(f"[rss_llm] could not parse extraction for {link!r} (even with json_repair): {e}")
            return []

    events = []
    for item in items:
        try:
            start = datetime.fromisoformat(item["start_datetime"]).replace(tzinfo=NY_TZ)
        except (KeyError, ValueError, TypeError):
            continue  # no usable date -- drop rather than guess

        end = None
        if item.get("end_datetime"):
            try:
                end = datetime.fromisoformat(item["end_datetime"]).replace(tzinfo=NY_TZ)
            except (ValueError, TypeError):
                end = None

        confidence = float(item.get("date_confidence", 0.5))
        events.append(Event(
            title=item.get("title", "Untitled")[:200],
            start_datetime=start,
            end_datetime=end,
            venue=item.get("venue"),
            neighborhood=normalize_neighborhood(item.get("neighborhood") or item.get("venue")),
            price_tier=item.get("price_tier"),
            category_tags=item.get("category_tags", []),
            editorial_blurb=item.get("editorial_blurb"),
            source=source,
            source_url=link,
            source_quality=SOURCE_QUALITY,
            date_confidence=confidence,
            # low-confidence dates get flagged for review rather than silently
            # entering the calendar -- see scoring.py / output filtering
            extraction_status="ok" if confidence >= 0.6 else "needs_review",
            llm_vibe_match=float(item["vibe_match"]) if item.get("vibe_match") is not None else None,
        ))

    return events


def fetch_all(feed_url: str, source_name: str, client: anthropic.Anthropic,
              love_examples: list[str], hate_examples: list[str],
              max_items: int = 15) -> list[Event]:
    parsed = feedparser.parse(feed_url)
    all_events: list[Event] = []

    for entry in parsed.entries[:max_items]:
        published = datetime(*entry.published_parsed[:6], tzinfo=NY_TZ) \
            if getattr(entry, "published_parsed", None) else datetime.now(NY_TZ)
        summary = getattr(entry, "summary", "") or getattr(entry, "description", "")
        link = getattr(entry, "link", "")

        # Gap 1: Content Hash State Ledger check
        if link and summary and is_article_unchanged(link, summary):
            print(f"[rss_llm] skipping unchanged article: {link!r}")
            continue

        try:
            events = extract_events_from_article(
                client, source_name, entry.title, link, summary,
                published, love_examples, hate_examples,
            )
            all_events.extend(events)
            if link and summary:
                record_article(link, summary)
        except Exception as e:  # noqa: BLE001
            print(f"[rss_llm] skipping {entry.link!r}: {e}")

    return all_events
