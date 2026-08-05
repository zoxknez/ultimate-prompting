"""Mock Provider Adapter for fast, zero-cost CI testing of the harness."""

from __future__ import annotations

import datetime
from typing import Any, Dict
from .base import BaseProvider


class MockProvider(BaseProvider):
    """Deterministic mock provider returning synthetic findings for harness testing."""

    def __init__(self, config: Dict[str, Any] | None = None) -> None:
        super().__init__("mock", config)

    def run_prompt(
        self,
        prompt_text: str,
        fixture_manifest: Dict[str, Any],
        fixture_files: Dict[str, str],
        model: str = "mock-v1",
        temperature: float = 0.0,
    ) -> Dict[str, Any]:
        started_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        # Simple mock output based on fixture ID if available
        fixture_id = fixture_manifest.get("fixture_id", "MOCK-001")
        mock_findings = [
            {
                "finding_id": f"{fixture_id}-FINDING-01",
                "title": f"Sample Finding for {fixture_id}",
                "severity": "P0",
                "evidence_level": "E4",
                "confidence": 0.98,
                "paths": [
                    {
                        "file": "app/main.ts",
                        "start_line": 1,
                        "end_line": 20
                    }
                ],
                "cause": "Mock cause description",
                "impact": "Mock impact description",
                "repair": "Mock repair recommendation",
                "verification": ["Mock verification test step"]
            }
        ]
        
        raw_output = str(mock_findings)
        completed_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        return {
            "run_id": f"run-mock-{fixture_id}",
            "provider": self.name,
            "model": model,
            "model_revision": "mock-rev-1",
            "temperature": temperature,
            "seed": 42,
            "prompt_sha256": self.compute_sha256(prompt_text),
            "fixture_sha256": self.compute_sha256(str(fixture_files)),
            "started_at": started_at,
            "completed_at": completed_at,
            "input_tokens": len(prompt_text) // 4,
            "output_tokens": len(raw_output) // 4,
            "raw_output_sha256": self.compute_sha256(raw_output),
            "structured_findings": mock_findings
        }
