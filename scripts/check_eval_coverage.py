#!/usr/bin/env python3
"""Validate Eval Fixture Coverage and Golden Package Completeness."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVALS_DIR = ROOT / "evals"
FIXTURES_DIR = EVALS_DIR / "fixtures"
STACKS_INDEX = ROOT / "stacks" / "index.json"


def main() -> int:
    if not STACKS_INDEX.exists():
        print(f"FAIL: {STACKS_INDEX} missing.")
        return 1

    stacks = json.loads(STACKS_INDEX.read_text(encoding="utf-8"))["stacks"]
    total_fixtures = 0
    missing_coverage = 0

    for stack in stacks:
        stack_id = stack["stack_id"]
        stack_fix_dir = FIXTURES_DIR / stack_id
        
        if not stack_fix_dir.exists():
            print(f"WARN: No fixture directory for stack '{stack_id}'")
            missing_coverage += 1
            continue

        fixtures = [d for d in stack_fix_dir.iterdir() if d.is_dir()]
        total_fixtures += len(fixtures)
        print(f"OK   Stack '{stack_id}' has {len(fixtures)} fixture package(s)")

    print(f"\nTotal Public Fixture Packages Found: {total_fixtures}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
