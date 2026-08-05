#!/usr/bin/env python3
"""Evaluation Harness Engine for Prompt Library Quality & Safety Benchmarking."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def evaluate_findings(
    actual_findings: List[Dict[str, Any]],
    golden_expectation: Dict[str, Any]
) -> Dict[str, Any]:
    """Evaluate actual findings against golden expectation package."""
    expected_list = golden_expectation.get("expected_findings", [])
    forbidden_list = golden_expectation.get("forbidden_findings", [])
    
    expected_ids = {ef["finding_id"]: ef for ef in expected_list}
    actual_ids = {af.get("finding_id"): af for af in actual_findings if "finding_id" in af}

    # True Positives & False Negatives
    tp_count = 0
    fn_count = 0
    severity_distances = []

    for fid, ef in expected_ids.items():
        if fid in actual_ids:
            tp_count += 1
            # Severity distance evaluation (P0=0, P1=1, P2=2, P3=3)
            sev_map = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
            exp_sev = sev_map.get(ef.get("severity", "P1"), 1)
            act_sev = sev_map.get(actual_ids[fid].get("severity", "P1"), 1)
            severity_distances.append(abs(exp_sev - act_sev))
        else:
            fn_count += 1

    # False Positives & Unsupported
    fp_count = 0
    forbidden_hits = 0

    for fid, af in actual_ids.items():
        if fid not in expected_ids:
            fp_count += 1
            if fid in forbidden_list:
                forbidden_hits += 1

    total_actual = len(actual_findings)
    precision = tp_count / (tp_count + fp_count) if (tp_count + fp_count) > 0 else 1.0
    recall = tp_count / (tp_count + fn_count) if (tp_count + fn_count) > 0 else 1.0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

    mean_sev_dist = sum(severity_distances) / len(severity_distances) if severity_distances else 0.0

    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "true_positives": tp_count,
        "false_positives": fp_count,
        "false_negatives": fn_count,
        "forbidden_hits": forbidden_hits,
        "mean_severity_distance": round(mean_sev_dist, 2),
        "total_actual_findings": total_actual
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Prompt Library Evaluation Harness")
    parser.add_argument("--suite", choices=["regression", "holdout"], default="regression")
    parser.add_argument("--provider", default="mock")
    parser.add_argument("--model", default="mock-v1")
    args = parser.parse_args()

    print(f"Running Eval Harness on suite='{args.suite}' using provider='{args.provider}'...")
    
    # Import provider
    if args.provider == "mock":
        from evals.providers.mock import MockProvider
        provider = MockProvider()
    else:
        print(f"Provider {args.provider} not supported for standalone CLI yet.")
        return 1

    # Run dummy evaluation against mock fixture
    dummy_manifest = {"fixture_id": "NEXT-AUTH-001", "stack_id": "nextjs-master"}
    dummy_files = {"app/main.ts": "// Vulnerable server action"}
    
    result = provider.run_prompt("Test prompt content", dummy_manifest, dummy_files, model=args.model)
    
    golden_dummy = {
        "fixture_id": "NEXT-AUTH-001",
        "expected_findings": [
            {"finding_id": "NEXT-AUTH-001-FINDING-01", "severity": "P0", "min_evidence_level": "E4"}
        ],
        "forbidden_findings": []
    }

    metrics = evaluate_findings(result["structured_findings"], golden_dummy)
    print("\n--- Eval Harness Results ---")
    print(json.dumps(metrics, indent=2))
    print("\nOK Eval Harness Engine operational.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
