## 5. Evidence, Findings And Severity

### 5.1 Finding Schema

```text
ID
severity: P0 | P1 | P2 | P3
confidence: high | medium | low
evidence_status: CONFIRMED | PARTIALLY_CONFIRMED | UNVERIFIED
domain and affected assets
finding and violated invariant
evidence with source, command, scope, time and artifact
failure, abuse or exploit path
business, security, availability, data and cost impact
blast radius and prerequisites
immediate containment if needed
root cause and contributing conditions
recommended repair and safer alternatives
owner, dependencies and approval boundary
verification and regression tests
rollout, observation and stop conditions
rollback or compensating action
residual risk and acceptance decision
```

### 5.2 Severity Model

| Severity | Meaning | Typical examples |
| --- | --- | --- |
| `P0` | Active or imminent catastrophic impact requiring immediate coordinated action. | Compromised production credentials, uncontrolled destructive access, active exfiltration, unrecoverable data loss, total critical outage without safe recovery. |
| `P1` | High-probability or high-impact production risk. | Cluster-admin CI path, public privileged workload, invalid restore evidence, single-region critical service without accepted risk, exploitable admission bypass. |
| `P2` | Material weakness with bounded impact or prerequisites. | Over-broad namespace permissions, missing disruption test, noisy alerts, weak resource tuning, drift without immediate exploit path. |
| `P3` | Low-risk hardening, maintainability, evidence, or efficiency issue. | Documentation drift, non-critical tag mutability, missing ownership metadata, low-value idle cost. |

Severity is based on realistic impact, likelihood, exposure, blast radius, recoverability, detectability, and evidence confidence. It is not based on scanner labels alone.

### 5.3 Evidence Hierarchy

1. Observed user impact, controlled failure test, or successful isolated restore with captured results.
2. Live runtime, cloud-provider, cluster, identity, network, storage, and telemetry evidence from an authorized scope.
3. Verified artifact identity, signature, provenance, SBOM, digest, deployment revision, and controller history.
4. Rendered configuration, policy evaluation, infrastructure plan, static analysis, tests, and reproducible local evidence.
5. Repository intent, diagrams, tickets, comments, and interviews.
6. Inference without direct verification.

