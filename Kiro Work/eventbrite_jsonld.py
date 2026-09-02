"""
Eventbrite adapter: best-effort only, using extruct for JSON-LD extraction.

Eventbrite deprecated its public search API in Feb 2020. Event pages sit behind 
bot protection. This adapter does the polite thing: plain fetch, parse defensively 
with battle-tested extruct library, skip silently on failure.

Replaces hand-rolled regex + JSON parsing with extruct's JsonLdExtractor,
which handles:
- Single objects, arrays, or @graph wrappers
- Multiple script tags (only some are type "Event")
- Malformed JSON-LD structures that appear in the wild
"""
from datetime import datetime

import extruct
import requests

from neighborhoods import normalize_neighborhood
from schema import Event

SOURCE_QUALITY = 4
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; personal-events-curator/1.0)"
}


def parse_event_page(url: str) -> Event | None:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
    except requests.RequestException:
        return None

    if resp.status_code != 200:
        # includes bot-challenge responses -- skip, don't fight it
        return None

    # Extract all JSON-LD blocks using extruct
    try:
        data = extruct.extract(
            resp.text,
            base_url=url,
            syntaxes=['json-ld'],
            errors='ignore'  # don't crash on malformed JSON-LD
        )
    except Exception:  # noqa: BLE001 - intentionally broad, best-effort parsing
        return None
    
    json_ld_blocks = data.get('json-ld', [])
    
    # Find the Event block
    event_block = None
    for block in json_ld_blocks:
        block_type = block.get('@type', '')
        if isinstance(block_type, list):
            if 'Event' in block_type:
                event_block = block
                break
        elif block_type == 'Event':
            event_block = block
            break
    
    if not event_block:
        return None
    
    # Extract fields from Event schema.org JSON-LD
    try:
        start = datetime.fromisoformat(event_block["startDate"].replace("Z", "+00:00"))
    except (KeyError, ValueError):
        return None

    end = None
    if event_block.get("endDate"):
        try:
            end = datetime.fromisoformat(event_block["endDate"].replace("Z", "+00:00"))
        except ValueError:
            end = None

    location = event_block.get("location", {})
    venue = None
    address_text = ""
    
    if isinstance(location, dict):
        venue = location.get("name")
        address = location.get("address")
        if isinstance(address, dict):
            address_text = address.get("streetAddress", "")
        elif isinstance(address, str):
            address_text = address

    offers = event_block.get("offers")
    price_tier = None
    if isinstance(offers, dict) and offers.get("price") is not None:
        try:
            price = float(offers["price"]) if str(offers["price"]).replace(".", "", 1).isdigit() else None
            if price == 0:
                price_tier = "free"
            elif price is not None:
                price_tier = "$" if price < 25 else "$$" if price < 75 else "$$$"
        except (ValueError, TypeError):
            price_tier = None

    image = event_block.get("image")
    if isinstance(image, list):
        image = image[0] if image else None

    return Event(
        title=event_block.get("name", "Untitled")[:200],
        start_datetime=start,
        end_datetime=end,
        venue=venue,
        neighborhood=normalize_neighborhood(f"{venue or ''} {address_text or ''}"),
        price_tier=price_tier,
        category_tags=[],
        editorial_blurb=None,
        source="eventbrite",
        source_url=url,
        image_url=image if isinstance(image, str) else None,
        source_quality=SOURCE_QUALITY,
        date_confidence=1.0,  # structured JSON-LD, not an LLM guess
        extraction_status="ok",
    )


def fetch_all(event_urls: list[str]) -> list[Event]:
    """
    event_urls: individual Eventbrite event page URLs you've collected
    (e.g. from a category/location listing page you fetch separately).
    Failures are skipped silently -- see module docstring.
    """
    events = []
    for url in event_urls:
        event = parse_event_page(url)
        if event:
            events.append(event)
    return events
