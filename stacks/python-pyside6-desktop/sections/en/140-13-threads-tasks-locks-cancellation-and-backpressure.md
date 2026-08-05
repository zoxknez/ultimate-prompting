## 13. Threads, Tasks, Locks, Cancellation, And Backpressure

### 13.1 Audit Scope

1. Inventory `QThread`, worker-object patterns, `QThreadPool`, `QRunnable`, Python threads, executors, timers, queues, locks, semaphores, conditions, and background services.
2. Record owner, start condition, concurrency limit, input queue, cancellation contract, deadline, result delivery, exception path, join/drain behavior, and shutdown owner.
3. Identify subclassed-QThread misuse, work executing on the wrong thread, QObject moves after parenting, direct cross-thread UI access, and blocking queued deadlocks.
4. Review lock ordering, lock scope, callbacks under locks, signal emission under locks, database connections per thread, and native-library thread safety.
5. Check unbounded task submission, queue growth, large retained payloads, priority inversion, starvation, retry storms, and user-triggered concurrency amplification.
6. Distinguish cancellation request from completed cancellation and define behavior for non-cancellable native, file, database, device, and network work.

### 13.2 Required Verification

1. Run burst, sustained, cancellation, timeout, shutdown, worker-crash, queue-full, and dependency-slowdown scenarios with thread and queue instrumentation.
2. Use deterministic synchronization tests, faulthandler dumps, platform stack capture, and stress repetition to investigate races and deadlocks.
3. Verify bounded queues, admission control, progress coalescing, load shedding, retry budgets, and user-visible degraded states.
4. Prove that every background exception is observed, classified, reported, and either recovered or causes a controlled state transition.
5. Confirm that no worker, thread, timer, lock, device handle, or database connection survives logout, workspace switch, update restart, or shutdown unintentionally.

