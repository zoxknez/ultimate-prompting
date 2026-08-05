## 4. Evidence Model And Required Records

### 4.1 Evidence Levels

| Level | Meaning | Allowed conclusion |
| --- | --- | --- |
| E0 | Claim or assumption only | Do not use for readiness decisions. |
| E1 | Static source or configuration evidence | Useful for discovery; runtime behavior remains unverified. |
| E2 | Resolved environment, dependency, generated-code, or build evidence | Confirms the tested build path, not installed behavior. |
| E3 | Packaged artifact, signature, and clean-machine installation evidence | Confirms delivered bytes and installation scope. |
| E4 | Instrumented runtime and user-journey evidence | Confirms behavior for the tested platform, configuration, data, and workload. |
| E5 | Production-like failure, upgrade, rollback, restore, or incident exercise | Required for strong resilience and recovery claims. |

### 4.2 Finding Record

1. Assign a stable finding ID, P0-P3 severity, confidence, evidence level, affected platform/version, file/symbol, and owner.
2. Record symptom, reproduction, root cause, trust boundary, business and technical impact, exploitability or failure conditions, and blast radius.
3. Distinguish source defect, build defect, packaging defect, installation defect, runtime defect, operational gap, and documentation gap.
4. Define the minimal complete fix, alternatives rejected, compatibility impact, migration requirement, rollback, and residual risk.
5. Attach exact commands, exit codes, relevant output excerpts, artifact hashes, screenshots or traces, test data, and timestamps.
6. Close a finding only after focused regression and the widest applicable packaged/runtime verification pass.

