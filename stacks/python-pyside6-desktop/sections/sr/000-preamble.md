---
prompt_id: python-pyside6-qt-desktop-production-audit
version: 2.0.0
title: Produkcioni audit Python, PySide6 i Qt desktop aplikacije
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

# MASTER PROMPT - Dubinski produkcioni audit, popravka, hardening, pakovanje, izdavanje i oporavak Python / PySide6 / Qt desktop aplikacija

Koristi ovaj prompt za pregled, bezbednu popravku, hardening, testiranje, pakovanje, potpisivanje, distribuciju, ažuriranje, rollback i oporavak stvarne desktop aplikacije izgrađene pomoću Python-a, PySide6, Qt for Python-a, Qt Widgets-a, Qt Quick/QML-a, Qt WebEngine-a, native ekstenzija ili mešovitog Python/native steka. Audit obuhvata ceo put od repozitorijuma i izbora interpretera do tačnog instaliranog executable-a, spakovanog Python i Qt runtime-a, native biblioteka, lokalnih podataka, integracije sa operativnim sistemom, update kanala, signing identiteta, telemetrije i procedure oporavka.

Cilj može biti Windows, macOS ili Linux proizvod; offline-first poslovni alat, media klijent, editor, downloader, launcher, tray utility, kiosk, hardware companion, naučna aplikacija, enterprise klijent, UI lokalnog agenta ili komercijalna desktop aplikacija sa automatskim ažuriranjem.

