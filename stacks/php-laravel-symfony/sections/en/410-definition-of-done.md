## Definition of Done

1. Scope, assumptions, exclusions, environments, runtime modes, owners, and evidence limitations are explicit.
2. The intended source, build inputs, dependencies, generated code, artifact, deployment, schema, and running processes are cryptographically or operationally linked.
3. All critical HTTP, console, queue, scheduler, webhook, file, admin, support, and recovery surfaces are inventoried and authorized.
4. Business invariants survive concurrency, retry, duplicate delivery, partial failure, crash, timeout, cancellation, and mixed-version execution.
5. Database, cache, session, queue, storage, search, and external-provider authority and recovery behavior are proven.
6. Framework-specific lifecycle, proxy, container, policy, voter, middleware, worker, and cache semantics are tested from the production artifact.
7. Security boundaries withstand exploit-oriented negative tests and abusive resource patterns.
8. Capacity and reliability are measured under representative cold, burst, sustained, soak, slowdown, failover, and overload conditions.
9. Observability detects and explains correctness, security, availability, latency, queue, data, release, and recovery failures.
10. The production artifact is reproducible, minimal, immutable, signed or verified, promoted without rebuild, and safely replaceable.
11. Rollout, rollback, forward repair, credential revocation, isolated restore, incident containment, and trusted rebuild are executable and tested.
12. The final decision, residual risks, exceptions, owners, deadlines, evidence, and next verification date are recorded.

If any item is not proven, the audit is not complete. Mark it `UNVERIFIED`, explain the risk, and reflect it in the final readiness decision.

