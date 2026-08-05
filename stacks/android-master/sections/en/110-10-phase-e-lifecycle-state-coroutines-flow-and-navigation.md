## 10. Phase E - Lifecycle, State, Coroutines, Flow And Navigation

### 10.1 Coroutines And Flow

1. Find `GlobalScope`, unmanaged scopes, orphan jobs, custom scopes without owners, and incorrect supervisor behavior.
2. Verify dispatchers are injectable where testing or policy requires it.
3. Detect disk, database, network, JSON, crypto, bitmap, or blocking work on the main thread.
4. Verify cancellation propagates through repositories, use cases, network calls, database work, players, and UI state production.
5. Check exception handling, `CoroutineExceptionHandler`, `supervisorScope`, `async`, structured concurrency, and lost failures.
6. Verify `stateIn`, `shareIn`, replay, started policy, and scope do not cause leaks, stale data, hidden background work, or duplicated upstream subscriptions.
7. Verify lifecycle-aware collection using appropriate APIs such as `repeatOnLifecycle` or `collectAsStateWithLifecycle`.
8. Check `flowOn`, `withContext`, channel capacity, buffer, conflation, backpressure, and hot-flow ownership.
9. Test rapid input, stale search, cancellation, retry, concurrent refresh, double tap, rotation, backgrounding, and process recreation.
10. Use `flatMapLatest`, mutexes, actors, transactions, idempotency, or serialization only where the actual concurrency model requires them.
11. Verify tests use deterministic schedulers and do not rely on real delays.

### 10.2 ViewModel, Saved State And Process Death

1. Prefer screen or destination-level ViewModels when their lifecycle benefits apply.
2. Verify ViewModels do not retain Activity, Fragment, View, NavController, mutable Context, or UI-only objects.
3. Distinguish durable domain data, screen UI state, transient UI events, and navigation effects.
4. Verify state can be reconstructed after process death without silently relying on in-memory singletons.
5. Use `SavedStateHandle` only for small restorable state and identifiers, not as a substitute for durable storage.
6. Verify one-time events are not lost, duplicated, or replayed after recreation.
7. Test configuration changes, locale, theme, font scale, multi-window, background kill, and restore.
8. Verify loading, empty, content, stale, partial, retry, permission-denied, offline, and terminal error states.
9. Prevent double submission and inconsistent UI during long-running writes.

### 10.3 Navigation, Deep Links And Back Behavior

1. Map every destination, graph, nested graph, start destination, dynamic feature, and external entry point.
2. Verify route arguments are typed, validated, size-bounded, and do not carry sensitive objects.
3. Verify deep links validate scheme, host, path, query, identity, tenant, and authorization before displaying or mutating data.
4. Verify untrusted intents cannot skip authentication, parental gates, onboarding, payment, consent, or required state.
5. Test cold-start, warm-start, existing-task, notification, app-link, share, restore, and multiple-deep-link scenarios.
6. Verify back, predictive back, up navigation, task behavior, dialogs, sheets, nested navigation, and state restoration.
7. Prevent duplicate destinations and duplicate side effects from repeated navigation events.
8. Verify app links and Digital Asset Links from actual deployed hosts where applicable.
9. Verify sensitive routes do not leak data through URLs, logs, recents, screenshots, or analytics.

