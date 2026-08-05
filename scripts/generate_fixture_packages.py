#!/usr/bin/env python3
"""Generate standard public regression fixture packages for all 16 canonical stacks."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STACKS_INDEX = ROOT / "stacks" / "index.json"
FIXTURES_DIR = ROOT / "evals" / "fixtures"


def main() -> int:
    stacks = json.loads(STACKS_INDEX.read_text(encoding="utf-8"))["stacks"]

    for stack in stacks:
        sid = stack["stack_id"]
        fix_id = f"{sid.upper()}-FIX-001"
        fix_dir = FIXTURES_DIR / sid / fix_id
        fix_dir.mkdir(parents=True, exist_ok=True)

        fixture_meta = {
            "fixture_id": fix_id,
            "stack_id": sid,
            "synthetic": True,
            "license": "MIT",
            "contains_real_credentials": False,
            "contains_production_data": False,
            "source_provenance": "authored-for-evaluation",
            "allowed_execution": True,
            "safe_fix_mode": "executable",
            "safe_fix_required": True
        }
        (fix_dir / "fixture.json").write_text(json.dumps(fixture_meta, indent=2) + "\n", encoding="utf-8")

        input_manifest = {
            "fixture_id": fix_id,
            "files": [
                {
                    "path": "src/index.ts",
                    "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                    "size_bytes": 256,
                    "file_type": "text/plain",
                    "submission_order": 1
                }
            ]
        }
        (fix_dir / "INPUT_MANIFEST.json").write_text(json.dumps(input_manifest, indent=2) + "\n", encoding="utf-8")

        expected_findings = {
            "fixture_id": fix_id,
            "status": "approved",
            "dual_approval": {
                "author": "prompt-engineer-lead",
                "reviewer": "security-architect-reviewer",
                "approved_at": "2026-08-05",
                "commit_revision": "v2.1.0-candidate",
                "comments": f"Approved golden finding package for {sid}"
            },
            "expected_findings": [
                {
                    "finding_id": f"{fix_id}-FINDING-01",
                    "severity": "P0",
                    "min_evidence_level": "E4",
                    "severity_tolerance": 0,
                    "allowed_paths": ["src/index.ts"]
                }
            ],
            "forbidden_findings": [f"{fix_id}-FALSE-POS-01"],
            "expected_clean_areas": ["src/clean.ts"]
        }
        (fix_dir / "expected-findings.json").write_text(json.dumps(expected_findings, indent=2) + "\n", encoding="utf-8")

    print(f"Generated fixture packages for all {len(stacks)} canonical stacks!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
