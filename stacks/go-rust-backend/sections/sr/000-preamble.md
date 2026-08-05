---
prompt_id: go-rust-backend-systems-production-audit
version: 2.0.0
title: Go i Rust backend i systems production audit
language: sr
status: production-candidate
default_mode: AUDIT_AND_SAFE_FIX
baseline_date: 2026-08-05
requires:
  - core/audit-operating-contract.md
  - core/severity-model.md
  - core/final-report-schema.md
  - core/production-readiness-dod.md
---
# MASTER PROMPT - Dubinski production audit, popravka, hardening, provera izdanja i oporavak Go i Rust sistema

Koristi ovaj prompt za audit, bezbednu popravku, hardening, testiranje, build, pakovanje, deploy, rollback i oporavak stvarnog Go i/ili Rust backend-a, servisa, worker-a, CLI alata, daemon-a, proxy-ja, data-plane komponente, control-plane komponente, biblioteke, embedded sistema, WebAssembly modula ili mešovitog sistema.

Audit mora da obuhvati ceo put od repozitorijuma i razrešenog toolchain-a do generisanog koda, build tag-ova ili Cargo feature-a, linkovanih native biblioteka, immutable artefakata, deployment revizije, pokrenutog procesa, skladišta podataka, mrežnih peer-ova, telemetrije, incident kontrola i dokazanog oporavka. Kompilacija, Safe Rust, odsustvo panic-a, zelen race run ili uspešan health check nikada nisu sami po sebi dovoljni.

