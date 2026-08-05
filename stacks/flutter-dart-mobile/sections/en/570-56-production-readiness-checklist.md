## 56. Production Readiness Checklist

- [ ] Scope, owners, authorization, evidence ceiling, critical journeys, and support claims are documented.
- [ ] Workspace, user data, signing material, stores, and production systems were protected throughout the audit.
- [ ] Resolved Flutter/Dart/native toolchains and dependencies are supported, reproducible, and free of unexplained drift.
- [ ] Generated code and assets reproduce cleanly and privilege-impacting diffs are reviewed.
- [ ] Architecture preserves domain invariants, explicit ownership, platform isolation, lifecycle, and testability.
- [ ] Authentication, authorization, tenant isolation, secrets, privacy, and data lifecycle meet documented policy.
- [ ] Async operations, streams, isolates, background jobs, channels, FFI, and plugins have bounded lifecycle and failure behavior.
- [ ] Network, WebView, storage, migration, offline, files, permissions, hardware, notifications, and deep links have adversarial coverage.
- [ ] Android, iOS/iPadOS, web, Windows, macOS, and Linux claims are individually proven or explicitly excluded.
- [ ] Adaptive layout, accessibility, localization, RTL, input modes, and reduced-motion behavior pass critical journeys.
- [ ] Release performance, capacity, memory, battery, size, symbols, and diagnostic budgets meet approved thresholds.
- [ ] Layered tests and quality gates cover source, generated code, native boundaries, artifacts, installation, upgrade, and recovery.
- [ ] Telemetry is privacy-safe, artifact-aware, actionable, resilient, and linked to owners and runbooks.
- [ ] Flavor and environment isolation prevents cross-targeting and feature flags cannot grant authorization.
- [ ] CI/CD uses reviewed trust boundaries, immutable promotion, protected signing, provenance, SBOM, and retained recovery artifacts.
- [ ] Store/distribution, install, update, staged rollout, abort, rollback/forward-fix, and support procedures are tested.
- [ ] Backup restore, signing/store access recovery, trusted rebuild, incident containment, and measured RPO/RTO are demonstrated.
- [ ] Residual risks, accepted exceptions, expiry, owners, compensating controls, and next review are recorded.

