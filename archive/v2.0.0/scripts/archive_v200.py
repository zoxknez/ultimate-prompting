#!/usr/bin/env python3
"""Archive v2.0.0 artifacts into archive/v2.0.0/ and compute SHA-256 manifest."""

from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_DIR = ROOT / "archive" / "v2.0.0"


def copy_file_or_dir(src: Path, dst: Path) -> None:
    if src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    elif src.is_file():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def generate_archive_manifest() -> None:
    manifest_entries = []
    for file_path in sorted(ARCHIVE_DIR.rglob("*")):
        if file_path.is_file() and file_path.name != "MANIFEST.sha256":
            rel_path = file_path.relative_to(ARCHIVE_DIR).as_posix()
            content = file_path.read_bytes()
            sha256 = hashlib.sha256(content).hexdigest()
            manifest_entries.append(f"{sha256}  {rel_path}")

    manifest_path = ARCHIVE_DIR / "MANIFEST.sha256"
    manifest_path.write_text("\n".join(manifest_entries) + "\n", encoding="utf-8")
    print(f"Generated {manifest_path} with {len(manifest_entries)} entries.")


def main() -> int:
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Copy 32 prompt files
    for p in ROOT.glob("*.md"):
        if p.name in {"README.md", "CHANGELOG.md", "CONTRIBUTING.md", "SECURITY.md", "VALIDATION_REPORT.md", "FINAL_LIBRARY_REVIEW.sr.md", "UPGRADE_PROGRESS.md"}:
            continue
        copy_file_or_dir(p, ARCHIVE_DIR / p.name)

    # 2. Copy catalog, manifest, validation report
    for name in ["PROMPT_CATALOG.json", "MANIFEST.sha256", "VALIDATION_REPORT.md"]:
        src = ROOT / name
        if src.exists():
            copy_file_or_dir(src, ARCHIVE_DIR / name)

    # 3. Copy baselines, core, scripts directories
    for dname in ["baselines", "core", "scripts"]:
        src = ROOT / dname
        if src.exists():
            copy_file_or_dir(src, ARCHIVE_DIR / dname)

    # 4. Generate SHA manifest for archive
    generate_archive_manifest()
    print("Archive v2.0.0 freeze complete!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
