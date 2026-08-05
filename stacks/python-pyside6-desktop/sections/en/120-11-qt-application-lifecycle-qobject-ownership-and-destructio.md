## 11. Qt Application Lifecycle, QObject Ownership, And Destruction

### 11.1 Audit Scope

1. Map `QApplication` or `QGuiApplication` creation, singleton initialization, startup phases, splash, dependency construction, event-loop entry, shutdown, and restart.
2. For every critical QObject, record creator, parent, Python reference owner, thread affinity, consumers, destruction trigger, `deleteLater` behavior, and shutdown order.
3. Identify ownership mismatches between Python garbage collection and Qt parent-child deletion, dangling wrappers, resurrected references, and use-after-delete risks.
4. Review top-level windows, dialogs, tray icons, timers, network objects, threads, models, delegates, actions, and native resources for deterministic cleanup.
5. Inspect application state changes, session restore, suspend/resume, logout, user switching, and operating-system termination paths.
6. Distinguish normal close, hide-to-tray, forced termination, crash, update restart, installer shutdown, and operating-system logout semantics.

### 11.2 Required Verification

1. Instrument creation, affinity, signal connections, destruction, finalization, and shutdown for representative critical objects.
2. Test repeated open/close, login/logout, workspace switch, window recreation, tray restore, update restart, and application exit for leaks and stale callbacks.
3. Use weak references, `QPointer`, destroyed signals, debug assertions, and platform tools where appropriate to prove lifetime assumptions.
4. Verify that shutdown stops new work, cancels or drains existing work, flushes critical data, releases locks and devices, and exits within a defined deadline.
5. Reject fixes that merely keep objects alive globally or call garbage collection without correcting ownership.

