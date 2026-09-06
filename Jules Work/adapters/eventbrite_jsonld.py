"""
Eventbrite adapter: best-effort only. Eventbrite deprecated its public
search API in Feb 2020, and its event pages sit behind bot protection that
a plain request sometimes trips. Rather than fight that with a stealth
headless browser (an arms race, over a supplementary source, that a
personal unattended cron job won't notice losing), this adapter does the
polite thing: plain fetch, parse defensively, skip silently on failure.

JSON-LD parsing is defensive on purpose: event pages in the wild show up as
a single object, an array of objects, or wrapped in an "@graph" list, and
a page can carry multiple <script type="application/ld+json"> tags where
only one is actually type "Event". Handle all three shapes rather than
assuming the first one.
"""
import json
import re
import requests
from datetime import datetime

from schema import Event
from neighborhoods import normalize_neighborhood

SOURCE_QUALITY = 4
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; personal-events-curator/1.0)"
}

LD_JSON_RE = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)


def _flatten_ld_blocks(html: str) -> list[dict]:
    """Pull every ld+json script tag out of the page using extruct (with regex fallback)
    and flatten arrays / @graph wrappers into a single list of plain dicts."""
    blocks = []
    try:
        import extruct
        extracted = extruct.extract(html, syntaxes=["json-ld"])
        json_ld_list = extracted.get("json-ld", [])
        for item in json_ld_list:
            if isinstance(item, list):
                blocks.extend(item)
            elif isinstance(item, dict) and "@graph" in item:
                blocks.extend(item["@graph"])
            elif isinstance(item, dict):
                blocks.append(item)
        if blocks:
            return blocks
    except Exception as err:
        print(f"[eventbrite_jsonld] extruct parsing fallback to regex: {err}")

    for raw in LD_JSON_RE.findall(html):
        try:
            parsed = json.loads(raw.strip())
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, list):
            blocks.extend(parsed)
        elif isinstance(parsed, dict) and "@graph" in parsed:
            blocks.extend(parsed["@graph"])
        elif isinstance(parsed, dict):
            blocks.append(parsed)
    return blocks


def _is_event_type(block: dict) -> bool:
    t = block.get("@type", "")
    if isinstance(t, list):
        return "Event" in t
    return t == "Event"


def parse_event_page(url: str) -> Event | None:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
    except requests.RequestException:
        return None

    if resp.status_code != 200:
        # includes bot-challenge responses -- skip, don't fight it
        return None

    for block in _flatten_ld_blocks(resp.text):
        if not _is_event_type(block):
            continue

        try:
            start = datetime.fromisoformat(block["startDate"].replace("Z", "+00:00"))
        except (KeyError, ValueError):
            continue

        end = None
        if block.get("endDate"):
            try:
                end = datetime.fromisoformat(block["endDate"].replace("Z", "+00:00"))
            except ValueError:
                end = None

        location = block.get("location", {})
        venue = location.get("name") if isinstance(location, dict) else None
        address = location.get("address") if isinstance(location, dict) else None
        address_text = address.get("streetAddress") if isinstance(address, dict) else str(address or "")

        offers = block.get("offers")
        price_tier = None
        if isinstance(offers, dict) and offers.get("price") is not None:
            price = float(offers["price"]) if str(offers["price"]).replace(".", "", 1).isdigit() else None
            if price == 0:
                price_tier = "free"
            elif price is not None:
                price_tier = "$" if price < 25 else "$$" if price < 75 else "$$$"

        image = block.get("image")
        if isinstance(image, list):
            image = image[0] if image else None

        return Event(
            title=block.get("name", "Untitled")[:200],
            start_datetime=start,
            end_datetime=end,
            venue=venue,
            neighborhood=normalize_neighborhood(f"{venue or ''} {address_text or ''}"),
            price_tier=price_tier,
            category_tags=[],
            editorial_blurb=None,
            source="eventbrite",
            source_url=url,
            image_url=image,
            source_quality=SOURCE_QUALITY,
            date_confidence=1.0,  # structured JSON-LD, not an LLM guess
            extraction_status="ok",
        )

    return None  # no Event block found -- page structure changed, or we got blocked


def fetch_all(event_urls: list[str]) -> list[Event]:
    """event_urls: individual Eventbrite event page URLs you've collected
    (e.g. from a category/location listing page you fetch separately).
    Failures are skipped silently -- see module docstring."""
    events = []
    for url in event_urls:
        event = parse_event_page(url)
        if event:
            events.append(event)
    return events
