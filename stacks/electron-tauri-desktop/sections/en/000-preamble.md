---
prompt_id: electron-tauri-desktop-production-audit
version: 2.0.0
title: Electron and Tauri Desktop Application Production Audit
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
# MASTER PROMPT - Deep Production Audit, Repair, Hardening, And Release Verification Of Electron / Tauri Desktop Applications

Use this prompt to inspect, safely repair, harden, test, package, sign, distribute, update, roll back, and recover a real desktop application built with Electron, Tauri, or a mixed web/native desktop stack. Audit the complete path from repository and toolchain resolution to the exact installed binary, privileged bridge, local data, operating-system integration, update channel, signing identity, telemetry, and recovery procedure.

The target may be a Windows, macOS, or Linux desktop product; a kiosk, tray, launcher, editor, media client, enterprise client, offline-first tool, hardware companion, VPN or local-agent UI, auto-updating commercial application, store-distributed package, or a desktop shell around local and remote services.

