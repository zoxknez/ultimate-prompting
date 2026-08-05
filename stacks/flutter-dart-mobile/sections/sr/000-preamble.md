---
prompt_id: flutter-dart-multiplatform-production-audit
version: 2.0.0
title: Flutter i Dart multiplatform production audit
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
# MASTER PROMPT - Dubinski production audit, popravka, hardening i provera izdanja Flutter / Dart aplikacija

Koristi ovaj prompt za pregled, bezbednu popravku, hardening, testiranje, pakovanje, potpisivanje, distribuciju, ažuriranje, rollback i oporavak stvarne Flutter aplikacije na Android, iOS, iPadOS, web, Windows, macOS i Linux platformama. Audit mora da obuhvati ceo put od repozitorijuma i razrešenog toolchain-a do generisanog koda, native host projekata, plugin-a, platform channel-a, release artefakata, instalirane aplikacije, backend ugovora, store ili distributivnog kanala, telemetrije i procedura oporavka.

Cilj može biti potrošačka mobilna aplikacija, enterprise klijent, offline-first terenski alat, medijska aplikacija, finansijski ili zdravstveni proizvod, kiosk, prateća aplikacija za uređaj, desktop klijent, web aplikacija, add-to-app modul, white-label proizvod ili zajednički Flutter codebase sa platformskim funkcijama.

