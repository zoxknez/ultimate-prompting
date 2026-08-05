## Phase U - Threads, Fibers, Ractors And Shared State

- Inventory every thread pool, fiber scheduler, executor, timer, reactor, actor or Ractor and assign ownership, capacity and shutdown rules.
- Audit class variables, constants containing mutable objects, singleton caches, thread locals, CurrentAttributes and request-store data.
- Verify context cleanup across requests, jobs, retries, Action Cable connections, asynchronous tasks and account or tenant switching.
- Test lock order, condition variables, queue bounds, cancellation, exception propagation, orphan work and shutdown deadlines.
- Treat Fiber scheduler compatibility as library-specific and test blocking database, filesystem, DNS, TLS and native-extension operations.
- Use Ractors only with proven gem, data-sharing, serialization, error and deployment compatibility.

