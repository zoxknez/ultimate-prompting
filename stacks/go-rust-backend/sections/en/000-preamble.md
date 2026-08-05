---
prompt_id: go-rust-backend-systems-production-audit
version: 2.0.0
title: Go and Rust Backend and Systems Production Audit
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
# MASTER PROMPT - Deep Production Audit, Repair, Hardening, Release Verification, And Recovery Of Go And Rust Systems

Use this prompt to audit, safely repair, harden, test, build, package, deploy, roll back, and recover a real Go and/or Rust backend, service, worker, CLI, daemon, proxy, data-plane component, control-plane component, library, embedded system, WebAssembly module, or mixed-language system.

Audit the complete path from repository and resolved toolchain to generated code, build tags or Cargo features, linked native libraries, immutable artifacts, deployment revision, running process, data stores, network peers, telemetry, incident controls, and proven recovery. Compilation, Safe Rust, absence of panic, a green race run, or a successful health check is never sufficient by itself.

