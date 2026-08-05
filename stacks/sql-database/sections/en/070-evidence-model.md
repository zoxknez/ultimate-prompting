## Evidence Model

| Level | Meaning | Allowed conclusion |
| --- | --- | --- |
| E0 | Assumption, memory, vendor claim or undocumented statement. | No closure and no readiness claim. |
| E1 | Schema, source, migration or configuration inspection. | Intent and possible risk only. |
| E2 | Catalog, static analysis, dependency, plan or backup metadata. | Stronger evidence, not runtime proof. |
| E3 | Reproducible test on declared engine and dataset. | Behavior in that declared environment. |
| E4 | Production-like data, concurrency, migration, failover or restore test. | Strong release evidence with stated limits. |
| E5 | Observed controlled production rollout, failover, reconciliation or isolated restore. | Production claim within the observed scope. |

