## 24. Policy As Code And Preventive Controls

**Objective:** Convert critical invariants into tested, observable, governable controls.

### 24.1 Required Checks

1. Define critical invariants for identity, privilege, network, artifacts, resources, encryption, public exposure, data location, labels, ownership, versions, and backup.
2. Map each invariant to preventive, detective, responsive, or accepted-risk controls across source, CI, registry, admission, cloud, runtime, and monitoring layers.
3. Audit policy source, review, tests, bundles, distribution, versioning, ownership, exception process, expiry, telemetry, and rollback.
4. Use representative positive, negative, boundary, legacy, emergency, and malicious fixtures. Verify policy results before enforcement.
5. Roll out in audit or warn mode where appropriate, measure false positives and bypasses, then enforce with an explicit change plan.
6. Verify policy-engine availability, timeout, cache, stale-bundle, fail-open or fail-closed behavior, break-glass, and control-plane dependencies.
7. Do not duplicate controls blindly. Identify authoritative layer and expected behavior when layers disagree.

### 24.2 Minimum Evidence

- Invariant-to-control matrix with owners and enforcement points.
- Policy test corpus, coverage, exceptions, false-positive, and bypass evidence.
- Policy-engine failure and rollback test results.

### 24.3 Exit Criteria

1. P0 and P1 invariants have effective preventive or rapidly detective controls.
2. Exceptions are narrow, attributable, time-bound, visible, and tested.
3. Policy failure behavior is understood and cannot create an unnoticed broad bypass.

