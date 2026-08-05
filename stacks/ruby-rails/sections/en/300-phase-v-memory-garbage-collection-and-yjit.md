## Phase V - Memory, Garbage Collection And YJIT

- Measure RSS, heap slots, allocation rate, retained objects, old objects, fragmentation, native memory and copy-on-write efficiency.
- Inspect caches, class loaders, autoloading, query cache, thread locals, subscriptions, callbacks, string duplication and large response buffers.
- Compare GC behavior under cold, steady, burst, queue-heavy and memory-pressure workloads.
- Benchmark YJIT enabled and disabled using the same release artifact and workload; include warmup, memory headroom and rollback.
- Capture heap or object evidence safely and ensure dumps, traces and profiler output do not leak secrets or customer data.

