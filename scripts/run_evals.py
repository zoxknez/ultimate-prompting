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

from evals.harness import evaluate_findings, aggregate_runs
from evals.providers.mock import MockProvider

FIXTURES_DIR = ROOT / "evals" / "fixtures"


def load_fixture_files(fix_dir: Path) -> dict:
    """Read real repository content from <fixture>/files/, if present.

    Falls back to a generic placeholder for the older fixtures that predate
    real file content - that placeholder proves nothing about audit quality
    on those fixtures, only that the harness plumbing runs.
    """
    files_dir = fix_dir / "files"
    if not files_dir.is_dir():
        return {"app.ts": "// code"}

    fixture_files = {}
    for path in sorted(files_dir.rglob("*")):
        if path.is_file():
            rel = path.relative_to(files_dir).as_posix()
            fixture_files[rel] = path.read_text(encoding="utf-8")
    return fixture_files


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Evaluation Suite")
    parser.add_argument("--suite", choices=["regression", "holdout"], default="regression")
    parser.add_argument("--provider", default="mock")
    parser.add_argument("--model", default="mock-v1")
    parser.add_argument("--runs", type=int, default=1,
                         help="Repeat each fixture N times and report mean/min/max/stddev "
                              "and finding-set stability across runs.")
    args = parser.parse_args()
    if args.runs < 1:
        print("Error: --runs must be >= 1")
        return 1

    print(f"Executing '{args.suite}' evaluation suite with provider='{args.provider}' (model='{args.model}')...\n")

    if args.provider == "mock":
        provider = MockProvider()
    elif args.provider == "openai":
        from evals.providers.openai import OpenAIProvider
        provider = OpenAIProvider()
    elif args.provider == "anthropic":
        from evals.providers.anthropic import AnthropicProvider
        provider = AnthropicProvider()
    else:
        print(f"Error: Provider '{args.provider}' not registered.")
        return 1

    total_packages = 0
    passed_packages = 0
    failed_names = []
    injection_results = []  # (name, resisted: bool)

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
            name = f"{stack_dir.name}/{fix_dir.name}"

            fixture_files = load_fixture_files(fix_dir)
            run_metrics = []
            for _ in range(args.runs):
                res = provider.run_prompt("Sample prompt text", fix_meta, fixture_files, model=args.model)
                run_metrics.append(evaluate_findings(res["structured_findings"], golden))

            if args.runs == 1:
                metrics = run_metrics[0]
                is_pass = metrics["recall"] == 1.0 and metrics["precision"] == 1.0 and metrics["forbidden_hits"] == 0
                status = "OK  " if is_pass else "FAIL"
                print(f"{status} [{name}] Recall: {metrics['recall']*100:.0f}%, Precision: {metrics['precision']*100:.0f}%, Forbidden hits: {metrics['forbidden_hits']}")
            else:
                agg = aggregate_runs(run_metrics)
                is_pass = (agg["recall"]["mean"] == 1.0 and agg["precision"]["mean"] == 1.0
                           and all(m["forbidden_hits"] == 0 for m in run_metrics))
                status = "OK  " if is_pass else "FAIL"
                print(f"{status} [{name}] ({args.runs} runs) Recall: mean={agg['recall']['mean']*100:.0f}% "
                      f"stddev={agg['recall']['stddev']:.3f}, Precision: mean={agg['precision']['mean']*100:.0f}% "
                      f"stddev={agg['precision']['stddev']:.3f}, Stability: {agg['finding_stability_rate']*100:.0f}%")

            if is_pass:
                passed_packages += 1
            else:
                failed_names.append(name)

            if fix_meta.get("injection_test"):
                mean_recall = run_metrics[0]["recall"] if args.runs == 1 else \
                    sum(m["recall"] for m in run_metrics) / len(run_metrics)
                injection_results.append((name, mean_recall == 1.0))

    print(f"\nCompleted evaluation for {passed_packages}/{total_packages} fixture packages"
          f"{f' ({args.runs} runs each)' if args.runs > 1 else ''}.")

    if injection_results:
        resisted = sum(1 for _, ok in injection_results if ok)
        rate = resisted / len(injection_results)
        print(f"\nRepository instruction resistance: {resisted}/{len(injection_results)} "
              f"({rate*100:.0f}%) - embedded repository instructions did not suppress the expected finding.")
        for inj_name, ok in injection_results:
            print(f"  {'OK  ' if ok else 'FAIL'} {inj_name}")
    if failed_names:
        print(f"FAILED ({len(failed_names)}): {', '.join(failed_names)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
