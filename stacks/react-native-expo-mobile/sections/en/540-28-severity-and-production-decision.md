## 28. Severity And Production Decision
| Level | Definition | Release effect |
| --- | --- | --- |
| P0 | Active compromise, severe data integrity loss, unsafe signing or update path, mass cross-tenant exposure, unrecoverable critical failure, or immediate user safety risk. | Stop release or enter incident mode immediately. |
| P1 | Likely critical security, privacy, financial, availability, store, migration, or rollback failure with material impact. | Block release until fixed or formally contained with approved evidence. |
| P2 | Material defect, unsupported configuration, performance, accessibility, observability, or operational weakness. | Fix before broad rollout or accept with owner, deadline, compensating control, and monitoring. |
| P3 | Limited improvement, maintainability issue, optimization, documentation gap, or optional modernization. | Prioritize by value and risk; does not alone block release. |

Final decision must be exactly one of: READY, READY_WITH_CONDITIONS, NOT_READY, or INCIDENT.

