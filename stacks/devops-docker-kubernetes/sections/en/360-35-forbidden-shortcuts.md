## 35. Forbidden Shortcuts

1. Do not equate a green pipeline, successful plan, synced GitOps application, ready pod, or healthy dashboard with production readiness.
2. Do not deploy mutable tags, unverified artifacts, unreviewed manifests, or locally rebuilt production binaries.
3. Do not put secrets in Docker `ARG` or `ENV`, Git, images, manifests, state, plans, logs, command lines, or chat output.
4. Do not weaken TLS, certificate verification, RBAC, admission, Pod Security, network policy, signatures, scans, tests, probes, resource controls, audit logs, backup, or deletion protection to pass a check.
5. Do not grant cluster-admin, cloud-admin, wildcard, Docker socket, privileged, hostPath, or long-lived credential access as a convenience fix.
6. Do not run broad `apply`, `destroy`, `delete`, `prune`, `reconcile`, `restart`, `drain`, `rotate`, or `failover` actions without exact scope, approval, observation, and rollback.
7. Do not assume Helm rollback, Git revert, image rollback, Terraform state restore, or cluster snapshot restores external data or side effects.
8. Do not close a backup finding because backup jobs are green. Require isolated restore and integrity evidence.
9. Do not accept scanner severity, compliance badge, benchmark score, or policy pass as proof that the real risk is resolved.
10. Do not optimize cost by silently removing redundancy, observability, retention, support, security, capacity headroom, or recovery options.
11. Do not recommend a major platform migration without comparing risk reduction, migration risk, operating model, skill, cost, support, rollback, and alternatives.
12. Do not issue `ready` when critical live state, production artifact identity, restore evidence, or operational ownership remains unverified.

