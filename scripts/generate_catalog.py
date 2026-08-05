#!/usr/bin/env python3
"""Generate PROMPT_CATALOG.json and MANIFEST.sha256 for release."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADING_RX = re.compile(r"^(#{1,6})\s+(.+)$")


def compute_sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    catalog = {
        "version": "2.1.0",
        "generated_at": "2026-08-05",
        "active_pairs": 16,
        "active_files": 32,
        "prompts": {}
    }

    for path in sorted(ROOT.glob("*.md")):
        if path.name in {"README.md", "CHANGELOG.md", "CONTRIBUTING.md", "SECURITY.md", "VALIDATION_REPORT.md", "FINAL_LIBRARY_REVIEW.sr.md", "UPGRADE_PROGRESS.md"}:
            continue

        content = path.read_bytes()
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        headings = sum(1 for l in lines if HEADING_RX.match(l))

        catalog["prompts"][path.name] = {
            "version": "2.1.0",
            "lines": len(lines),
            "headings": headings,
            "bytes": len(content),
            "sha256": compute_sha256(content)
        }

    catalog_path = ROOT / "PROMPT_CATALOG.json"
    catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated {catalog_path.name}")

    # Generate MANIFEST.sha256 using RELEASE_FILES.json if available
    release_files_path = ROOT / "RELEASE_FILES.json"
    if release_files_path.exists():
        rel_files = json.loads(release_files_path.read_text(encoding="utf-8")).get("included_files", [])
        manifest_lines = []
        for rf in sorted(rel_files):
            fp = ROOT / rf
            if fp.is_file():
                sha = compute_sha256(fp.read_bytes())
                manifest_lines.append(f"{sha}  {rf}")
        
        manifest_path = ROOT / "MANIFEST.sha256"
        manifest_path.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
        print(f"Updated {manifest_path.name} with {len(manifest_lines)} release files.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
