"""Base Provider Adapter for Prompt Library Evaluation Harness."""

from __future__ import annotations

import abc
import hashlib
from typing import Any, Dict


class BaseProvider(abc.ABC):
    """Abstract base class for LLM evaluation providers."""

    def __init__(self, name: str, config: Dict[str, Any] | None = None) -> None:
        self.name = name
        self.config = config or {}

    @abc.abstractmethod
    def run_prompt(
        self,
        prompt_text: str,
        fixture_manifest: Dict[str, Any],
        fixture_files: Dict[str, str],
        model: str,
        temperature: float = 0.0,
    ) -> Dict[str, Any]:
        """Execute a prompt against a fixture and return standardized result dict."""
        pass

    def compute_sha256(self, content: str) -> str:
        return hashlib.sha256(content.encode("utf-8")).hexdigest()
