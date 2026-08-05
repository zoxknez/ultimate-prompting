# Core — Production Readiness Definition of Done

Mark each applicable item `CONFIRMED` / `UNVERIFIED` / `NOT_APPLICABLE` with evidence.

## Minimum (all stacks)

1. Workspace protected; uncommitted work recorded
2. Real stack/runtime/toolchain identified
3. Lifecycle/EOL checked against **current** primary sources
4. Dependency graph + lock integrity reviewed
5. Baseline install/build/test status recorded with real commands
6. Critical user/business flows mapped
7. AuthN/AuthZ (or N/A) with positive and negative cases
8. Secrets not leaked in source, logs, or report
9. P0/P1 fixed or contained with recovery path
10. P0–P2 fixes have regression tests where feasible
11. Deploy/rollback (or packaging/update) strategy documented
12. Observability sufficient for incident diagnosis (or gap listed)
13. Unverified areas explicit
14. Final diff free of unrelated churn
15. No production-ready claim without evidence

Stack overlays add domain-specific DoD items (restore tests, OTA runtimeVersion, 16 KB pages, etc.).
