## 2. Current Research Baseline - Re-Check Before Every Audit

At the baseline date, primary sources indicated the following. This is a dated starting point, not permanent truth.

| Component | Baseline on 2026-08-05 | Mandatory audit action |
| --- | --- | --- |
| Kubernetes | Supported upstream lines `1.36`, `1.35`, and `1.34` | Resolve exact patch, provider support, skew, API removals, and upgrade path. |
| Docker Engine | `29.x` current release line | Verify exact engine, containerd, BuildKit, API, storage driver, and support status. |
| Helm | `4.2.x` stable line; Helm 3 in limited support window | Verify chart and plugin compatibility before moving major versions. |
| SLSA | Specification `1.2` | Map actual build provenance and isolation to the applicable requirements. |
| Pod Security | Pod Security Standards and built-in Pod Security Admission | Determine enforce, audit, and warn posture per namespace and exception. |
| GitHub Actions where used | OIDC, artifact attestations, least privilege, immutable action references | Verify trust boundaries, fork behavior, permissions, runner isolation, and SHA pinning. |
| NIST SSDF | SP 800-218 version 1.1 is final; newer revisions may be draft | Use final requirements unless the organization intentionally adopts a verified draft. |

