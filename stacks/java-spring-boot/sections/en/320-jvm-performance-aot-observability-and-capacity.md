## JVM Performance, AOT, Observability, And Capacity

### JVM, GC, Memory, And Native Resources

- Capture JVM vendor/build, heap sizing mode, container awareness, GC, pause targets, region settings, direct memory, metaspace, code cache, thread stacks, native libraries, and relevant flags.
- Measure allocation rate, live set, promotion, pause distribution, concurrent-cycle behavior, safepoints, class loading, code cache, direct buffers, file descriptors, sockets, and native memory.
- Investigate leaks with heap histograms, dumps, JFR, native memory tracking, allocation profiles, reference chains, classloader retention, ThreadLocal retention, and cache ownership.
- Test memory limits, OOM variants, heap-dump behavior, disk capacity, restart loops, graceful degradation, and whether sensitive data appears in dumps or diagnostics.
- Do not tune flags before establishing workload, baseline, bottleneck, hypothesis, controlled experiment, and rollback criteria.

### Latency, Throughput, And Capacity

- Define workload models by endpoint, message, job, tenant, payload, dataset, concurrency, arrival pattern, dependency behavior, and cache state.
- Measure p50, p95, p99, and maximum latency, throughput, errors, saturation, queue wait, pool wait, CPU, memory, GC, network, disk, and downstream pressure.
- Run cold-start, warm, burst, sustained, soak, failover, recovery, retry-storm, noisy-neighbor, large-payload, and degraded-dependency tests.
- Separate server processing from queueing, network, proxy, serialization, database, broker, cache, and client time using traces and coordinated measurements.
- Establish safe capacity, headroom, autoscaling signals, scale-up delay, scale-down safety, admission thresholds, load-shedding policy, and operator actions.

### AOT And Native Image

- Treat JVM, CDS, layered JAR, executable JAR, WAR, and GraalVM native image as distinct runtime products with separate compatibility and performance evidence.
- Verify AOT processing, reachability metadata, reflection, resources, proxies, serialization, JNI, dynamic class loading, agents, locales, charsets, TLS, and service loading.
- Test every supported profile and optional integration in native mode; a successful minimal native build does not prove production feature coverage.
- Compare startup, RSS, throughput, tail latency, build time, binary size, observability, debugging, patching, and failure behavior against the JVM artifact.
- Preserve a tested rollback path between native and JVM artifacts when operational policy allows both.

### Observability And Health Model

- Define release, environment, service, instance, tenant-safe, request, job, message, schema, and dependency attributes consistently across logs, metrics, and traces.
- Instrument critical business transitions, queueing, retries, timeouts, pool waits, transaction outcomes, outbox lag, consumer lag, cache behavior, and recovery actions.
- Control metric cardinality, trace sampling, baggage, payload capture, stack traces, and log volume; redact secrets and personal data before export.
- Separate liveness, readiness, startup, dependency, degradation, data freshness, backlog, and business health; no single green endpoint proves service correctness.
- Tie every actionable alert to an owner, severity, SLO or invariant, dashboard, evidence query, runbook, escalation, and verified recovery action.


