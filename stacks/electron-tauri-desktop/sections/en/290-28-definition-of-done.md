## 28. Definition Of Done

1. Workspace and user/signing data were protected; repository state and audit boundaries are recorded.
2. All relevant source, generated, dependency, build, package, signing, installer, updater, store, and runtime assets are inventoried.
3. Actual Electron/Tauri and embedded/runtime/tool versions are verified; support and compatibility are checked against current primary sources.
4. Clean locked restore/build, relevant static checks, tests, package generation, and artifact inspection are recorded with real commands and exit codes.
5. Architecture, process, window/webview, origin, privilege, IPC/command, local service, data, and update maps are complete.
6. Every material claim has an evidence status and level. Suspicions are separated from confirmed findings.
7. Every P0/P1 has evidence, root cause, impact, containment, repair, regression proof, release impact, rollback, and owner.
8. Applicable P2 findings have targeted remediation or a prioritized, testable plan. P3 work is not presented as a production blocker without cause.
9. Electron security settings or Tauri capabilities are verified in the packaged application with positive and negative tests.
10. Authentication, resource authorization, account/tenant isolation, session cleanup, secret storage, and privileged actions are verified.
11. Critical local writes, migrations, synchronization, and external side effects are safe under duplicate, concurrent, interrupted, and crash conditions.
12. Files, URLs, protocols, imports, exports, archives, downloads, external-open, local listeners, sidecars, and devices are constrained and tested.
13. Build and package supply chain, SBOM/provenance, artifact identity, signing, notarization, key custody, and revocation are verified.
14. Fresh install, upgrade matrix, repair, interrupted update, rollback/recovery, and uninstall are tested or clearly blocked with exact reasons.
15. Performance and resource claims are based on measurement; accessibility and localization are tested in packaged builds.
16. Observability and incident artifacts can identify exact version/channel/platform/process and diagnose critical failure without exposing sensitive data.
17. CI/CD gates, artifact promotion, staged rollout, abort, emergency release, rollback, and compromised-key procedures are documented and exercised where required.
18. Final diff is narrow, reviewable, free of unrelated changes, and includes necessary tests and documentation.
19. Final report contains exact commands, evidence, artifacts, hashes, changes, tests, blockers, residual risk, owners, and authoritative sources.
20. If any applicable condition is unmet, the application is not fully production-ready and the exact blocking condition is stated.

