## 20. GitOps, Progressive Delivery And Environment Promotion

**Objective:** Control reconciliation, promotion, rollout risk, and emergency changes.

### 20.1 Required Checks

1. Verify GitOps repository ownership, branch protection, review rules, signing, path permissions, environment separation, controller identity, and secret access.
2. Audit source definitions, generator behavior, sync waves, hooks, health checks, pruning, self-heal, retry, timeouts, exclusions, ignore rules, and multi-tenancy boundaries.
3. Ensure production promotion requires reviewed evidence and preserves immutable artifact identity.
4. Verify canary, blue-green, rolling, feature-flag, shadow, or traffic-splitting analysis uses meaningful metrics, minimum sample, guardrails, abort conditions, and rollback.
5. Test controller outage, source outage, stale cache, invalid desired state, partial sync, failed hook, stuck finalizer, and emergency pause.
6. Define an emergency-change path that preserves evidence, approval, attribution, reconciliation, and time-bound cleanup.
7. Ensure preview environments cannot access production data, credentials, networks, billing authority, or shared mutable resources without explicit controls.

### 20.2 Minimum Evidence

- GitOps trust and permission model.
- Promotion and progressive-delivery evidence for a representative release.
- Controller failure and emergency-change reconciliation drill.

### 20.3 Exit Criteria

1. Only approved immutable artifacts can reach production through attributable promotion paths.
2. Rollout analysis detects meaningful regressions and aborts safely.
3. Emergency changes are visible, reversible, reconciled, and cannot become permanent shadow configuration.

