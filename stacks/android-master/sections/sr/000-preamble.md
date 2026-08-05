---
prompt_id: android-kotlin-compose-production-audit
version: 2.0.0
title: Production audit Android, Kotlin, Jetpack Compose i Android TV aplikacija
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

# MASTER PROMPT - Dubinski Production Audit Android, Kotlin i Jetpack Compose Aplikacija

Koristi ovaj prompt za audit, bezbednu popravku, verifikaciju i pripremu stvarne Android aplikacije za produkciju. Audituj kompletan delivery lanac, a ne samo Kotlin source kod ili uspesan debug build.

Ciljni projekat moze koristiti Jetpack Compose, Views, mesoviti UI, Kotlin, Java interoperabilnost, Coroutines i Flow, Hilt ili drugi DI framework, Room, DataStore, WorkManager, Navigation, OkHttp, Retrofit, Ktor, Media3, CameraX, Bluetooth, lokaciju, Firebase, Android TV, Wear OS, Automotive, native biblioteke, dynamic feature module, Play Feature Delivery ili enterprise i sideload distribuciju.

