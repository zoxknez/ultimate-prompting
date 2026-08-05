## Concurrency, Virtual Threads, Reactor, And Scheduling

### Executor And Task Ownership Matrix

- Inventory every platform thread, virtual thread, executor, fork-join pool, scheduler, Reactor scheduler, timer, queue, semaphore, rate limiter, and framework-created pool.
- For each, record creator, owner, task class, queue type and bound, concurrency, rejection policy, timeout, cancellation, context propagation, metrics, and shutdown owner.
- Reject unbounded task submission or hidden common-pool use for production-critical work unless capacity and failure behavior are demonstrated.
- Verify blocking work never runs on event-loop or scheduler threads whose contract forbids blocking, and verify CPU work cannot starve I/O or control-plane tasks.
- Test saturation, rejection, interruption, cancellation, timeout, process shutdown, dependency slowdown, and memory pressure for every critical executor.

### Virtual Thread Audit

- Verify where virtual threads are enabled and whether framework, server, client, scheduler, database, logging, tracing, and native libraries are compatible with the intended model.
- Detect pinning risks from synchronized blocks, native calls, monitor contention, class initialization, file locks, and libraries that retain carrier threads.
- Do not translate cheap thread creation into unbounded downstream concurrency; retain semaphores, pool limits, rate limits, quotas, and admission control.
- Test ThreadLocal, MDC, SecurityContext, transaction context, locale, tenant context, scoped values, interruption, and cancellation behavior.
- Compare throughput, tail latency, heap, native memory, connection pressure, and failure behavior against platform-thread baselines under realistic blocking workloads.

### Reactive And WebFlux Correctness

- Map publishers, subscribers, hot and cold sources, scheduler boundaries, backpressure, buffering, replay, retries, timeouts, cancellation, and resource lifetimes.
- Detect blocking calls, hidden JDBC or filesystem work, `block()`, synchronous logging, native calls, and expensive mapping on Netty event-loop threads.
- Prove request cancellation reaches database/client work where supported and does not leave orphaned tasks or partially committed side effects.
- Verify context propagation for security, tenant, tracing, locale, transactions, and correlation data without relying on ThreadLocal semantics.
- Test slow consumers, disconnects, retry loops, large streams, empty publishers, multiple subscriptions, duplicate side effects, and mixed imperative/reactive transaction boundaries.

### Async, Scheduling, And Batch Work

- Inventory `@Async`, `TaskExecutor`, `@Scheduled`, `TaskScheduler`, Quartz, Spring Batch, integration flows, maintenance jobs, and external schedulers.
- Verify uniqueness, leader election, overlap policy, misfire policy, timezone, daylight-saving behavior, retries, checkpoints, partitioning, restartability, and duplicate prevention.
- For virtual-thread schedulers, test fixed-delay, fixed-rate, and cron semantics separately; do not assume equivalent thread behavior.
- Prove job parameters, execution identity, chunk boundaries, skip/retry policy, writer idempotency, and restart behavior after failure between read, process, write, and commit.
- Test two replicas starting the same job, long-running tasks during deployment, clock skew, missed triggers, catch-up storms, and partial external side effects.

### Context Propagation And Cancellation

- Enumerate security, tenant, request, trace, locale, transaction, feature, deadline, and idempotency context and define its authoritative carrier.
- Verify propagation across servlet async, virtual threads, custom executors, Reactor, messaging listeners, scheduled jobs, coroutines or language interop, and callbacks.
- Clear context at task completion and pool reuse; test leakage between users, tenants, requests, jobs, and tests.
- Propagate deadlines where possible and translate cancellation into bounded cleanup rather than silent abandonment.
- Do not use MDC or tracing context as an authorization source; authorization context must be explicit, authenticated, and tamper resistant.


