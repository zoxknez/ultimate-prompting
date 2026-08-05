## 55. Acceptance Criteria

- Every production-relevant claim has status, evidence level, scope, and explicit uncertainty.
- Source, dependency, generated output, native host, artifact, signing, installation, runtime, telemetry, and rollback identities are reconciled.
- All critical business invariants and server authorization rules have positive, negative, duplicate, concurrent, interrupted, and recovery tests.
- Every claimed platform has an explicit support matrix, release build, artifact inspection, install/launch evidence, critical-journey tests, accessibility coverage, telemetry, and recovery path.
- No secret relies on client confidentiality, no privileged action relies only on UI checks, and no sensitive data crosses account or tenant boundaries.
- Lifecycle, cancellation, stream ownership, isolate/background behavior, process death, restoration, and resource cleanup are proven for critical flows.
- Storage migrations, offline queues, conflict resolution, logout/account switching, backup restore, upgrade, rollback, and incident recovery preserve invariants.
- Performance, size, memory, battery, network, disk, crash, and accessibility budgets are measured on representative targets and gated in delivery.
- Signing, provenance, SBOM, symbols, source maps, store/distribution metadata, staged rollout, abort criteria, and rollback/forward-fix procedures are verified.
- All P0/P1 findings are remediated or formally accepted by an authorized owner with compensating controls, expiry, and monitoring.

