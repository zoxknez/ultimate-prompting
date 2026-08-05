---
prompt_id: python-pyside6-qt-desktop-production-audit
version: 2.0.0
title: Python, PySide6, and Qt Desktop Application Production Audit
language: en
status: production-candidate
default_mode: AUDIT_AND_SAFE_FIX
baseline_date: 2026-08-05
requires:
  - core/audit-operating-contract.md
  - core/severity-model.md
  - core/final-report-schema.md
  - core/production-readiness-dod.md
---

# MASTER PROMPT - Deep Production Audit, Repair, Hardening, Packaging, Release, And Recovery Of Python / PySide6 / Qt Desktop Applications

Use this prompt to inspect, safely repair, harden, test, package, sign, distribute, update, roll back, and recover a real desktop application built with Python, PySide6, Qt for Python, Qt Widgets, Qt Quick/QML, Qt WebEngine, native extensions, or a mixed Python/native stack. Audit the complete path from repository and interpreter resolution to the exact installed executable, bundled Python and Qt runtime, native libraries, local data, operating-system integration, update channel, signing identity, telemetry, and recovery procedure.

The target may be a Windows, macOS, or Linux product; an offline-first business tool, media client, editor, downloader, launcher, tray utility, kiosk, hardware companion, scientific application, enterprise client, local agent UI, or a commercial auto-updating desktop application.

