## 34. Mandatory Test Matrix

Run only tests that are authorized and safe for the target. Record `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE` with evidence for every row.

| Domain | Minimum tests |
| --- | --- |
| Repository and configuration | Clean render, syntax, schema, lint, secret scan, dependency lock, deterministic generation, diff. |
| Container build | Multi-stage, non-root, no-secret layers, reproducibility, required architectures, SBOM, provenance, signature, runtime smoke. |
| Pipeline | Trusted and untrusted paths, fork, OIDC, permissions, pinning, runner isolation, injection, artifact substitution, cancellation, retry. |
| Supply chain | SBOM coverage, provenance verification, signature identity, admission rejection, vulnerability triage, revocation and rebuild. |
| Kubernetes foundation | Version skew, removed APIs, control-plane access, node replacement, drain, zone assumption, add-on recovery. |
| Workloads | Startup, readiness, liveness, shutdown, rollout, rollback, OOM, disk pressure, job retry, duplicate delivery, missed schedule. |
| Security and identity | PSS or equivalent, admission bypass, effective RBAC, workload identity, denied access, break-glass, revocation, secret rotation. |
| Network and TLS | Default deny, required flows, DNS failure, certificate renewal and expiry, route conflicts, timeout, retry amplification, egress. |
| State and data | Migration, consistency, idempotency, full disk, attachment failure, replica lag, corruption, failover, deletion protection. |
| Performance and capacity | Baseline, peak, burst, soak, cold start, scaling, saturation, failover, recovery, quota and cost. |
| Observability and incident | Telemetry loss, alert fire and delivery, routing, runbook, compromised artifact, credential revocation, evidence preservation. |
| Backup and DR | Isolated restore, integrity, point in time, missing key, corrupted backup, region loss, failover, failback, measured RPO and RTO. |

### 34.1 Coverage Rules

1. Test the real production artifact or an artifact proven identical by digest, configuration, and deployment inputs.
2. Use release-like optimization, security, identity, network, storage, and policy settings.
3. Cover at least one critical synchronous journey, one asynchronous or scheduled path, one administrative path, and one recovery path where applicable.
4. Include negative and failure cases. Happy-path tests alone are insufficient.
5. Do not run destructive production experiments without explicit authorization, current backups, bounded blast radius, and rollback.
6. Re-run failed or corrected tests and preserve before-and-after evidence.

