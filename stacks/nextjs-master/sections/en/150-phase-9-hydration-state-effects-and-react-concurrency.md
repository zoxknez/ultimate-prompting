## Phase 9 - Hydration, State, Effects, And React Concurrency

Prove deterministic rendering, correct state ownership, safe effects, and stable behavior under concurrent rendering and navigation.

### Audit Requirements

- Detect hydration differences caused by time, randomness, locale, timezone, browser APIs, invalid HTML, data races, or flag drift.
- Review duplicated state, derived state, stale closures, effect dependencies, subscriptions, timers, observers, abort, and cleanup.
- Verify Suspense, transitions, optimistic updates, useActionState, useOptimistic, and error recovery preserve invariants.
- Prevent double-submit, stale overwrite, lost optimistic rollback, duplicate notification, and navigation-triggered replay.
- Audit context scope, external stores, hydration snapshots, selector stability, and subscription behavior.
- Use React Compiler only with measured compatibility, explicit rollout, and a disable path.

### Required Evidence

- Hydration warning inventory with deterministic reproduction.
- State and effect ownership map for critical flows.
- Before/after rendering, memory, interaction, and bundle metrics.
- List of optimistic mutations and authoritative reconciliation paths.

### Mandatory Failure And Acceptance Tests

- Repeat hydration across locales, timezones, clocks, browsers, and flag states.
- Submit rapidly, navigate away, abort, return, and verify one authoritative result.
- Resolve concurrent requests out of order and block stale overwrite.
- Canary React Compiler and prove correctness, performance, memory, and debugging acceptance.

