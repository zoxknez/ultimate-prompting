## Mandatory Evidence Matrices

### M1 - Source, Toolchain And Runtime Identity

| Required column | Evidence |
| --- | --- |
| commit | `[VALUE / LINK / COMMAND / RESULT]` |
| Ruby engine and patch | `[VALUE / LINK / COMMAND / RESULT]` |
| Bundler and lock digest | `[VALUE / LINK / COMMAND / RESULT]` |
| artifact digest | `[VALUE / LINK / COMMAND / RESULT]` |
| process role | `[VALUE / LINK / COMMAND / RESULT]` |
| schema and release marker | `[VALUE / LINK / COMMAND / RESULT]` |

### M2 - Process And Capacity Topology

| Required column | Evidence |
| --- | --- |
| web workers | `[VALUE / LINK / COMMAND / RESULT]` |
| threads | `[VALUE / LINK / COMMAND / RESULT]` |
| job workers | `[VALUE / LINK / COMMAND / RESULT]` |
| scheduler | `[VALUE / LINK / COMMAND / RESULT]` |
| Cable | `[VALUE / LINK / COMMAND / RESULT]` |
| database and cache connections | `[VALUE / LINK / COMMAND / RESULT]` |

### M3 - Endpoint Authorization

| Required column | Evidence |
| --- | --- |
| route | `[VALUE / LINK / COMMAND / RESULT]` |
| actor | `[VALUE / LINK / COMMAND / RESULT]` |
| tenant | `[VALUE / LINK / COMMAND / RESULT]` |
| resource | `[VALUE / LINK / COMMAND / RESULT]` |
| allowed action | `[VALUE / LINK / COMMAND / RESULT]` |
| negative case | `[VALUE / LINK / COMMAND / RESULT]` |

### M4 - Business Invariants

| Required column | Evidence |
| --- | --- |
| invariant | `[VALUE / LINK / COMMAND / RESULT]` |
| application control | `[VALUE / LINK / COMMAND / RESULT]` |
| database control | `[VALUE / LINK / COMMAND / RESULT]` |
| concurrency test | `[VALUE / LINK / COMMAND / RESULT]` |
| reconciliation | `[VALUE / LINK / COMMAND / RESULT]` |
| owner | `[VALUE / LINK / COMMAND / RESULT]` |

### M5 - Transactions And Side Effects

| Required column | Evidence |
| --- | --- |
| flow | `[VALUE / LINK / COMMAND / RESULT]` |
| transaction manager | `[VALUE / LINK / COMMAND / RESULT]` |
| isolation | `[VALUE / LINK / COMMAND / RESULT]` |
| lock | `[VALUE / LINK / COMMAND / RESULT]` |
| external effect | `[VALUE / LINK / COMMAND / RESULT]` |
| crash recovery | `[VALUE / LINK / COMMAND / RESULT]` |

### M6 - Jobs And Schedulers

| Required column | Evidence |
| --- | --- |
| adapter | `[VALUE / LINK / COMMAND / RESULT]` |
| delivery semantics | `[VALUE / LINK / COMMAND / RESULT]` |
| retry | `[VALUE / LINK / COMMAND / RESULT]` |
| idempotency | `[VALUE / LINK / COMMAND / RESULT]` |
| mixed-version | `[VALUE / LINK / COMMAND / RESULT]` |
| operator recovery | `[VALUE / LINK / COMMAND / RESULT]` |

### M7 - Data And Migration Compatibility

| Required column | Evidence |
| --- | --- |
| schema step | `[VALUE / LINK / COMMAND / RESULT]` |
| old code | `[VALUE / LINK / COMMAND / RESULT]` |
| new code | `[VALUE / LINK / COMMAND / RESULT]` |
| backfill | `[VALUE / LINK / COMMAND / RESULT]` |
| cutover | `[VALUE / LINK / COMMAND / RESULT]` |
| rollback or forward repair | `[VALUE / LINK / COMMAND / RESULT]` |

### M8 - Security And Secret Boundaries

| Required column | Evidence |
| --- | --- |
| asset | `[VALUE / LINK / COMMAND / RESULT]` |
| owner | `[VALUE / LINK / COMMAND / RESULT]` |
| storage | `[VALUE / LINK / COMMAND / RESULT]` |
| rotation | `[VALUE / LINK / COMMAND / RESULT]` |
| revocation | `[VALUE / LINK / COMMAND / RESULT]` |
| incident evidence | `[VALUE / LINK / COMMAND / RESULT]` |

### M9 - External Dependencies

| Required column | Evidence |
| --- | --- |
| dependency | `[VALUE / LINK / COMMAND / RESULT]` |
| timeout budget | `[VALUE / LINK / COMMAND / RESULT]` |
| retry | `[VALUE / LINK / COMMAND / RESULT]` |
| circuit or bulkhead | `[VALUE / LINK / COMMAND / RESULT]` |
| degraded mode | `[VALUE / LINK / COMMAND / RESULT]` |
| reconciliation | `[VALUE / LINK / COMMAND / RESULT]` |

### M10 - Performance And Capacity

| Required column | Evidence |
| --- | --- |
| workload | `[VALUE / LINK / COMMAND / RESULT]` |
| SLO | `[VALUE / LINK / COMMAND / RESULT]` |
| measured limit | `[VALUE / LINK / COMMAND / RESULT]` |
| bottleneck | `[VALUE / LINK / COMMAND / RESULT]` |
| headroom | `[VALUE / LINK / COMMAND / RESULT]` |
| scale or shed action | `[VALUE / LINK / COMMAND / RESULT]` |

### M11 - Release And Rollback

| Required column | Evidence |
| --- | --- |
| artifact | `[VALUE / LINK / COMMAND / RESULT]` |
| canary | `[VALUE / LINK / COMMAND / RESULT]` |
| guardrail | `[VALUE / LINK / COMMAND / RESULT]` |
| abort threshold | `[VALUE / LINK / COMMAND / RESULT]` |
| rollback steps | `[VALUE / LINK / COMMAND / RESULT]` |
| verification | `[VALUE / LINK / COMMAND / RESULT]` |

### M12 - Backup, Restore And DR

| Required column | Evidence |
| --- | --- |
| data set | `[VALUE / LINK / COMMAND / RESULT]` |
| backup evidence | `[VALUE / LINK / COMMAND / RESULT]` |
| restore evidence | `[VALUE / LINK / COMMAND / RESULT]` |
| RPO | `[VALUE / LINK / COMMAND / RESULT]` |
| RTO | `[VALUE / LINK / COMMAND / RESULT]` |
| reconciliation | `[VALUE / LINK / COMMAND / RESULT]` |

