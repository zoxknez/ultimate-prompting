## 18. Futures, Cancellation, Concurrency, And Race Conditions

Dart is single-threaded per isolate, but applications still have asynchronous races, native concurrency, multiple isolates, and distributed conflicts.

- Trace every critical Future chain, callback, completer, timer, microtask, post-frame callback, retry, debounce, throttle, and cancellation boundary.
- Detect use-after-dispose, setState after dispose, stale response overwrite, duplicate submission, overlapping refresh, lost update, double navigation, and repeated side effects.
- Verify cancellation or stale-result suppression when route, query, account, tenant, device, locale, filter, or session changes.
- Audit mutex, lock, semaphore, queue, single-flight, lease, idempotency-key, optimistic concurrency, version, and compare-and-set strategies where needed.
- Verify UI-level deduplication does not replace server-side idempotency and authorization for payments, orders, mutations, uploads, and destructive actions.
- Test rapid repeated input, slow network, timeout, reconnect, retry, app pause, clock change, token refresh, duplicate push, and old/new version overlap.
- Preserve correlation IDs and operation state across retries so telemetry distinguishes one logical operation from duplicate executions.
- Require deterministic concurrency tests with controllable clocks, fake transports, barriers, and fault injection for material races.

