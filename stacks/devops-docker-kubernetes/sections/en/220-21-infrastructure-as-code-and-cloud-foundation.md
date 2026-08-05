## 21. Infrastructure As Code And Cloud Foundation

**Objective:** Make cloud changes reviewable, deterministic, least-privileged, and recoverable.

### 21.1 Required Checks

1. Inventory IaC roots, modules, providers, backends, workspaces or stacks, state ownership, lock mechanism, environments, imports, generated code, and manual resources.
2. Pin provider and module constraints deliberately, verify checksums and provenance, and reject unreviewed remote execution or mutable module sources.
3. Protect state with encryption, least privilege, versioning, locking, backup, recovery, audit logs, separation, and secret-aware handling.
4. Review plans for replacement, deletion, force-new, implicit defaults, unknown values, data sources, provider side effects, quota impact, and blast radius.
5. Detect drift, unmanaged resources, imports, moved blocks, tainted resources, state surgery, console changes, orphan dependencies, and stale outputs.
6. Audit organization, account, project, region, network, IAM, KMS, logging, budget, quota, support, and break-glass foundations before application resources.
7. Test plan, policy, apply in isolation, partial failure, interrupted apply, import, rollback or forward-fix, state restore, and provider outage behavior.
8. Never run production apply from an unreviewed local workstation when a controlled pipeline is required.

### 21.2 Minimum Evidence

- IaC topology, ownership, backend, state, and permission inventory.
- Representative plan review with destructive and unknown-value analysis.
- State backup, restore, interruption, and drift-reconciliation evidence.

### 21.3 Exit Criteria

1. Production infrastructure changes are reviewed, attributable, policy-checked, and executed through approved identities.
2. State is protected and recoverable without exposing secrets.
3. Destructive, replacement, drift, and partial-apply risks are explicit before execution.

