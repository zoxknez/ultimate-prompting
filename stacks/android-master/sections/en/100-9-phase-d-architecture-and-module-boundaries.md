## 9. Phase D - Architecture And Module Boundaries

1. Map UI, presentation, domain, data, platform, network, storage, feature, and shared layers.
2. Confirm dependency direction from code and Gradle, not package names.
3. Prefer separation of concerns, single source of truth, and unidirectional data flow where they improve correctness.
4. Do not introduce a domain layer or Clean Architecture ceremony without demonstrated complexity or reuse.
5. Verify UI components do not access databases, network clients, content providers, or mutable singletons directly without justified design.
6. Verify repositories own data-source coordination and expose explicit behavior.
7. Check module boundaries for cycles, leakage of implementation types, broad shared modules, duplicate models, and unstable public APIs.
8. Verify DI scopes match Android lifetimes and do not retain activities, views, contexts, players, or accounts incorrectly.
9. Identify service locators, mutable global state, hidden singleton caches, static callbacks, and process-wide state.
10. Verify feature boundaries support testing, ownership, build performance, and release behavior rather than only directory aesthetics.
11. Map critical state transitions and persistence boundaries.
12. Record architecture exceptions and their rationale instead of forcing uniformity.

