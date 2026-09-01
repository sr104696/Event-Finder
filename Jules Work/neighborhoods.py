"""
Fixed NYC neighborhood list + a tiny nearest-match normalizer.

This is intentionally low-tech: a hardcoded list plus substring/alias
matching on venue/address text. Swap in real geocoding (NYC Open Data
neighborhood tabulation areas, or a geocoding API) later if this proves
too coarse -- but don't start there.
"""

NEIGHBORHOODS = [
    "Astoria", "Long Island City", "Greenpoint", "Williamsburg", "Bushwick",
    "Bed-Stuy", "Crown Heights", "Prospect Heights", "Park Slope",
    "Gowanus", "Red Hook", "Sunset Park", "Bay Ridge", "DUMBO",
    "Brooklyn Heights", "Fort Greene", "Clinton Hill", "East Williamsburg",
    "Ridgewood",
    "Lower East Side", "East Village", "Greenwich Village", "West Village",
    "SoHo", "NoHo", "Chinatown", "Tribeca", "Chelsea", "Flatiron",
    "Gramercy", "Midtown", "Hell's Kitchen", "Upper West Side",
    "Upper East Side", "Harlem", "Washington Heights", "Financial District",
    "Long Island City",
    "Mott Haven", "South Bronx",
    "Jackson Heights", "Flushing", "Sunnyside", "Forest Hills",
    "St. George", "Stapleton",
]

# alias -> canonical neighborhood, for common variants that show up in
# venue names / addresses (extend this as you see misses in practice)
ALIASES = {
    "bk": None,  # too ambiguous, leave unmapped rather than guess wrong
    "les": "Lower East Side",
    "wburg": "Williamsburg",
    "billyburg": "Williamsburg",
    "bed stuy": "Bed-Stuy",
    "hells kitchen": "Hell's Kitchen",
    "fidi": "Financial District",
    "uws": "Upper West Side",
    "ues": "Upper East Side",
    "dtbk": "Downtown Brooklyn",
}


def normalize_neighborhood(text: str | None) -> str | None:
    """Best-effort match of free text (venue name, address, LLM guess) to
    the fixed neighborhood list. Returns None rather than a wrong guess."""
    if not text:
        return None
    t = text.lower()

    for alias, canonical in ALIASES.items():
        if alias in t and canonical:
            return canonical

    for hood in NEIGHBORHOODS:
        if hood.lower() in t:
            return hood

    return None
