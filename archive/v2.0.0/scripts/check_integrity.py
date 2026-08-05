#!/usr/bin/env python3
"""Repository-wide structural and metadata checks for active EN/SR prompt pairs."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"FAIL PyYAML unavailable: {exc}")
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
HEADING = re.compile(r"^(#{1,3})\s+(.+)$")
FENCE = re.compile(r"^```")
FORBIDDEN_SR = {"–": "en dash", "—": "em dash", "‑": "non-breaking hyphen"}


def split_frontmatter(text: str) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter")
    try:
        end = lines[1:].index("---") + 1
    except ValueError as exc:
        raise ValueError("unterminated YAML frontmatter") from exc
    data = yaml.safe_load("\n".join(lines[1:end])) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data, "\n".join(lines[end + 1 :])


def line_shape(line: str, in_fence: bool) -> str:
    s = line.strip()
    if FENCE.match(s):
        return "fence"
    if in_fence:
        return "code"
    if not s:
        return "blank"
    m = HEADING.match(s)
    if m:
        return f"h{len(m.group(1))}"
    if s.startswith("|---") or s.startswith("| ---"):
        return "table-separator"
    if s.startswith("|"):
        return "table-row"
    if re.match(r"^\d+\.\s", s):
        return "numbered"
    if s.startswith("- "):
        return "bullet"
    if s.startswith(">"):
        return "quote"
    return "paragraph"


def shapes(text: str) -> list[str]:
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        out.append(line_shape(line, in_fence))
        if FENCE.match(line.strip()):
            in_fence = not in_fence
    if in_fence:
        raise ValueError("unbalanced fenced code block")
    return out


def headings(text: str) -> list[str]:
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if FENCE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING.match(line.strip())
        if m:
            out.append(m.group(1))
    return out


def active_pairs() -> list[tuple[Path, Path]]:
    pairs: list[tuple[Path, Path]] = []
    for en in sorted(ROOT.glob("*.en.md")):
        sr = ROOT / en.name.replace(".en.md", ".sr.md")
        if not sr.exists():
            raise ValueError(f"missing Serbian pair for {en.name}")
        pairs.append((en, sr))
    return pairs


def main() -> int:
    failures: list[str] = []
    pairs = active_pairs()
    for en, sr in pairs:
        en_text = en.read_text(encoding="utf-8")
        sr_text = sr.read_text(encoding="utf-8")
        try:
            en_meta, en_body = split_frontmatter(en_text)
            sr_meta, sr_body = split_frontmatter(sr_text)
        except ValueError as exc:
            failures.append(f"{en.stem}: {exc}")
            continue

        en_version = en_meta.get("version", en_meta.get("prompt_version"))
        sr_version = sr_meta.get("version", sr_meta.get("prompt_version"))
        if en_version != sr_version:
            failures.append(f"{en.stem}: version mismatch {en_version!r} vs {sr_version!r}")
        if en_version != "2.0.0":
            failures.append(f"{en.stem}: expected version 2.0.0, got {en_version!r}")
        def declares(meta: dict, language: str) -> bool:
            single = str(meta.get("language", "")).lower()
            multi = [str(item).lower() for item in meta.get("languages", [])]
            accepted = {language.lower()}
            if language == "sr":
                accepted.update({"sr-latn", "sr_latn", "sr-latn-rs"})
            return single in accepted or any(item in accepted for item in multi)

        if not declares(en_meta, "en") or not declares(sr_meta, "sr"):
            failures.append(f"{en.stem}: invalid language metadata")

        en_lines = en_text.splitlines()
        sr_lines = sr_text.splitlines()
        if len(en_lines) != len(sr_lines):
            failures.append(f"{en.stem}: line count {len(en_lines)} vs {len(sr_lines)}")

        try:
            en_shapes = shapes(en_text)
            sr_shapes = shapes(sr_text)
        except ValueError as exc:
            failures.append(f"{en.stem}: {exc}")
            continue
        if en_shapes != sr_shapes:
            first = next((i for i, pair in enumerate(zip(en_shapes, sr_shapes), 1) if pair[0] != pair[1]), None)
            failures.append(f"{en.stem}: line-shape mismatch at line {first}")

        if headings(en_body) != headings(sr_body):
            failures.append(f"{en.stem}: heading-depth sequence mismatch")

        for char, name in FORBIDDEN_SR.items():
            count = sr_text.count(char)
            if count:
                failures.append(f"{sr.name}: contains {count} {name} character(s)")

        source_manifest = en_meta.get("source_manifest") or sr_meta.get("source_manifest")
        if source_manifest:
            source_path = ROOT / str(source_manifest)
            if not source_path.exists():
                failures.append(f"{en.stem}: missing source manifest {source_manifest}")
            elif source_path.suffix == ".json":
                try:
                    json.loads(source_path.read_text(encoding="utf-8"))
                except json.JSONDecodeError as exc:
                    failures.append(f"{en.stem}: invalid JSON source manifest: {exc}")

        print(f"OK   {en.stem[:-3]}: {len(en_lines)} lines, {len(headings(en_body))} headings")

    if len(pairs) != 16:
        failures.append(f"expected 16 active prompt pairs, found {len(pairs)}")

    if failures:
        print("\nFAILURES")
        for item in failures:
            print(f"- {item}")
        return 1

    print(f"\nAll {len(pairs)} active EN/SR pairs passed integrity checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
