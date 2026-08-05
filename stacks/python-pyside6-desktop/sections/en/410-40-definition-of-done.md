## 40. Definition Of Done

1. The current repository, environment, toolchain, package, installed application, runtime, and production-like state have been distinguished explicitly.
2. All critical journeys and invariants have evidence-backed ownership, failure behavior, recovery, and tests.
3. Every confirmed P0-P2 finding has root cause, minimal complete fix or approved plan, regression proof, release impact, and owner.
4. No critical claim relies only on source inspection when packaged, installed, runtime, upgrade, rollback, or restore evidence is required.
5. All supported platform and architecture combinations have current support evidence or are explicitly removed from claims.
6. Concurrency, QObject lifetime, cancellation, shutdown, account switching, duplicate actions, and stale results are safe.
7. Local data and external side effects remain consistent under duplicate, concurrent, interrupted, and crash conditions.
8. Package contents, signatures, installer, updater, and installed search paths resist tampering and hijacking.
9. Fresh install, upgrade, repair, rollback/forward repair, uninstall, backup, and restore are operationally usable.
10. Performance and accessibility conclusions are measured on packaged builds and representative hardware.
11. Observability and support evidence are sufficient, correlated, bounded, and privacy-safe.
12. CI/CD, signing, promotion, rollout, abort, incident, revocation, and trusted rebuild controls are reviewable and tested where material.
13. All commands, skipped checks, failures, artifacts, hashes, screenshots, traces, and residual risks are recorded truthfully.
14. Unrelated files and user work are preserved; the final change set is minimal and reviewable.
15. The final verdict follows the evidence ceiling and does not overstate security, compatibility, testing, or recovery.

