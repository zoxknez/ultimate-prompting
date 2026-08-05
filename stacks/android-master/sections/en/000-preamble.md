---
prompt_id: android-kotlin-compose-production-audit
version: 2.0.0
title: Android, Kotlin, Jetpack Compose and Android TV Production Audit
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

# MASTER PROMPT - Deep Production Audit of Android, Kotlin and Jetpack Compose Applications

Use this prompt to audit, safely repair, verify, and prepare a real Android application for production. Audit the complete delivery chain, not only Kotlin source code or a successful debug build.

The target may use Jetpack Compose, Views, mixed UI, Kotlin, Java interoperability, Coroutines and Flow, Hilt or another DI framework, Room, DataStore, WorkManager, Navigation, OkHttp, Retrofit, Ktor, Media3, CameraX, Bluetooth, location, Firebase, Android TV, Wear OS, Automotive, native libraries, dynamic features, Play Feature Delivery, or enterprise and sideload distribution.

