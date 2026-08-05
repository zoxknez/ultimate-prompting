#!/usr/bin/env python3
"""Lossless decomposition of a v2.0.0 master prompt into stack-local sections.

Splits a master prompt file into byte-exact chunks at top-level ('## ') heading
boundaries, so that concatenating the chunks in order reproduces the original
file exactly. No text is reworded, trimmed, or reflowed. This is step 1 of the
Phase 5 pilot: prove lossless section-local composition before any shared
module (core/, contracts/) extraction is attempted.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADING_RE = re.compile(r"^## [^#].*$", re.MULTILINE)


def slugify(heading_text: str) -> str:
    text = heading_text.lstrip("#").strip()
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60] or "section"


def split_sections(source_text: str) -> list[tuple[str, str]]:
    """Return [(slug, exact_chunk_text), ...] such that concatenation == source_text."""
    matches = list(HEADING_RE.finditer(source_text))
    if not matches:
        raise ValueError("No top-level '## ' headings found; nothing to split.")

    chunks: list[tuple[str, str]] = []
    preamble = source_text[: matches[0].start()]
    chunks.append(("000-preamble", preamble))

    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(source_text)
        heading_line = m.group(0)
        chunks.append((slugify(heading_line), source_text[start:end]))

    return chunks


def main() -> int:
    parser = argparse.ArgumentParser(description="Lossless master-prompt section splitter")
    parser.add_argument("--source", required=True, help="Path to the master prompt file (relative to repo root)")
    parser.add_argument("--stack-id", required=True)
    parser.add_argument("--locale", required=True, choices=["en", "sr"])
    parser.add_argument("--verify-only", action="store_true", help="Split in-memory and verify losslessness without writing files")
    args = parser.parse_args()

    source_path = ROOT / args.source
    source_text = source_path.read_text(encoding="utf-8")

    chunks = split_sections(source_text)
    reconstructed = "".join(chunk for _, chunk in chunks)

    if reconstructed != source_text:
        print("FAIL: reconstructed text does not match source byte-for-byte.")
        return 1

    print(f"OK   Lossless split verified: {len(chunks)} sections, {len(source_text)} chars, exact reconstruction.")

    if args.verify_only:
        return 0

    out_dir = ROOT / "stacks" / args.stack_id / "sections" / args.locale
    out_dir.mkdir(parents=True, exist_ok=True)

    section_rel_paths = []
    width = len(str(len(chunks) * 10))
    for idx, (slug, chunk) in enumerate(chunks):
        if idx == 0:
            filename = "000-preamble.md"
        else:
            filename = f"{idx * 10:0{width}d}-{slug}.md"
        out_path = out_dir / filename
        out_path.write_text(chunk, encoding="utf-8", newline="\n")
        section_rel_paths.append((out_path.relative_to(ROOT)).as_posix())

    manifest_path = ROOT / "stacks" / args.stack_id / f"sections.{args.locale}.json"
    manifest_path.write_text(
        json.dumps({"stack_id": args.stack_id, "locale": args.locale, "sections": section_rel_paths}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(section_rel_paths)} section files to {out_dir}")
    print(f"Wrote manifest to {manifest_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
