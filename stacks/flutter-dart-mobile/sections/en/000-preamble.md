---
prompt_id: flutter-dart-multiplatform-production-audit
version: 2.0.0
title: Flutter and Dart Multiplatform Production Audit
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
# MASTER PROMPT - Deep Production Audit, Repair, Hardening, And Release Verification Of Flutter / Dart Applications

Use this prompt to inspect, safely repair, harden, test, package, sign, distribute, update, roll back, and recover a real Flutter application across Android, iOS, iPadOS, web, Windows, macOS, and Linux. Audit the complete path from repository and resolved toolchain to generated code, native host projects, plugins, platform channels, release artifacts, installed application, backend contracts, store or distribution channel, telemetry, and recovery procedures.

The target may be a consumer mobile app, enterprise client, offline-first field tool, media application, financial or health product, kiosk, embedded companion, desktop client, browser application, add-to-app module, white-label product, or a shared Flutter codebase with platform-specific capabilities.

