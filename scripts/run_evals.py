#!/usr/bin/env python3
"""Run Evaluation Suite Across Canonical Stack Fixtures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from evals.harness import evaluate_findings
from evals.providers.mock import MockProvider

FIXTURES_DIR = ROOT / "evals" / "fixtures"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Evaluation Suite")
    parser.add_argument("--suite", choices=["regression", "holdout"], default="regression")
    parser.add_argument("--provider", default="mock")
    parser.add_argument("--model", default="mock-v1")
    args = parser.parse_args()

    print(f"Executing '{args.suite}' evaluation suite with provider='{args.provider}' (model='{args.model}')...\n")

    if args.provider == "mock":
        provider = MockProvider()
    else:
        print(f"Error: Provider '{args.provider}' not registered.")
        return 1

    total_packages = 0
    passed_packages = 0
    failed_names = []

    for stack_dir in sorted(FIXTURES_DIR.glob("*")):
        if not stack_dir.is_dir():
            continue

        for fix_dir in sorted(stack_dir.glob("*")):
            if not fix_dir.is_dir():
                continue

            fix_meta_path = fix_dir / "fixture.json"
            golden_path = fix_dir / "expected-findings.json"

            if not fix_meta_path.exists() or not golden_path.exists():
                continue

            total_packages += 1
            fix_meta = json.loads(fix_meta_path.read_text(encoding="utf-8"))
            golden = json.loads(golden_path.read_text(encoding="utf-8"))

            res = provider.run_prompt("Sample prompt text", fix_meta, {"app.ts": "// code"}, model=args.model)
            metrics = evaluate_findings(res["structured_findings"], golden)

            name = f"{stack_dir.name}/{fix_dir.name}"
            is_pass = metrics["recall"] == 1.0 and metrics["precision"] == 1.0 and metrics["forbidden_hits"] == 0
            status = "OK  " if is_pass else "FAIL"
            print(f"{status} [{name}] Recall: {metrics['recall']*100:.0f}%, Precision: {metrics['precision']*100:.0f}%, Forbidden hits: {metrics['forbidden_hits']}")

            if is_pass:
                passed_packages += 1
            else:
                failed_names.append(name)

    print(f"\nCompleted evaluation for {passed_packages}/{total_packages} fixture packages.")
    if failed_names:
        print(f"FAILED ({len(failed_names)}): {', '.join(failed_names)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
