## 24. CI/CD, Provenance, Rollout, And Recovery

### 24.1 CI/CD Trust Boundaries
- Map repository permissions, branch protection, pull-request trust, fork behavior, workflow permissions, runners, caches, artifacts, OIDC, secrets, and deployment approvals.
- Prevent untrusted pull-request code from accessing signing credentials, update keys, production tokens, store APIs, private packages, or protected caches.
- Pin or verify actions, build images, package managers, toolchains, downloaded binaries, native dependencies, and remote scripts.
- Require clean checkout, immutable dependencies, tests, release builds, artifact inspection, SBOM, provenance, signatures, and approval gates.
- Separate build, signing, submission, OTA publication, channel mapping, and production rollout permissions.
- Retain immutable evidence linking actor, workflow, source, environment, artifact, signature, store submission, update publication, and rollout decision.

### 24.2 Rollout, Abort, Rollback, And Forward Fix
- Define rollout cohort, platform, device, OS, app version, native runtime, update channel, tenant, geography, feature flag, and monitoring window.
- Set quantitative guardrails for crash, ANR, startup, update success, critical journey, auth, sync, battery, backend errors, and support volume.
- Assign authority to pause, abort, roll back OTA, halt store rollout, disable feature, stop background work, revoke credential, and initiate incident mode.
- Separate JavaScript rollback, native binary rollback, configuration rollback, backend rollback, data rollback, reconciliation, and forward repair.
- Prove old and new binaries, old and new updates, old and new backend contracts, and old and new local schemas can coexist for the required window.
- Never label rollback ready until it has been exercised with representative data, installed versions, channels, and failure states.

### 24.3 Backup, Restore, And Incident Recovery
- Inventory recoverable server data, client data, update metadata, symbols, source maps, signing records, store records, configuration, and audit evidence.
- Define RPO and RTO per critical journey and verify them with isolated restore and reconciliation exercises.
- Test recovery from corrupted local data, bad OTA, bad native release, lost signing credential, revoked certificate, backend restore, and incompatible schema.
- Preserve forensic evidence before deleting caches, uninstalling, republishing, rotating keys, rebuilding, or restoring.
- For supply-chain compromise rebuild from trusted source, clean runners, verified dependencies, newly issued credentials, and reviewed artifacts.
- Document containment, eradication, recovery, user impact, notification obligations, residual risk, and recurrence prevention.

