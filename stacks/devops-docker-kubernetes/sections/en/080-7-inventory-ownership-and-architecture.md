## 7. Inventory, Ownership And Architecture

**Objective:** Build a verified system map and remove unknown ownership.

### 7.1 Required Checks

1. Discover all repositories, services, jobs, queues, databases, object stores, caches, registries, clusters, namespaces, accounts, public endpoints, and third-party dependencies.
2. Map request, event, batch, administrative, deployment, secret, and recovery data flows across trust boundaries.
3. Identify tier, criticality, data classification, user impact, SLO, RPO, RTO, owner, on-call rotation, and runbook for every critical component.
4. Compare diagrams and catalogs with live DNS, cloud inventory, cluster APIs, registries, CI systems, and telemetry.
5. Identify orphaned, duplicated, shadow, unmanaged, end-of-life, and internet-exposed assets.
6. Document shared dependencies and correlated failure domains, including identity, DNS, KMS, registry, CI, control plane, and observability.

### 7.2 Minimum Evidence

- Architecture and trust-boundary diagram tied to live evidence.
- Machine-readable asset and ownership inventory.
- List of unknown, orphaned, shared, and critical dependencies.

### 7.3 Exit Criteria

1. Critical services have confirmed owners, dependencies, SLOs, RPOs, RTOs, and escalation paths.
2. Live architecture materially matches documented intent or drift is registered.
3. No internet-exposed or privileged unknown asset remains untriaged.

