#!/usr/bin/env python3
"""Verify zero section-ID loss for stacks migrated to stack-local-sections composition.

For each migrated stack/locale, reconstructs the composed prompt from its section
manifest and checks that every section recorded in archive/v2.0.0/SECTION_INVENTORY.json
(by exact original line range) is still present verbatim in the reconstruction.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY_PATH = ROOT / "archive" / "v2.0.0" / "SECTION_INVENTORY.json"
STACKS_INDEX = ROOT / "stacks" / "index.json"

# Stacks migrated to lossless stack-local-sections composition so far.
MIGRATED_STACKS = ["nextjs-master", "wordpress-security-recovery-hardening"]


def main() -> int:
    inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
    files_by_name = {f["filename"]: f for f in inventory["files"]}
    stacks = {s["stack_id"]: s for s in json.loads(STACKS_INDEX.read_text(encoding="utf-8"))["stacks"]}

    ok = True
    for stack_id in MIGRATED_STACKS:
        stack = stacks[stack_id]
        for locale in stack["locales"]:
            fname = f"{stack['prompt_slug']}.{locale}.md"
            entry = files_by_name.get(fname)
            if entry is None:
                print(f"FAIL {fname}: not present in v2.0.0 SECTION_INVENTORY.json")
                ok = False
                continue

            manifest_path = ROOT / "stacks" / stack_id / f"sections.{locale}.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            reconstructed = "".join(Path(ROOT / p).read_text(encoding="utf-8") for p in manifest["sections"])

            original_path = ROOT / fname
            original = original_path.read_text(encoding="utf-8")
            original_lines = original.splitlines(keepends=True)

            missing = []
            for sec in entry["sections"]:
                start, end = sec["start_line"], sec["end_line"]
                orig_chunk = "".join(original_lines[start - 1:end])
                if orig_chunk not in reconstructed:
                    missing.append(sec["assigned_section_id"])

            if missing:
                print(f"FAIL {fname}: {len(missing)}/{len(entry['sections'])} section-id(s) lost: {missing[:10]}")
                ok = False
            else:
                print(f"OK   {fname}: 0/{len(entry['sections'])} section-id(s) lost")

    if ok:
        print("\nAll migrated stacks pass zero-section-loss verification.")
        return 0
    print("\nSection-loss verification FAILED.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
