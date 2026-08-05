## 14. State Management And Reactive Consistency

Audit the actual state machine whether the project uses Provider, Riverpod, Bloc, Cubit, Redux, MobX, Signals, GetX, ValueNotifier, custom controllers, or mixed approaches.

- Inventory source of truth, derived state, ephemeral UI state, persisted state, server state, cache state, navigation state, and platform state.
- Verify event ordering, stale-result suppression, duplicate request coalescing, optimistic update rollback, pagination, refresh, retry, and account switching.
- Test simultaneous user actions, repeated taps, route changes during requests, background/foreground transitions, reconnect, logout, and tenant switch.
- Verify provider/bloc/controller scope, disposal, auto-dispose, keep-alive, restoration, nested overrides, test overrides, and cross-route ownership.
- Detect inconsistent loading/error/empty/success models, hidden stale data, partial failures, infinite refresh loops, duplicate listeners, and notification storms.
- Ensure sensitive state is cleared on logout, account removal, tenant change, app reset, device compromise response, and retention expiry.
- Measure rebuild granularity and selector behavior; optimize only after profiling confirms avoidable work.
- Require deterministic state-transition tests for critical flows, including invalid, interrupted, duplicated, reordered, and replayed events.

