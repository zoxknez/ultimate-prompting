#!/usr/bin/env python3
"""Structural EN/SR parity checker for audit prompts (ignores fenced code)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADING = re.compile(r"^(#{1,3})\s+(.+)$")
FENCE = re.compile(r"^```")


def headings(path: Path) -> list[str]:
    out: list[str] = []
    in_fence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if FENCE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING.match(line.strip())
        if m:
            out.append(f"{m.group(1)} {m.group(2).strip()}")
    return out


def pairs() -> list[tuple[Path, Path]]:
    result = []
    for en in sorted(ROOT.glob("*.en.md")):
        sr = en.parent / (en.name[: -len(".en.md")] + ".sr.md")
        if sr.exists():
            result.append((en, sr))
        else:
            print(f"MISSING SR for {en.name}")
    return result


def main() -> int:
    failed = 0
    for en, sr in pairs():
        he, hs = headings(en), headings(sr)
        if len(he) != len(hs):
            print(f"FAIL {en.name}: EN headings={len(he)} SR headings={len(hs)}")
            failed += 1
            for i, (a, b) in enumerate(zip(he, hs)):
                if a.split()[0] != b.split()[0]:
                    print(f"  first level mismatch at {i}: {a!r} vs {b!r}")
                    break
            else:
                if len(he) > len(hs):
                    print(f"  EN extra from {len(hs)}: {he[len(hs) : len(hs) + 3]}")
                else:
                    print(f"  SR extra from {len(he)}: {hs[len(he) : len(he) + 3]}")
            continue
        bad = [
            (i, a, b)
            for i, (a, b) in enumerate(zip(he, hs))
            if a.split()[0] != b.split()[0]
        ]
        if bad:
            print(f"FAIL {en.name}: heading depth mismatch {bad[0]}")
            failed += 1
        else:
            print(f"OK   {en.name} ({len(he)} headings)")
    if failed:
        print(f"\n{failed} pair(s) failed structural parity")
        return 1
    print("\nAll pairs passed heading-count/depth parity")
    return 0


if __name__ == "__main__":
    sys.exit(main())
