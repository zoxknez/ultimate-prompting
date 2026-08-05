## 19. Helm, Kustomize, CRDs, Operators And Webhooks

**Objective:** Make generated configuration deterministic, reviewable, upgrade-safe, and failure-aware.

### 19.1 Required Checks

1. Render every environment from a clean checkout with pinned dependencies and compare output, values, patches, defaults, capabilities, hooks, and generated names.
2. Audit chart, subchart, plugin, remote base, OCI artifact, and template-function provenance, version constraints, checksums, and update policy.
3. Detect unsafe defaults, hidden mutable values, environment leakage, secret rendering, duplicate resources, ordering assumptions, and non-idempotent hooks.
4. Audit CRD schemas, pruning, defaults, status, subresources, conversion webhooks, stored versions, migration, ownership, finalizers, and deletion effects.
5. Audit operators and admission webhooks for RBAC, image provenance, leader election, reconciliation idempotency, retry, backoff, finalizers, upgrade order, availability, TLS, timeout, and failurePolicy.
6. Test install, upgrade from supported prior versions, rollback limits, uninstall, CRD preservation, webhook outage, and partial reconciliation.
7. Do not claim Helm rollback restores external state, data migrations, CRD schema, or cloud resources unless explicitly verified.

### 19.2 Minimum Evidence

- Deterministic render diff for all environments.
- CRD, operator, webhook, and plugin compatibility matrix.
- Install, upgrade, outage, rollback, and uninstall test evidence.

### 19.3 Exit Criteria

1. Generated resources are deterministic, reviewable, and free of secret material.
2. CRD and webhook upgrade order cannot brick the control path or silently corrupt objects.
3. Rollback limitations and external side effects are explicit.

