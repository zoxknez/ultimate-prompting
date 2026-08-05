#!/usr/bin/env python3
"""One-off, verified extraction of the finding-status vocabulary block shared
verbatim by ai-rag-llm-agent and android-master (EN + SR), into a real shared
contract module under contracts/evidence/.

This only touches the two stacks where the block was proven byte-identical
(see the session's diff analysis). No other stack is modified. Every step is
verified: the module text must be byte-identical across both stacks/locales
before extraction, and part_a + module + part_b must reconstruct the original
section file exactly.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EN_START = "2. Use one evidence status for every material claim:"
EN_END_LINE = "4. For commands not run, state `UNVERIFIED - not run because [specific reason]`.\n"
SR_START = "2. Za svaku materijalnu tvrdnju koristi jedan evidence status:"
SR_END_LINE = "4. Za komande koje nisu pokrenute napisi `UNVERIFIED - not run because [specific reason]`.\n"

TARGETS = [
    {
        "stack_id": "ai-rag-llm-agent",
        "locale": "en",
        "section_file": "020-1-non-negotiable-operating-contract.md",
        "continued_file": "021-1-non-negotiable-operating-contract-continued.md",
        "start_marker": EN_START,
        "end_line": EN_END_LINE,
    },
    {
        "stack_id": "ai-rag-llm-agent",
        "locale": "sr",
        "section_file": "020-1-obavezujuci-operativni-ugovor.md",
        "continued_file": "021-1-obavezujuci-operativni-ugovor-continued.md",
        "start_marker": SR_START,
        "end_line": SR_END_LINE,
    },
    {
        "stack_id": "android-master",
        "locale": "en",
        "section_file": "020-1-non-negotiable-operating-contract.md",
        "continued_file": "021-1-non-negotiable-operating-contract-continued.md",
        "start_marker": EN_START,
        "end_line": EN_END_LINE,
    },
    {
        "stack_id": "android-master",
        "locale": "sr",
        "section_file": "020-1-obavezujuci-operativni-ugovor.md",
        "continued_file": "021-1-obavezujuci-operativni-ugovor-continued.md",
        "start_marker": SR_START,
        "end_line": SR_END_LINE,
    },
]

MODULE_PATH = {
    "en": "contracts/evidence/finding-status-vocabulary-standard.en.md",
    "sr": "contracts/evidence/finding-status-vocabulary-standard.sr.md",
}


def split_file(path: Path, start_marker: str, end_line: str) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8")
    start = text.index(start_marker)
    end_marker_pos = text.index(end_line, start)
    end = end_marker_pos + len(end_line)
    return text[:start], text[start:end], text[end:]


def main() -> int:
    module_blocks = {"en": None, "sr": None}
    splits = {}

    # Pass 1: split + verify reconstruction + verify cross-stack byte-identical module block
    for t in TARGETS:
        sec_path = ROOT / "stacks" / t["stack_id"] / "sections" / t["locale"] / t["section_file"]
        part_a, module_block, part_b = split_file(sec_path, t["start_marker"], t["end_line"])
        original = sec_path.read_text(encoding="utf-8")
        if part_a + module_block + part_b != original:
            print(f"FAIL reconstruction mismatch: {sec_path}")
            return 1

        loc = t["locale"]
        if module_blocks[loc] is None:
            module_blocks[loc] = module_block
        elif module_blocks[loc] != module_block:
            print(f"FAIL module block not byte-identical for locale {loc} at {sec_path}")
            return 1

        splits[(t["stack_id"], loc)] = (part_a, part_b, t)

    # Pass 2: write the shared module files
    for loc, block in module_blocks.items():
        module_path = ROOT / MODULE_PATH[loc]
        module_path.parent.mkdir(parents=True, exist_ok=True)
        module_path.write_text(block, encoding="utf-8", newline="\n")
        print(f"Wrote shared module {module_path.relative_to(ROOT).as_posix()} ({len(block)} chars)")

    # Pass 3: rewrite the section files (part_a stays under original name, part_b becomes a new file)
    # and patch each stack's sections manifest to splice in the module reference.
    for (stack_id, loc), (part_a, part_b, t) in splits.items():
        sec_dir = ROOT / "stacks" / stack_id / "sections" / loc
        (sec_dir / t["section_file"]).write_text(part_a, encoding="utf-8", newline="\n")
        (sec_dir / t["continued_file"]).write_text(part_b, encoding="utf-8", newline="\n")

        manifest_path = ROOT / "stacks" / stack_id / f"sections.{loc}.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        old_rel = f"stacks/{stack_id}/sections/{loc}/{t['section_file']}"
        idx = manifest["sections"].index(old_rel)
        manifest["sections"][idx:idx + 1] = [
            old_rel,
            {"module": MODULE_PATH[loc]},
            f"stacks/{stack_id}/sections/{loc}/{t['continued_file']}",
        ]
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(f"Patched manifest {manifest_path.relative_to(ROOT).as_posix()}")

    print("\nOK Extraction complete for ai-rag-llm-agent and android-master (en+sr).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
