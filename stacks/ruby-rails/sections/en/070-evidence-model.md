## Evidence Model

| Level | Meaning | Allowed conclusion |
| --- | --- | --- |
| E0 | Assumption, memory or undocumented statement. | No finding closure and no readiness claim. |
| E1 | Source or configuration inspection. | Implementation intent only. |
| E2 | Static tool, dependency, schema or build analysis. | Potential issue or compatibility evidence. |
| E3 | Reproducible local or CI execution on a declared environment. | Behavior in that environment only. |
| E4 | Production-like release artifact, realistic data, concurrency and failure testing. | Strong release evidence with stated limits. |
| E5 | Observed production behavior, controlled rollout, telemetry, rollback or isolated restore. | Production claim within the observed scope. |

