#!/usr/bin/env python3
"""Decoupled Release Validator for Prompt Library Releases."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_check_script(script_name: str, args: list[str] | None = None) -> bool:
    cmd = [sys.executable, str(ROOT / "scripts" / script_name)] + (args or [])
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"OK   {script_name} {' '.join(args or [])}")
        return True
    else:
        print(f"FAIL {script_name} {' '.join(args or [])}\n{res.stdout}\n{res.stderr}")
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Prompt Library Release Validator")
    parser.add_argument("--static", action="store_true", help="Run static integrity, parity, baseline, and lock checks")
    parser.add_argument("--evidence", type=str, help="Path to evaluation evidence directory")
    args = parser.parse_args()

    if not args.static and not args.evidence:
        print("Error: Specify --static, --evidence <dir>, or both.")
        return 1

    success = True

    if args.static:
        print("--- Running Static Release Gate Checks ---")
        success &= run_check_script("check_integrity.py")
        success &= run_check_script("check_parity.py")
        success &= run_check_script("check_baselines.py")
        success &= run_check_script("compose.py", ["--check-lock"])
        # Phase 5 pilot stacks are migrated to lossless stack-local-sections composition
        # and must stay byte-equivalent to their v2.0.0 reference. The remaining 14 stacks
        # are still pending Phase 6/7 migration and are intentionally not gated here yet.
        success &= run_check_script("compose.py", ["--stack", "nextjs-master", "--check"])
        success &= run_check_script("compose.py", ["--stack", "wordpress-security-recovery-hardening", "--check"])
        success &= run_check_script("check_section_loss.py")
        success &= run_check_script("check_eval_coverage.py")
        success &= run_check_script("run_evals.py", ["--suite", "regression", "--provider", "mock"])

    if args.evidence:
        evidence_dir = Path(args.evidence)
        print(f"--- Verifying Release Evidence at {evidence_dir} ---")
        if not evidence_dir.exists():
            print(f"WARN: Evidence directory {evidence_dir} does not exist yet.")
        else:
            print(f"OK   Evidence directory found at {evidence_dir}")

    if success:
        print("\nRELEASE GATE VERIFICATION PASSED")
        return 0
    else:
        print("\nRELEASE GATE VERIFICATION FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(main())
