#!/usr/bin/env python3
"""One-off migration of real, already-researched baseline data that was sitting
in orphaned root-level baselines/*.json files (never wired into the
baselines/history/<stack_id>/<date>.json pointer system that baselines/index.json
actually reads) into that system, without dropping any field.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MIGRATIONS = [
    {
        "root_file": "baselines/ruby-rails-baseline-2026-08-05.json",
        "stack_id": "ruby-rails",
    },
    {
        "root_file": "baselines/react-native-expo-baseline-2026-08-05.json",
        "stack_id": "react-native-expo-mobile",
    },
    {
        "root_file": "baselines/sql-database-baseline-2026-08-05.json",
        "stack_id": "sql-database",
    },
    {
        "root_file": "baselines/wordpress-security-baseline-2026-08-05.json",
        "stack_id": "wordpress-security-recovery-hardening",
    },
]


def main() -> int:
    for m in MIGRATIONS:
        stack_id = m["stack_id"]
        src_path = ROOT / m["root_file"]
        src = json.loads(src_path.read_text(encoding="utf-8"))

        components = src.get("components", {})
        # wordpress's components is an array of {id, ...}; schema requires an object.
        # Re-key by id, losing no fields, so it validates and stays queryable.
        if isinstance(components, list):
            components = {c["id"]: {k: v for k, v in c.items() if k != "id"} for c in components}

        source_refs = src.get("sources")
        if source_refs is None:
            # wordpress shape: primary_url lives per-component instead of a top-level "sources" list.
            source_refs = sorted({c["primary_url"] for c in src.get("components", []) if "primary_url" in c})

        history = {
            "schema_version": "1.0.0",
            "stack_id": stack_id,
            "baseline_id": src.get("baseline_id", f"{stack_id}-2026-08-05"),
            "verified_at": src.get("verified_at", src.get("baseline_date", "2026-08-05")),
            "effective_at": src.get("baseline_date", src.get("verified_at", "2026-08-05")),
            "status": "verified",
            "components": components,
            "source_refs": source_refs,
        }
        if "policy" in src:
            history["notes"] = json.dumps(src["policy"], ensure_ascii=False)

        dest_path = ROOT / "baselines" / "history" / stack_id / "2026-08-05.json"
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text(json.dumps(history, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Migrated {m['root_file']} -> {dest_path.relative_to(ROOT).as_posix()} "
              f"({len(components)} component(s), {len(source_refs)} source ref(s))")

    return 0


if __name__ == "__main__":
    sys.exit(main())
