#!/usr/bin/env python3
"""Check external URL accessibility in baselines/sources.json for nightly / release runs."""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES_FILE = ROOT / "baselines" / "sources.json"


def main() -> int:
    if not SOURCES_FILE.exists():
        print(f"FAIL: {SOURCES_FILE} missing.")
        return 1

    sources_data = json.loads(SOURCES_FILE.read_text(encoding="utf-8"))
    components = sources_data.get("components", [])

    print(f"Checking {len(components)} primary source URLs from {SOURCES_FILE.name}...")
    checked = 0
    failed = 0

    for comp in components:
        url = comp.get("primary_url")
        if not url:
            continue
        checked += 1
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (PromptLibraryBot/2.1.0)"})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status in (200, 301, 302):
                    print(f"OK   [{response.status}] {url}")
                else:
                    print(f"WARN [{response.status}] {url}")
        except Exception as err:
            print(f"FAIL {url} -> {err}")
            failed += 1

    print(f"\nSource link check completed: {checked} checked, {failed} failed.")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
