## 12. Signals, Slots, Events, Reentrancy, And UI State

### 12.1 Audit Scope

1. Inventory critical signal-slot connections, connection types, lambdas/closures, queued arguments, event filters, custom events, and direct method calls across boundaries.
2. Identify duplicate connections, connection leaks, stale receivers, captured mutable state, retained objects, silent signature mismatch, and overloaded-signal ambiguity.
3. Review direct, queued, blocking queued, and auto connection behavior with actual sender and receiver thread affinity.
4. Assess nested event loops from modal dialogs, `processEvents`, synchronous waits, drag/drop, menus, native dialogs, and reentrant callbacks.
5. Map UI state transitions, enabled/disabled controls, focus, selection, progress, cancellation, optimistic changes, errors, retries, and rollback.
6. Ensure user-triggered actions cannot start duplicate non-idempotent work through double-click, shortcut, menu, tray, deep link, or restored state.

### 12.2 Required Verification

1. Log and test connection establishment, delivery thread, ordering, duplicate delivery, receiver destruction, disconnect, and shutdown.
2. Force rapid repeated input, modal reentrancy, delayed completion, out-of-order completion, cancellation, window closure, and account switch.
3. Verify that UI updates occur only on the GUI thread and that stale results are rejected using operation identity, generation, or current-context checks.
4. Replace `processEvents` or synchronous GUI waits with explicit asynchronous state machines unless a narrowly justified, tested use remains.
5. Prove that action gating, idempotency, and domain constraints work independently of button disabled state.

