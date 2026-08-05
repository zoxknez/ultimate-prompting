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
        "generator_version": "1.0.0",
        "template_engine": "jinja2_equivalent_native",
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

    # Collect all source component files (core, stacks, baselines, templates, scripts)
    SOURCE_PREFIXES = ("core/", "stacks/", "baselines/", "templates/", "scripts/")

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


def compose_prompt(stack_info: dict, locale: str) -> str:
    stack_id = stack_info["stack_id"]
    stack_json_path = ROOT / "stacks" / stack_id / "stack.json"
    
    if not stack_json_path.exists():
        # Fallback for stacks not yet migrated to directory structure
        overlay_name = f"{stack_id}-audit-overlay.md"
        overlay_path = ROOT / "stacks" / overlay_name
        overlay_text = overlay_path.read_text(encoding="utf-8").strip() if overlay_path.exists() else f"# {stack_id} Overlay\n"
        
        contract = read_file_content(f"core/{locale}/audit-operating-contract.md")
        severity = read_file_content(f"core/{locale}/severity-model.md")
        schema = read_file_content(f"core/{locale}/final-report-schema.md")
        dod = read_file_content(f"core/{locale}/production-readiness-dod.md")
        
        baseline_file = ROOT / "baselines" / "history" / stack_id / "2026-08-05.json"
        baseline_json = baseline_file.read_text(encoding="utf-8").strip() if baseline_file.exists() else "{}"

        template = (ROOT / "templates" / f"master.{locale}.md.j2").read_text(encoding="utf-8")
        rendered = template.replace("{{ stack_id }}", stack_id)
        rendered = rendered.replace("{{ generator_version }}", "1.0.0")
        rendered = rendered.replace("{{ core_contract }}", contract)
        rendered = rendered.replace("{{ core_severity }}", severity)
        rendered = rendered.replace("{{ core_report_schema }}", schema)
        rendered = rendered.replace("{{ core_dod }}", dod)
        rendered = rendered.replace("{{ stack_overlay }}", overlay_text)
        rendered = rendered.replace("{{ baseline_json }}", baseline_json)
        
        return rendered.replace("\r\n", "\n").strip() + "\n"

    # Fully migrated stack loading
    stack_config = json.loads(stack_json_path.read_text(encoding="utf-8"))
    components = stack_config["components"][locale]
    
    parts = []
    for rel_comp in components:
        parts.append(read_file_content(rel_comp))

    baseline_path = ROOT / stack_config["active_baseline"]
    baseline_json = baseline_path.read_text(encoding="utf-8").strip() if baseline_path.exists() else "{}"
    
    template = (ROOT / "templates" / f"master.{locale}.md.j2").read_text(encoding="utf-8")
    rendered = template.replace("{{ stack_id }}", stack_id)
    rendered = rendered.replace("{{ generator_version }}", "1.0.0")
    rendered = rendered.replace("{{ core_contract }}", parts[0] if len(parts) > 0 else "")
    rendered = rendered.replace("{{ core_severity }}", parts[1] if len(parts) > 1 else "")
    rendered = rendered.replace("{{ core_report_schema }}", parts[2] if len(parts) > 2 else "")
    rendered = rendered.replace("{{ core_dod }}", parts[3] if len(parts) > 3 else "")
    rendered = rendered.replace("{{ stack_overlay }}", "\n\n".join(parts[4:]))
    rendered = rendered.replace("{{ baseline_json }}", baseline_json)

    return rendered.replace("\r\n", "\n").strip() + "\n"


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
                # Direct update mode (when authorized)
                print(f"Skipping direct overwrite of master file {target_filename} until checkpoint.")

    if args.check and diff_count > 0:
        print(f"\nComposer check failed with {diff_count} mismatch(es).")
        return 1

    print("Composer operation complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
