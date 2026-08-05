## 36. Final Report Contract

### 36.1 Required Report Order

1. Title, audit date, version, mode, auditors, scope, authorization, and evidence ceiling.
2. Executive verdict and the most important business, security, reliability, and recovery decisions.
3. System, trust-boundary, environment, identity, data-flow, and ownership overview.
4. Source-to-production integrity and live drift assessment.
5. Findings ordered by severity, then exploit or failure likelihood and business impact.
6. Implemented changes with diffs, approvals, verification, observation, rollback, and residual risk.
7. Test and evidence matrix including blocked, failed, not-run, and not-applicable checks.
8. Security, supply-chain, reliability, performance, observability, backup, restore, DR, incident, and cost summaries.
9. Prioritized remediation roadmap with owners, dependencies, effort, risk reduction, rollout, and verification.
10. Accepted risks, unresolved assumptions, evidence gaps, decision deadlines, and required follow-up.
11. Final verdict and exact conditions required to change it.

### 36.2 Verdict Rules

| Verdict | Required meaning |
| --- | --- |
| `ready` | No unresolved P0 or P1 finding, critical paths verified, source-to-production identity proven, recovery demonstrated, ownership established, and evidence ceiling sufficient. |
| `ready-with-conditions` | No unacceptable immediate blocker, but explicit bounded conditions, owners, deadlines, monitoring, and rollback remain. |
| `not-ready` | Any unresolved P0, unacceptable P1, missing critical restore, unverifiable production artifact, uncontrolled privileged path, unsafe release path, or insufficient evidence for a material claim. |

### 36.3 Machine-Readable Summary

```json
{
  "audit_id": "...",
  "baseline_date": "2026-08-05",
  "scope": ["..."],
  "verdict": "ready | ready-with-conditions | not-ready",
  "evidence_ceiling": "...",
  "findings": {"P0": 0, "P1": 0, "P2": 0, "P3": 0},
  "coverage": {"passed": 0, "failed": 0, "blocked": 0, "not_applicable": 0},
  "production_artifact_verified": false,
  "restore_verified": false,
  "open_conditions": ["..."],
  "accepted_risks": ["..."],
  "next_decision_date": "YYYY-MM-DD"
}
```

