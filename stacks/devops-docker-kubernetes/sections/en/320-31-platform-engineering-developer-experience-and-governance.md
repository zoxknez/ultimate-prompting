## 31. Platform Engineering, Developer Experience And Governance

**Objective:** Reduce cognitive load while preserving safe ownership and escape hatches.

### 31.1 Required Checks

1. Map platform products, paved roads, templates, catalogs, portals, APIs, golden paths, self-service actions, documentation, support, and ownership.
2. Measure onboarding, first deployment, rollback, secret access, preview environment, debugging, incident handoff, upgrade, and decommission workflows.
3. Ensure templates encode secure defaults without hiding critical behavior, locking teams into stale versions, or granting unnecessary privilege.
4. Verify ownership, support tiers, deprecation policy, versioning, migration guides, telemetry, feedback loops, adoption, satisfaction, and product SLOs.
5. Define controlled escape hatches with approval, visibility, expiry, compensating controls, and a path back to the paved road.
6. Audit tenancy, namespace or account vending, quota, network, identity, secret, billing, and deletion boundaries in self-service workflows.
7. Remove toil through automation only after the underlying invariant, failure behavior, ownership, and rollback are understood.

### 31.2 Minimum Evidence

- Platform product and ownership map.
- Measured developer journey and failure-path results.
- Template, self-service, exception, and deprecation assessment.

### 31.3 Exit Criteria

1. Critical developer workflows are safe, understandable, documented, measurable, and supported.
2. Self-service cannot silently cross tenant, identity, network, cost, or deletion boundaries.
3. Exceptions and deprecated paths are visible and actively converging.

