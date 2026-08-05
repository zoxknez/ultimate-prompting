## Phase 28 - Deployment Models, Containers, Serverless, And Multi-Instance Behavior

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Identify the exact deployment model for every API, worker, scheduler, migrator, CLI, and realtime process.
- Verify build and runtime image, user, filesystem, permissions, init, signals, certificates, locale, DNS, and native libraries.
- Run as non-root where feasible, use read-only filesystem and dropped capabilities where compatible, and isolate temp storage.
- Define CPU, memory, storage, file-descriptor, connection, process, and concurrency limits.
- Do not rely on warm memory, module globals, local disk, process locks, or one instance for correctness.
- Verify serverless cold start, reuse, concurrency, timeout, payload, streaming, pool, background work, and shutdown semantics.

### Required Evidence

- Produce and preserve the deployment and target-support matrix.
- Produce and preserve runtime security, limits, and multi-instance evidence.
- Produce and preserve graceful drain and process-replacement results.

### Mandatory Failure And Acceptance Tests

- Prove that non-root and read-only runtime preserves functionality.
- Prove that instance replacement does not lose authoritative state.
- Prove that serverless concurrency does not exhaust shared dependencies.

