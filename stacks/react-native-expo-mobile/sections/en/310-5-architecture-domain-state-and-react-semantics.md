## 5. Architecture, Domain, State, And React Semantics

### 5.1 Domain And Ownership
- Map features, domain rules, repositories, API clients, native services, navigation, state stores, caches, persistence, background workers, and observability owners.
- State critical invariants explicitly and identify where they are enforced on client, native layer, backend, database, and store/update systems.
- Detect duplicated authority among React state, query cache, local database, native singleton, navigation params, persistent storage, and backend state.
- Define ownership and cleanup for subscriptions, listeners, timers, sockets, tasks, native handles, media sessions, sensors, and background registrations.
- Separate business policy from UI convenience and never rely on hidden, disabled, or unmounted UI as authorization.
- Document degraded, offline, logged-out, suspended, process-restored, and partially migrated states.

### 5.2 State Management And Server State
- Audit Redux, Zustand, MobX, Recoil, Jotai, Context, custom stores, and query libraries according to actual usage rather than ideology.
- Prove cache keys include user, tenant, locale, permission, environment, filter, and version dimensions when required.
- Verify login, logout, account switch, tenant switch, token refresh, app restart, OTA update, and native update clear or migrate state safely.
- Audit optimistic mutations for conflict detection, rollback, idempotency, retry, reconciliation, and user-visible uncertainty.
- Detect stale closures, stale selectors, accidental global singletons, non-serializable state, unbounded history, and persistence of transient secrets.
- Test parallel screens, multiple tabs, background refresh, duplicate requests, and out-of-order responses.

### 5.3 React Rendering And Concurrent Features
- Inspect component identity, key stability, memoization, context fan-out, selector granularity, expensive render work, and unnecessary bridge or JSI calls.
- Audit every effect for dependency correctness, cleanup, idempotency, stale callback handling, abort behavior, and Strict Mode sensitivity.
- Verify Suspense, transitions, optimistic state, deferred work, and error boundaries under navigation, retry, backgrounding, and process recreation.
- Do not infer performance from render counts alone; correlate JS work, UI-thread work, Fabric commits, layout, native calls, GPU frames, and user-perceived latency.
- Test rapid mount-unmount cycles, screen replacement, nested navigators, list recycling, animation interruption, and stale asynchronous completion.
- Treat React Compiler or automatic memoization as a measured migration, not a substitute for correct ownership and state design.

