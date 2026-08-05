## Faza 24 - Observability, testovi, CI/CD, rollout i recovery

Dokazi user impact, release identitet, uzrocne putanje, delivery trust, rollout bezbednost, rollback limite i stvarni recovery.

### Zahtevi audita

- Emituj strukturirane logove i trace-ove sa release-om, deployment-om, rutom, runtime-om, request/trace ID-jevima, ishodom, trajanjem i bezbednom error klasom.
- Definisi SLI, SLO, error budget, burn alert-e, owner-a, eskalaciju, runbook i recovery potvrdu.
- Redact-uj cookie-je, token-e, tajne, PII, payment podatke, upload-e, query stringove, stack local-e i source map-e.
- Koristi unit, component, integration, contract, production-artifact, browser, security, load, accessibility, migration i recovery testove prema riziku.
- Izoluj untrusted CI, pin-uj trusted alate, izgradi jednom, napravi digest/SBOM/provenance, testiraj artefakt i promovisi bez rebuild-a.
- Definisi canary, cohort, guardrail-e, abort autoritet, old/new kompatibilnost, rollback, forward repair, restore, RPO, RTO i incident switch-eve.

### Obavezni dokazi

- Telemetry schema, redaction testovi, release korelacija i SLO tabela.
- Risk-to-test-to-release-gate matrica i production-artifact dokaz.
- CI/CD trust mapa i immutable promotion dokaz.
- Rollout, compatibility, rollback/repair, izolovani restore, RPO i RTO dokaz.

### Obavezni failure i acceptance testovi

- Seed-uj PII/secret canary-je i proveri telemetry redaction.
- Dokazi da svaki release gate pada na seed-ovanom reprezentativnom defektu.
- Canary-uj release, aktiviraj guardrail, abortuj i izvrsi recovery.
- Restore-uj u izolaciji i proveri schemu, kljuceve, fajlove, queue-eve, search, tenant-e i kriticne tokove.

