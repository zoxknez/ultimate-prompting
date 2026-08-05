#!/usr/bin/env python3
"""Deterministic Prompt Composer & Composition Lock Manager."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK_FILE = ROOT / "COMPOSITION_LOCK.json"
STACKS_INDEX = ROOT / "stacks" / "index.json"


def read_file_content(rel_path: str) -> str:
    path = ROOT / rel_path
    if not path.exists():
        raise FileNotFoundError(f"Required component file missing: {rel_path}")
    return path.read_text(encoding="utf-8").strip()


def compute_file_sha256(rel_path: str) -> str:
    path = ROOT / rel_path
    if not path.exists():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def generate_composition_lock() -> dict:
    lock_data = {
        "schema_version": "1.0.0",
        "generator_version": "2.0.0",
        "template_engine": "stack_local_sections_concatenation",
        "encoding": "utf-8",
        "line_endings": "lf",
        "final_newline": True,
        "inputs": {}
    }
    
    # Excluded from lock: generated outputs, archive, eval results, lock itself
    EXCLUDED_NAMES = {
        "COMPOSITION_LOCK.json", "MANIFEST.sha256",
        "PROMPT_CATALOG.json", "RELEASE_FILES.json",
    }
    EXCLUDED_PREFIXES = ("archive/", "evals/results/", ".git/")

    # Collect all source component files (stacks, contracts, baselines, scripts)
    SOURCE_PREFIXES = ("stacks/", "contracts/", "baselines/", "scripts/")

    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        rel_p = p.relative_to(ROOT).as_posix()
        if p.name in EXCLUDED_NAMES:
            continue
        if any(rel_p.startswith(ep) for ep in EXCLUDED_PREFIXES):
            continue
        if not any(rel_p.startswith(sp) for sp in SOURCE_PREFIXES):
            continue
        lock_data["inputs"][rel_p] = f"sha256:{hashlib.sha256(p.read_bytes()).hexdigest()}"

    return lock_data


def compose_stack_local_sections(stack_config: dict, locale: str) -> str:
    """Concatenate byte-exact section chunks (+ optional core/contract modules) in manifest order.

    Section chunks are produced by scripts/decompose_master.py as exact substrings of the
    original v2.0.0 file, so concatenating them with no added separators reproduces the
    original file exactly when no core/contract modules are prepended yet (Phase 5 checkpoint).
    """
    parts = []
    for rel in stack_config.get("core_modules", {}).get(locale, []):
        parts.append(read_file_content(rel) + "\n\n")
    for rel in stack_config.get("contract_modules", {}).get(locale, []):
        parts.append(read_file_content(rel) + "\n\n")

    manifest_rel = stack_config["sections_manifest"][locale]
    manifest_path = ROOT / manifest_rel
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for entry in manifest["sections"]:
        # An entry is either a plain relative path (stack-local section) or
        # {"module": "<path>"} referencing a shared, deduplicated contract module.
        section_rel = entry["module"] if isinstance(entry, dict) else entry
        section_path = ROOT / section_rel
        parts.append(section_path.read_text(encoding="utf-8"))

    return "".join(parts)


def compose_prompt(stack_info: dict, locale: str) -> str:
    stack_id = stack_info["stack_id"]
    stack_json_path = ROOT / "stacks" / stack_id / "stack.json"

    if not stack_json_path.exists():
        raise FileNotFoundError(f"Stack '{stack_id}' has no stacks/{stack_id}/stack.json.")

    stack_config = json.loads(stack_json_path.read_text(encoding="utf-8"))
    if stack_config.get("composition_mode") != "stack-local-sections":
        raise ValueError(
            f"Stack '{stack_id}' has unsupported composition_mode "
            f"{stack_config.get('composition_mode')!r}; expected 'stack-local-sections'."
        )
    return compose_stack_local_sections(stack_config, locale)


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic Prompt Composer")
    parser.add_argument("--all", action="store_true", help="Compose all master prompts")
    parser.add_argument("--stack", type=str, help="Compose specific stack ID")
    parser.add_argument("--check", action="store_true", help="Check if master prompts match compiled outputs")
    parser.add_argument("--update-lock", action="store_true", help="Update COMPOSITION_LOCK.json")
    parser.add_argument("--check-lock", action="store_true", help="Verify COMPOSITION_LOCK.json")
    args = parser.parse_args()

    if args.update_lock:
        lock_data = generate_composition_lock()
        LOCK_FILE.write_text(json.dumps(lock_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Updated {LOCK_FILE}")
        return 0

    if args.check_lock:
        if not LOCK_FILE.exists():
            print(f"FAIL: {LOCK_FILE} missing.")
            return 1
        current_lock = generate_composition_lock()
        existing_lock = json.loads(LOCK_FILE.read_text(encoding="utf-8"))
        if current_lock["inputs"] != existing_lock.get("inputs", {}):
            print("FAIL: Composition lock inputs mismatch!")
            return 1
        print("OK Composition Lock verified.")
        return 0

    if not STACKS_INDEX.exists():
        print(f"FAIL: {STACKS_INDEX} missing.")
        return 1

    stacks_data = json.loads(STACKS_INDEX.read_text(encoding="utf-8"))["stacks"]

    if args.stack:
        stacks_data = [s for s in stacks_data if s["stack_id"] == args.stack]
        if not stacks_data:
            print(f"FAIL: Stack '{args.stack}' not found in registry.")
            return 1

    diff_count = 0
    for stack in stacks_data:
        for loc in stack["locales"]:
            target_filename = f"{stack['prompt_slug']}.{loc}.md"
            target_path = ROOT / target_filename
            compiled_content = compose_prompt(stack, loc)
            
            if args.check:
                if not target_path.exists():
                    print(f"FAIL: {target_filename} does not exist.")
                    diff_count += 1
                else:
                    existing_content = target_path.read_text(encoding="utf-8").replace("\r\n", "\n")
                    if existing_content != compiled_content:
                        print(f"FAIL: {target_filename} differs from compiled output.")
                        diff_count += 1
                    else:
                        print(f"OK   {target_filename} matches composer output.")
            else:
                target_path.write_text(compiled_content, encoding="utf-8", newline="\n")
                print(f"Wrote {target_filename} from composer output.")

    if args.check and diff_count > 0:
        print(f"\nComposer check failed with {diff_count} mismatch(es).")
        return 1

    print("Composer operation complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
