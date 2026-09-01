"""
Tests for json_repair integration in rss_llm.py
"""
import json
import json_repair


def test_json_repair_fallback():
    malformed_json = """
    [
      {
        "title": "Unclosed Quote & Trailing Comma Event",
        "start_datetime": "2026-09-15T19:00:00",
        "venue": "The Bell House",
        "vibe_match": 85,
      }
    ]
    """
    repaired = json_repair.repair_json(malformed_json)
    parsed = json.loads(repaired)
    assert isinstance(parsed, list)
    assert len(parsed) == 1
    assert parsed[0]["title"] == "Unclosed Quote & Trailing Comma Event"
