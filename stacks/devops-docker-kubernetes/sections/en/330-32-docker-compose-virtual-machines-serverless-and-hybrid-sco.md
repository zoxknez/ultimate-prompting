## 32. Docker Compose, Virtual Machines, Serverless And Hybrid Scope

**Objective:** Apply equivalent production rigor outside Kubernetes.

### 32.1 Required Checks

1. For Compose, verify interpolation, profiles, dependency semantics, health, restart, resource limits, networks, volumes, secrets, configs, logging, update process, and host assumptions.
2. For virtual machines, audit image provenance, bootstrap, patching, configuration management, metadata access, host firewall, SSH or remote administration, endpoint protection, disk encryption, backup, replacement, and drift.
3. For serverless, audit package and layer provenance, identity, event sources, concurrency, cold start, retries, dead-letter behavior, idempotency, timeouts, VPC access, secrets, logs, deployment versions, and rollback.
4. For edge systems, verify constrained connectivity, clock, certificates, local state, remote update signing, staged rollout, physical access, offline operation, and recovery.
5. For hybrid or multi-cloud systems, audit identity federation, routing, DNS, data transfer, egress cost, consistency, observability, support boundaries, failover, and correlated dependencies.
6. Do not copy Kubernetes controls mechanically. Preserve the invariant while adapting implementation to the actual runtime.
7. Test startup, shutdown, replacement, update, rollback, host or region loss, secret rotation, backup, restore, and incident isolation for each runtime type.

### 32.2 Minimum Evidence

- Runtime-specific architecture, trust, ownership, and lifecycle inventory.
- Equivalent-control mapping outside Kubernetes.
- Update, failure, rollback, and recovery evidence for each applicable runtime.

### 32.3 Exit Criteria

1. Non-Kubernetes production paths meet the same business invariants for identity, artifact integrity, isolation, observability, and recovery.
2. Runtime-specific limitations and shared failure domains are explicit.
3. Updates and recovery are tested for every critical runtime type.

