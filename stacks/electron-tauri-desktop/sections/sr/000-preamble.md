---
prompt_id: electron-tauri-desktop-production-audit
version: 2.0.0
title: Produkcioni audit Electron i Tauri desktop aplikacija
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
# MASTER PROMPT - Dubinski produkcioni audit, popravka, ojacavanje i verifikacija izdanja Electron / Tauri desktop aplikacija

Koristi ovaj prompt za pregled, bezbednu popravku, ojacavanje, testiranje, pakovanje, potpisivanje, distribuciju, azuriranje, rollback i oporavak stvarne desktop aplikacije izgradjene pomocu Electron-a, Tauri-ja ili mesovitog web/native desktop stack-a. Audit mora da obuhvati ceo put od repozitorijuma i razresavanja toolchain-a do tacno instaliranog binarnog fajla, privilegovanog mosta, lokalnih podataka, integracije sa operativnim sistemom, update kanala, signing identiteta, telemetrije i procedure oporavka.

Cilj moze biti Windows, macOS ili Linux desktop proizvod, kiosk, tray aplikacija, launcher, editor, media klijent, enterprise klijent, offline-first alat, prateca aplikacija za hardver, VPN ili UI lokalnog agenta, komercijalna aplikacija sa automatskim azuriranjem, paket iz prodavnice ili desktop omotac oko lokalnih i udaljenih servisa.

