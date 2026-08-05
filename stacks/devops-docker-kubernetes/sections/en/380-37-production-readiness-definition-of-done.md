## 37. Production Readiness Definition Of Done

1. Scope, authorization, owners, criticality, environments, identities, data flows, dependencies, SLOs, RPOs, and RTOs are explicit.
2. Critical production artifacts are traced to reviewed source, protected builds, immutable digests, verified provenance, signatures, policy, and promotion.
3. Desired state, GitOps state, live cluster state, cloud state, and user-observed behavior are reconciled or documented as accepted drift.
4. Container, runtime, host, cluster, workload, identity, network, secret, storage, CI/CD, and supply-chain controls are verified against realistic abuse and failure paths.
5. Critical workloads meet measured performance, capacity, scaling, availability, data-correctness, and graceful-degradation requirements.
6. SLOs, telemetry, alerts, on-call routing, runbooks, incident roles, and escalation are tested and actionable.
7. Backups are protected and representative critical restores, failover, and failback meet accepted objectives with integrity evidence.
8. No unresolved P0 or unacceptable P1 finding remains. Every accepted risk has an accountable owner, rationale, expiry or review date, and compensating controls.
9. Every implemented change has focused tests, approval, rollout evidence, observation, rollback evidence, documentation, and ownership.
10. Version, support, deprecation, upgrade, vulnerability, cost, quota, and dependency risks have time-bound plans.
11. The final verdict is supported by the evidence ceiling and does not overclaim inaccessible production behavior.

