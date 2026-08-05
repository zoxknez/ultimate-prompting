## 22. Phase Q - CI/CD, Supply Chain And Release Governance

1. Map pull-request checks, branch protections, required reviews, build runners, caches, artifacts, signing, deployment, and Play track promotion.
2. Verify CI uses pinned actions, images, plugins, toolchains, and checksums where practical.
3. Separate untrusted pull-request execution from secrets and signing.
4. Verify artifacts are produced once and promoted rather than rebuilt differently for each environment where feasible.
5. Verify source revision, dependency state, toolchain, provenance, signing identity, and artifact digest are traceable.
6. Scan source and dependencies with appropriate tools, but confirm findings and avoid leaking proprietary code.
7. Verify SBOM or dependency inventory, license review, vulnerability response, and update ownership.
8. Verify signing and Play credentials are least-privileged, short-lived where possible, audited, and unavailable to forks.
9. Verify release notes, versioning, migrations, support readiness, policy declarations, and rollback plan are reviewed before promotion.
10. Verify tests cannot be silently skipped by task aliases, conditional CI logic, or changed paths.
11. Check remote and local Gradle caches for secret leakage and cross-branch contamination.
12. Verify dependency bots do not merge incompatible upgrades without project tests.

