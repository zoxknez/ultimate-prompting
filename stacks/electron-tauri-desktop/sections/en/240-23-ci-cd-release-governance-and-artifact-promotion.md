## 23. CI/CD, Release Governance, And Artifact Promotion

1. Map workflows from pull request to test, package, sign, notarize, publish, promote, store upload, update manifest, rollout, pause, rollback, and incident release.
2. Separate untrusted code execution from privileged release jobs. Require reviewed commits, protected environments, approvals, and branch/tag policy.
3. Use matrix builds for supported platforms/architectures and record which steps run natively, cross-compile, or use remote builders.
4. Promote the same immutable artifact through verification, signing where ordering permits, staging, and release. Explain every unavoidable transformation.
5. Verify package contents, fuses/capabilities, SBOM, provenance, signatures, notarization, installer metadata, malware/reputation scans, and update metadata before promotion.
6. Protect release version allocation from races and duplicate tags. Ensure application, package, installer, store, and feed versions remain consistent.
7. Require release notes with security/privacy/migration/update impact, known issues, support changes, and rollback conditions.
8. Define automated and manual release gates, abort thresholds, canary/phased cohorts, soak periods, owner, and emergency stop.
9. Retain exact artifacts, symbols, source maps, manifests, logs, signatures, hashes, approvals, and environment identity for the support and incident window.
10. Test the release pipeline using non-production signing/update/store targets and periodically exercise emergency release and rollback.
11. Do not allow the renderer/frontend, a pull-request job, or a general developer token to publish update metadata or signed artifacts.
12. Record residual manual steps and make them two-person, checklist-driven, auditable, and recoverable.

