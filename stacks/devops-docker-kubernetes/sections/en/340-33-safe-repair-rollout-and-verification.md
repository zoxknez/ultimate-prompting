## 33. Safe Repair, Rollout And Verification

**Objective:** Convert confirmed findings into controlled, reversible, evidence-backed changes.

### 33.1 Required Checks

1. Register the finding, invariant, owner, prerequisites, expected effect, blast radius, approval boundary, verification, rollout, stop conditions, rollback, and residual risk before editing.
2. Create the smallest coherent change. Do not mix unrelated upgrades, formatting, refactors, policy changes, and operational changes.
3. Validate syntax, schema, render, lint, unit tests, policy, security, plan, diff, and isolated runtime behavior before wider rollout.
4. Back up or snapshot affected state when appropriate and verify the backup is usable before destructive or stateful change.
5. Roll out through the safest representative environment, then canary or bounded scope, with named observers and a defined observation window.
6. Measure user impact, SLOs, errors, saturation, security signals, data correctness, cost, and control-plane health during rollout.
7. Stop or roll back immediately when a stop condition is reached. Record actual rollback result rather than assuming success.
8. Repeat focused regression, failure, security, and recovery tests after the change and update documentation, ownership, and runbooks.

### 33.2 Minimum Evidence

- Finding-to-change trace with review and approval.
- Before, during, after, and rollback evidence.
- Focused regression and residual-risk record.

### 33.3 Exit Criteria

1. Every applied change is attributable, reviewed, reversible, observed, and verified.
2. No unplanned broad upgrade, destructive side effect, or hidden risk acceptance occurred.
3. Residual risk has an explicit owner and decision.

