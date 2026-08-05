#!/usr/bin/env python3
"""Generate SECTION_INVENTORY.json for v2.0.0 prompt files before refactoring."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_DIR = ROOT / "archive" / "v2.0.0"

HEADING_RX = re.compile(r"^(#{1,6})\s+(.+)$")


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", text.upper())
    slug = re.sub(r"[-\s]+", "-", cleaned.strip())
    return slug[:60] or "UNTITLED"


def parse_sections_from_file(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    sections = []
    
    current_heading = "FRONTMATTER"
    current_level = 0
    current_start = 1
    current_lines: list[str] = []

    for idx, line in enumerate(lines, start=1):
        m = HEADING_RX.match(line)
        if m:
            if current_lines:
                content = "\n".join(current_lines)
                sec_id = f"SEC-{slugify(current_heading)}"
                sections.append({
                    "assigned_section_id": sec_id,
                    "heading": current_heading,
                    "level": current_level,
                    "start_line": current_start,
                    "end_line": idx - 1,
                    "line_count": len(current_lines),
                    "content_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
                })
            current_heading = m.group(2).strip()
            current_level = len(m.group(1))
            current_start = idx
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        content = "\n".join(current_lines)
        sec_id = f"SEC-{slugify(current_heading)}"
        sections.append({
            "assigned_section_id": sec_id,
            "heading": current_heading,
            "level": current_level,
            "start_line": current_start,
            "end_line": len(lines),
            "line_count": len(current_lines),
            "content_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
        })

    return sections


def main() -> int:
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    
    prompt_files = sorted(ROOT.glob("*.md"))
    inventory = {
        "schema_version": "1.0.0",
        "generated_at": "2026-08-05",
        "version": "2.0.0",
        "total_active_files": 0,
        "files": []
    }

    active_count = 0
    for path in prompt_files:
        if path.name in {"README.md", "CHANGELOG.md", "CONTRIBUTING.md", "SECURITY.md", "VALIDATION_REPORT.md", "FINAL_LIBRARY_REVIEW.sr.md", "UPGRADE_PROGRESS.md"}:
            continue
        
        active_count += 1
        sections = parse_sections_from_file(path)
        lang = "sr" if path.name.endswith(".sr.md") else "en"
        prompt_slug = path.name.replace(".en.md", "").replace(".sr.md", "")
        
        inventory["files"].append({
            "filename": path.name,
            "prompt_slug": prompt_slug,
            "locale": lang,
            "total_lines": sum(s["line_count"] for s in sections),
            "section_count": len(sections),
            "sections": sections
        })

    inventory["total_active_files"] = active_count
    
    output_path = ARCHIVE_DIR / "SECTION_INVENTORY.json"
    output_path.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated section inventory for {active_count} files at {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
