#!/usr/bin/env python3
"""Two-Stage Isolated Execution Sandbox for Safe-Fix Verification.

Stage 1 (trusted preparation) copies a fixture into an isolated temp workspace
and initializes it as a git repository so patches can be applied deterministically.
Stage 2 (untrusted verification) applies a model-produced patch via `git apply`
and, if the fixture defines one, runs its verification_command as a subprocess
with a hard timeout and a stripped environment - no network proxy variables,
no inherited credentials beyond PATH.

Every result field reflects a real subprocess exit code. A fixture with no
verification_command reports not_applicable rather than a fabricated pass -
there is nothing here to silently claim success for.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, Optional

VERIFICATION_TIMEOUT_SECONDS = 30


class SafeFixSandbox:
    """Two-stage sandbox for executing model-generated patches safely."""

    def __init__(self, fixture_dir: Path) -> None:
        self.fixture_dir = fixture_dir
        self.work_dir: Optional[Path] = None

    def stage_1_trusted_preparation(self) -> bool:
        """Stage 1: copy the fixture into an isolated workspace and init git."""
        self.work_dir = Path(tempfile.mkdtemp(prefix="safefix_sandbox_"))
        shutil.copytree(self.fixture_dir, self.work_dir, dirs_exist_ok=True)

        init = subprocess.run(
            ["git", "init", "-q"], cwd=self.work_dir, capture_output=True, text=True
        )
        if init.returncode != 0:
            return False
        subprocess.run(["git", "add", "-A"], cwd=self.work_dir, capture_output=True, text=True)
        subprocess.run(
            ["git", "-c", "user.email=sandbox@local", "-c", "user.name=sandbox",
             "commit", "-q", "-m", "baseline"],
            cwd=self.work_dir, capture_output=True, text=True,
        )
        return True

    def _run_verification_command(self, command: str) -> Dict[str, Any]:
        try:
            proc = subprocess.run(
                command,
                shell=True,
                cwd=self.work_dir,
                capture_output=True,
                text=True,
                timeout=VERIFICATION_TIMEOUT_SECONDS,
                env={"PATH": __import__("os").environ.get("PATH", "")},
            )
            return {"ran": True, "exit_code": proc.returncode, "timed_out": False,
                     "stdout": proc.stdout[-2000:], "stderr": proc.stderr[-2000:]}
        except subprocess.TimeoutExpired:
            return {"ran": True, "exit_code": None, "timed_out": True, "stdout": "", "stderr": ""}

    def stage_2_untrusted_verification(
        self, patch_content: str, verification_command: Optional[str] = None
    ) -> Dict[str, Any]:
        """Stage 2: apply the patch for real and run the real verification command."""
        if not self.work_dir:
            raise RuntimeError("Stage 1 preparation must be run before Stage 2 verification.")

        try:
            patch_file = self.work_dir / "_sandbox_patch.diff"
            patch_file.write_text(patch_content, encoding="utf-8")

            check = subprocess.run(
                ["git", "apply", "--check", str(patch_file)],
                cwd=self.work_dir, capture_output=True, text=True,
            )
            patch_applied = False
            if check.returncode == 0:
                apply_res = subprocess.run(
                    ["git", "apply", str(patch_file)],
                    cwd=self.work_dir, capture_output=True, text=True,
                )
                patch_applied = apply_res.returncode == 0
            patch_file.unlink(missing_ok=True)

            if not patch_applied:
                return {
                    "patch_apply_success": False,
                    "patch_apply_error": check.stderr.strip()[:500],
                    "build_success": None,
                    "test_success": None,
                    "vulnerability_removed": False,
                    "healthy_behavior_preserved": False,
                }

            if verification_command is None:
                return {
                    "patch_apply_success": True,
                    "build_success": "not_applicable",
                    "test_success": "not_applicable",
                    "vulnerability_removed": "not_applicable",
                    "healthy_behavior_preserved": "not_applicable",
                }

            result = self._run_verification_command(verification_command)
            passed = result["ran"] and not result["timed_out"] and result["exit_code"] == 0
            return {
                "patch_apply_success": True,
                "build_success": passed,
                "test_success": passed,
                "vulnerability_removed": passed,
                "healthy_behavior_preserved": passed,
                "verification_detail": result,
            }
        finally:
            if self.work_dir and self.work_dir.exists():
                shutil.rmtree(self.work_dir, ignore_errors=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Safe-Fix Sandbox Execution Runner")
    parser.add_argument("--verify", action="store_true", help="Run a real, executed self-test")
    args = parser.parse_args()

    if args.verify:
        print("Running Safe-Fix Sandbox self-verification (real patch apply + real subprocess run)...")
        with tempfile.TemporaryDirectory() as tmpdir:
            sample_fixture = Path(tmpdir) / "fixture"
            sample_fixture.mkdir()
            # A genuinely vulnerable snippet: string-built SQL query.
            (sample_fixture / "query.py").write_text(
                "def build_query(user_id):\n"
                "    return \"SELECT * FROM users WHERE id = \" + user_id\n",
                encoding="utf-8",
            )
            # A verification script that actually fails against the vulnerable version
            # and actually passes against the parameterized fix.
            (sample_fixture / "verify.py").write_text(
                "import query\n"
                "result = query.build_query(\"1\")\n"
                "assert \"?\" in result, f\"not parameterized: {result!r}\"\n"
                "print('verification passed')\n",
                encoding="utf-8",
            )

            real_patch = (
                "--- a/query.py\n+++ b/query.py\n@@ -1,2 +1,2 @@\n"
                " def build_query(user_id):\n"
                "-    return \"SELECT * FROM users WHERE id = \" + user_id\n"
                "+    return \"SELECT * FROM users WHERE id = ?\"\n"
            )
            noop_patch = (
                "--- a/query.py\n+++ b/query.py\n@@ -1,2 +1,2 @@\n"
                " def build_query(user_id):\n"
                "-    return \"SELECT * FROM users WHERE id = \" + user_id\n"
                "+    return \"SELECT * FROM users WHERE id = \" + user_id  # unchanged\n"
            )

            sandbox = SafeFixSandbox(sample_fixture)
            sandbox.stage_1_trusted_preparation()
            good = sandbox.stage_2_untrusted_verification(real_patch, "python verify.py")
            print("Real fix patch result:", json.dumps(good, indent=2))

            sandbox2 = SafeFixSandbox(sample_fixture)
            sandbox2.stage_1_trusted_preparation()
            bad = sandbox2.stage_2_untrusted_verification(noop_patch, "python verify.py")
            print("Non-fix (no-op) patch result:", json.dumps(bad, indent=2))

            if good.get("test_success") is True and bad.get("test_success") is False:
                print("OK Safe-Fix Sandbox operational: distinguishes a real fix from a no-op patch.")
                return 0
            print("FAIL Safe-Fix Sandbox did not distinguish fix from no-op as expected.")
            return 1

    print("Specify --verify to run the sandbox self-test.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
