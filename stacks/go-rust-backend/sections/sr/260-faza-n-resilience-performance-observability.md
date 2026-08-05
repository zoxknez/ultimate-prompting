## Faza N - Resilience, Performance, Observability

Timeout/retry/jitter/cancellation dosledni kroz inbound, DB, HTTP i job. Ne retry-uj non-idempotent write. Bounded concurrency prema kapacitetu dependency-ja.

Performance: merenje (p95/p99, CPU, memory, alloc, GC za Go, scheduler, lock contention, I/O, query). Benchmark i profiler dokazi. Ne optimizuj bez profilera. Microbenchmark nije end-to-end dokaz.

Observability: structured log, correlation/trace ID, metrics cardinality, tracing, health/readiness/liveness razdvojeni, dashboard, alert, runbook. Ne loguj tajne/PII.

