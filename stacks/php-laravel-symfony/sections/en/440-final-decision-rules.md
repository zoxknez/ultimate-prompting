## Final Decision Rules

| Decision | Required condition |
| --- | --- |
| READY | No unresolved P0 or P1, all critical paths proven, all mandatory controls pass, and rollback and restore are tested. |
| READY_WITH_CONDITIONS | No P0, no unaccepted P1, remaining bounded risks have owners, deadlines, monitoring, compensating controls, and expiry. |
| NOT_READY | A release blocker, unknown critical path, unsupported critical component, failed recovery proof, or material unowned risk remains. |
| INCIDENT | Active compromise, unsafe integrity uncertainty, destructive failure, or immediate containment and trusted rebuild is required. |

