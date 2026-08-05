## 38. Severity And Release Decision

### 38.1 P0-P3 Interpretation

| Severity | Meaning | Default action |
| --- | --- | --- |
| P0 | Active compromise, arbitrary code execution, signing/update compromise, irreversible widespread data loss, or immediate critical safety/business impact. | Stop release or operation; contain, preserve evidence, and recover. |
| P1 | High-likelihood severe security, authorization, data-integrity, crash-loop, update, migration, or rollback failure affecting material users. | Block release until fixed and verified or explicitly risk-accepted by authorized owners. |
| P2 | Material reliability, performance, accessibility, operability, privacy, maintainability, or compatibility defect with bounded impact. | Remediate before release when applicable or schedule with owner, deadline, controls, and acceptance criteria. |
| P3 | Low-risk improvement, cleanup, documentation, test depth, or optional modernization. | Prioritize transparently; do not present as a blocker without evidence. |

### 38.2 Verdicts

1. `READY`: all applicable production evidence and Definition of Done conditions are satisfied with no unresolved blocking risk.
2. `READY_WITH_CONDITIONS`: no unresolved P0/P1 blocker, but explicit bounded conditions, owners, dates, controls, and evidence ceilings remain.
3. `NOT_READY`: one or more blocking security, correctness, data, packaging, platform, update, rollback, restore, or operational conditions remain.
4. `INCIDENT`: active or suspected compromise, unsafe release channel, corrupted state, or untrusted build/runtime requires containment and trusted recovery.
5. Never convert lack of evidence into a positive verdict; state `UNVERIFIED` and the exact missing proof.

