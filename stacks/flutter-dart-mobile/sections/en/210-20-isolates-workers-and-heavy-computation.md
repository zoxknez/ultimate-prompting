## 20. Isolates, Workers, And Heavy Computation

Use isolation deliberately and verify message, memory, and lifecycle costs.

- Inventory `Isolate.spawn`, `Isolate.run`, `compute`, background plugin entrypoints, native worker threads, and web workers.
- Verify entrypoint reachability, tree-shaking annotations where required, initialization, plugin registration, dependency availability, and platform restrictions.
- Audit message serialization, TransferableTypedData, copying cost, object ownership, protocol versioning, malformed messages, and shutdown.
- Prevent isolates from using unsupported UI bindings, stale credentials, wrong tenant context, uninitialized storage, or non-isolate-safe native resources.
- Define cancellation, timeout, progress, crash propagation, restart, queue limits, and cleanup for long-running work.
- Profile whether isolation improves responsiveness after startup, copy, scheduling, and memory overhead.
- On web, verify worker availability, CSP, asset paths, browser support, fallback, and cross-origin isolation requirements.
- Require load, cancellation, termination, malformed-message, and repeated-start/stop tests.

