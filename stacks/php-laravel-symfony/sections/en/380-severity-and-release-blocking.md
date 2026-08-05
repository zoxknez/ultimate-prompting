## Severity and Release Blocking

| Severity | Meaning | Default release effect |
| --- | --- | --- |
| P0 | Active compromise, catastrophic integrity or authorization failure, unrecoverable loss risk, or unsafe production state. | Stop rollout or traffic, enter INCIDENT mode, contain immediately. |
| P1 | High-confidence critical exploit, cross-tenant access, major data loss or duplication, broken recovery, or severe availability risk. | Block release until fixed and verified; require accountable exception only under emergency governance. |
| P2 | Material defect with bounded impact, missing defense, compatibility risk, or operational weakness. | Fix before release or accept with owner, deadline, monitoring, and compensating control. |
| P3 | Low-impact weakness, maintainability issue, optimization, or evidence improvement. | Track with justified priority and acceptance criteria. |

- Any unknown on a critical trust, authorization, transaction, migration, or recovery path is release-blocking until verified or explicitly risk-accepted by the accountable authority.
- Severity is based on realistic impact and exploitability, not code style, finding count, or remediation effort.

