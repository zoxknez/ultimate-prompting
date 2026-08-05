#!/usr/bin/env python3
"""Fail if prompts hardcode known-suspect invented patch patterns without re-check language."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Patterns that previously appeared as invented/unverified patches without soft language.
# If these appear WITHOUT nearby re-check wording, warn/fail.
SUSPECT = [
    (re.compile(r"24\.19\.0"), "Node patch — prefer line 24.x + re-check nodejs.org"),
    (re.compile(r"26\.6\.0"), "Node Current patch — re-check nodejs.org"),
    (re.compile(r"29\.7\.1"), "Docker patch — re-check docker release notes"),
    (re.compile(r"1\.36\.3"), "K8s patch — re-check kubernetes.io/releases"),
    (re.compile(r"\b4\.2\.3\b"), "Helm patch — re-check helm releases"),
    (re.compile(r"9\.7\.2"), "MySQL patch — only if official notes confirm"),
]

SOFT = re.compile(
    r"re-check|proveri|verify|nodejs\.org|dev\.mysql\.com|kubernetes\.io|docker\.com|helm/helm",
    re.I,
)


def main() -> int:
    failed = 0
    for path in sorted(ROOT.glob("*.md")):
        if path.name in {"CHANGELOG.md", "README.md"}:
            # README may still mention historical issues
            continue
        text = path.read_text(encoding="utf-8")
        for rx, msg in SUSPECT:
            for m in rx.finditer(text):
                start = max(0, m.start() - 120)
                end = min(len(text), m.end() + 120)
                window = text[start:end]
                if not SOFT.search(window):
                    print(f"FAIL {path.name}: {msg} near ...{window.strip()[:80]}...")
                    failed += 1
    if failed:
        print(f"\n{failed} hardcode risk(s)")
        return 1
    print("OK baseline hardcode scan")
    return 0


if __name__ == "__main__":
    sys.exit(main())
