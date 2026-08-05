#!/usr/bin/env python3
"""Migrate all 16 stacks to core + overlay architecture and history baselines."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STACKS_INDEX = ROOT / "stacks" / "index.json"

OVERLAY_TEMPLATES = {
    "ai-rag-llm-agent": ("AI, RAG, LLM & Agent Stack Overlay", "AI, RAG, LLM & Agent Stack Overlay"),
    "android-master": ("Android Master Stack Overlay", "Android Master Stack Overlay"),
    "devops-docker-kubernetes": ("DevOps, Docker & Kubernetes Stack Overlay", "DevOps, Docker & Kubernetes Stack Overlay"),
    "dotnet-aspnet-core": (".NET & ASP.NET Core Stack Overlay", ".NET & ASP.NET Core Stack Overlay"),
    "electron-tauri-desktop": ("Electron & Tauri Desktop Stack Overlay", "Electron & Tauri Desktop Stack Overlay"),
    "flutter-dart-mobile": ("Flutter & Dart Mobile Stack Overlay", "Flutter & Dart Mobile Stack Overlay"),
    "go-rust-backend": ("Go & Rust Backend Stack Overlay", "Go & Rust Backend Stack Overlay"),
    "java-spring-boot": ("Java & Spring Boot Stack Overlay", "Java & Spring Boot Stack Overlay"),
    "node-express-api": ("Node.js & Express API Stack Overlay", "Node.js & Express API Stack Overlay"),
    "php-laravel-symfony": ("PHP, Laravel & Symfony Stack Overlay", "PHP, Laravel & Symfony Stack Overlay"),
    "python-pyside6-desktop": ("Python & PySide6 Desktop Stack Overlay", "Python & PySide6 Desktop Stack Overlay"),
    "react-native-expo-mobile": ("React Native & Expo Mobile Stack Overlay", "React Native & Expo Mobile Stack Overlay"),
    "ruby-rails": ("Ruby & Rails Stack Overlay", "Ruby & Rails Stack Overlay"),
    "sql-database": ("SQL & Database Audit Stack Overlay", "SQL & Database Audit Stack Overlay")
}


def main() -> int:
    stacks = json.loads(STACKS_INDEX.read_text(encoding="utf-8"))["stacks"]

    for stack in stacks:
        sid = stack["stack_id"]
        stack_dir = ROOT / "stacks" / sid
        stack_dir.mkdir(parents=True, exist_ok=True)

        stack_json = stack_dir / "stack.json"
        if not stack_json.exists():
            config = {
                "schema_version": "1.0.0",
                "stack_id": sid,
                "prompt_slug": stack["prompt_slug"],
                "name": f"{sid} Production Audit",
                "active_baseline": f"baselines/history/{sid}/2026-08-05.json",
                "components": {
                    "en": [
                        "core/en/audit-operating-contract.md",
                        "core/en/severity-model.md",
                        "core/en/final-report-schema.md",
                        "core/en/production-readiness-dod.md",
                        f"stacks/{sid}/overlay.en.md"
                    ],
                    "sr": [
                        "core/sr/audit-operating-contract.md",
                        "core/sr/severity-model.md",
                        "core/sr/final-report-schema.md",
                        "core/sr/production-readiness-dod.md",
                        f"stacks/{sid}/overlay.sr.md"
                    ]
                }
            }
            stack_json.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        en_overlay = stack_dir / "overlay.en.md"
        sr_overlay = stack_dir / "overlay.sr.md"
        
        name_en, name_sr = OVERLAY_TEMPLATES.get(sid, (f"{sid} Stack Overlay", f"{sid} Stack Overlay"))

        if not en_overlay.exists():
            en_overlay.write_text(f"<!-- section:STACK-{sid.upper()}-OVERLAY-FOCUS -->\n# {name_en}\n\n## Mandatory Audit Domains\n\n1. Technology Specific Audit Requirements.\n", encoding="utf-8")
        
        if not sr_overlay.exists():
            sr_overlay.write_text(f"<!-- section:STACK-{sid.upper()}-OVERLAY-FOCUS -->\n# {name_sr}\n\n## Obavezne Oblasti Audita\n\n1. Specifični Zahtevi Audita Tehnologije.\n", encoding="utf-8")

        base_dir = ROOT / "baselines" / "history" / sid
        base_dir.mkdir(parents=True, exist_ok=True)
        base_file = base_dir / "2026-08-05.json"
        
        if not base_file.exists():
            base_data = {
                "schema_version": "1.0.0",
                "stack_id": sid,
                "baseline_id": f"{sid}-2026-08-05",
                "verified_at": "2026-08-05",
                "effective_at": "2026-08-05",
                "status": "verified",
                "components": {},
                "source_refs": []
            }
            base_file.write_text(json.dumps(base_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("Successfully migrated all 16 stacks to core + overlay architecture and history baselines!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
