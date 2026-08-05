## 28. Production Readiness Definition Of Done

The application is production-ready only when all applicable items are evidenced:

1. Uncommitted work, production data, signing material, and secrets were protected during the audit.
2. Actual modules, variants, flavors, manifests, dependencies, SDKs, native libraries, and release paths are inventoried.
3. Android Studio, AGP, Gradle, JDK, Kotlin, SDK, NDK, KSP, Compose, and plugin versions are compatible and reproducible.
4. Debug and release baselines pass for the required variants, with real command evidence.
5. Release uses intended signing, endpoints, flags, R8, resource shrinking, mappings, native symbols, and policy declarations.
6. Application ID, signing continuity, version codes, database migrations, and update paths are safe.
7. 16 KB compatibility is verified for every packaged native library or formally `NOT_APPLICABLE`.
8. No applicable P0 remains open.
9. P1 findings are fixed or formally contained with owner, deadline, monitoring, and recovery.
10. Critical happy, negative, offline, retry, cancellation, lifecycle, process-death, account, migration, and rollback journeys pass.
11. Identity, session, authorization, deep links, exported components, WebViews, files, permissions, and sensitive data are protected.
12. Concurrency, transactions, idempotency, synchronization, and conflict behavior preserve data invariants.
13. Background work, notifications, media, device APIs, and battery use are correct under platform restrictions.
14. Accessibility, localization, adaptive layout, TV or other target-device behavior pass the defined matrix.
15. Startup, jank, memory, ANR, energy, and critical performance budgets are measured and acceptable.
16. Unit, integration, UI, instrumented, migration, release, and benchmark tests cover the highest risks and are sufficiently deterministic.
17. Crash mapping, native symbols, telemetry, alerts, feature flags, kill switches, runbooks, staged rollout, and rollback are tested.
18. Current Google Play and applicable legal or sector requirements are reviewed, with unresolved specialist items explicitly blocking where necessary.
19. Residual risk is explicit and accepted by an authorized owner.
20. No material area is declared safe solely because it was not tested.

If any applicable blocking item is incomplete, state:

> Not fully production-ready.

Then list the exact blocking conditions.

