## 53. Mandatory Evidence Matrices

Produce every applicable matrix. A missing platform, artifact, environment, identity, or recovery path must be visible rather than silently excluded.

### 53.1 Platform And Device Matrix

- Platform, OS/browser version, architecture, device/window class, input mode, distribution channel, support status, test depth, owner, and evidence.
- Include minimum, typical, latest, low-resource, accessibility, and representative vendor/device cases.

### 53.2 Toolchain And Dependency Matrix

- Local, CI, release, and production-resolved Flutter, Dart, engine, package graph, native toolchain, platform SDK, and generator versions.
- Mark drift, floating versions, unsupported combinations, prerelease components, native binary provenance, and remediation.

### 53.3 Artifact Identity Matrix

- Commit, dirty state, build job, artifact hash, package/bundle ID, version/build, flavor, signing identity, store/channel, symbols/source maps, SBOM, provenance, and runtime confirmation.
- Cover every promoted, staged, production, rollback, and incident-rebuild artifact.

### 53.4 Critical Journey Matrix

- Journey, role, tenant, starting state, network state, lifecycle state, platform, expected invariant, negative case, telemetry, rollback, and evidence.
- Include authentication, privileged mutations, payments/orders where applicable, offline flows, file/media flows, notification/deep-link entry, and recovery.

### 53.5 Authorization And Tenant Matrix

- Actor, subject, role, tenant, resource, operation, client presentation, server enforcement, local partition, negative test, revocation behavior, and evidence.
- Include direct route entry, changed identifier, stale link, account switch, tenant switch, impersonation, background work, and notifications.

### 53.6 Data And Storage Matrix

- Data class, owner, authority, location, account/tenant partition, encryption, key, backup, retention, deletion, export, migration, corruption recovery, and evidence.
- Include memory, secure storage, database, files, cache, browser storage, notifications, logs, crash reports, analytics, and backups.

### 53.7 Lifecycle And Concurrency Matrix

- Operation, owner, start state, interruption, cancellation, timeout, duplicate, stale-result rule, account/tenant change, process death, resume, cleanup, and evidence.
- Cover network calls, streams, state controllers, background jobs, isolates, platform channels, uploads/downloads, payments, migrations, and updates.

### 53.8 Plugin And Native Boundary Matrix

- Plugin/API, platform implementation, native dependency, permission/entitlement, channel/FFI contract, lifecycle, threading, error model, unsupported behavior, tests, owner, and evidence.
- Include federated implementations, platform views, background entrypoints, multiple engines, native assets, and security-sensitive bridges.

### 53.9 Permission And Hardware Matrix

- Capability, platform declaration, runtime state, purpose, data accessed, fallback, revocation, lifecycle, hardware absence, privacy disclosure, test device, and evidence.
- Include denied, permanently denied, restricted, limited, approximate, one-time, while-in-use, background, and revoked states where applicable.

### 53.10 Release And Rollout Matrix

- Platform/channel, artifact, cohort, prerequisite, store/install step, telemetry gate, acceptance threshold, abort trigger, rollback/forward-fix path, owner, and evidence.
- Include clean install, upgrades from supported versions, restored backup, low disk, offline launch, update interruption, old/new coexistence, and support communication.

### 53.11 Observability And SLO Matrix

- Critical journey or resource, SLI, target, source, dimensions, sampling, privacy, alert, owner, runbook, release gate, retention, and evidence.
- Include crash-free use, startup, jank, memory, network, auth, migration, sync, background work, notifications, update/install, and business outcomes.

### 53.12 Recovery And Incident Matrix

- Scenario, detection, evidence source, containment, revoked material, trusted source, rebuild/restore step, user impact, communication, RPO/RTO, owner, validation, and evidence.
- Include signing-key loss, malicious dependency, update compromise, data exposure, backend loss, store loss, telemetry outage, crash loop, and destructive migration.

