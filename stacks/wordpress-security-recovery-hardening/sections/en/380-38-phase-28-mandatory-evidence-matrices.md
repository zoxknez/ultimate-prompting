## 38. Phase 28 - Mandatory Evidence Matrices

Complete every applicable matrix. An empty matrix is not evidence.

### M1 - Asset and control-plane matrix

| Asset/control plane | Owner | Access path | Authentication | Logs | Last change | Evidence status | Risk |
| --- | --- | --- | --- | --- | --- | --- | --- |

### M2 - Source-to-runtime integrity matrix

| Component | Source/provenance | Expected version/hash | Installed version/hash | Runtime evidence | Drift | Decision |
| --- | --- | --- | --- | --- | --- | --- |

### M3 - Persistence matrix

| Persistence surface | Examination method | Result | Evidence ID | Remediation | Verification |
| --- | --- | --- | --- | --- | --- |

### M4 - Identity and secret matrix

| Identity/secret | Scope | Last rotated | Suspicious activity | Action | Revocation verified |
| --- | --- | --- | --- | --- | --- |

### M5 - Database integrity matrix

| Data domain/table | Indicator/query | Affected objects | Mutation method | Backup/rollback | Verification |
| --- | --- | --- | --- | --- | --- |

### M6 - Scheduled execution matrix

| Scheduler | Hook/job | Owner | Payload/arguments | Last/next run | Decision | Verification |
| --- | --- | --- | --- | --- | --- | --- |

### M7 - Edge and cache matrix

| Layer | Configuration owner | Suspicious state | Evidence | Invalidation/change | Verification |
| --- | --- | --- | --- | --- | --- |

### M8 - Backup and restore matrix

| Backup | Timestamp | Before plausible compromise | Integrity | Isolated scan | Restore test | Data gap | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |

### M9 - Vulnerability and patch matrix

| Component | Installed | Fixed/supported target | Exposure | Exploit evidence | Patch/change | Regression result |
| --- | --- | --- | --- | --- | --- | --- |

### M10 - Functional critical-flow matrix

| Flow | Anonymous/auth role | Expected | Result | Security assertion | Evidence |
| --- | --- | --- | --- | --- | --- |

### M11 - Notification and stakeholder matrix

| Stakeholder | Trigger | Decision owner | Deadline/source | Status | Evidence |
| --- | --- | --- | --- | --- | --- |

### M12 - Production-return matrix

| Gate | Required evidence | Result | Open risk | Approver | Timestamp |
| --- | --- | --- | --- | --- | --- |

