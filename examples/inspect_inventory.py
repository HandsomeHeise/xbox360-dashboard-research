"""Summarize the public resource inventory; no SDK or console access."""
from collections import Counter
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "data/resource-inventory.json").read_text(encoding="utf-8"))
dash = data["dashboard"]
guide = data["guide"]
assert len(dash["resources"]) == dash["total"] == 363
assert len(guide["resources"]) == guide["total"] == 72
assert Counter(item["status"] for item in dash["resources"]) == dash["status_counts"]
print("Dashboard resources:", dash["total"])
print("Guide resources:", guide["total"])
print("Dashboard status:", dict(Counter(item["status"] for item in dash["resources"])))
print("These are resource counts, not counts of user menus or hardware acceptance.")
