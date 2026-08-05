## 18. Phase M - Performance, Memory, Startup, Energy And Stability

1. Establish device, build, thermal, network, and data baselines before measurement.
2. Measure cold, warm, and hot startup, TTID, TTFD, first useful content, and startup initialization ownership.
3. Inspect App Startup initializers, content providers, DI graph creation, SDK initialization, disk I/O, and synchronous network or crypto at startup.
4. Use StrictMode, Perfetto, CPU, memory, network, energy, layout, Compose, and database tools as appropriate.
5. Detect Activity, Fragment, View, Compose, Context, receiver, callback, coroutine, bitmap, cursor, WebView, player, surface, and native leaks.
6. Measure heap growth, GC, allocation churn, bitmap pressure, native memory, file descriptors, threads, and decoder resources.
7. Test repeated navigation, rotation, playback, downloads, search, account switching, and background cycles.
8. Measure frame timing and jank on critical scrolling, animation, transition, keyboard, and TV focus journeys.
9. Verify image loading dimensions, cache policy, transformations, prefetch, cancellation, and OOM behavior.
10. Verify database, serialization, parsing, diffing, sorting, filtering, and formatting do not block critical threads.
11. Measure battery, wakeups, alarms, network, location, Bluetooth, sensors, FGS, and media locks.
12. Verify ANR sources including main-thread blocking, lock contention, binder calls, broadcast receivers, services, and input dispatch.
13. Use release-like builds and representative devices. Do not infer production performance from a fast development machine.
14. Define measurable budgets and acceptance gates for critical journeys.

