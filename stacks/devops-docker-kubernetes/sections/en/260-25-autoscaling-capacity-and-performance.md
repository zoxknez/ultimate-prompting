## 25. Autoscaling, Capacity And Performance

**Objective:** Meet demand without unstable scaling, hidden saturation, or uncontrolled cost.

### 25.1 Required Checks

1. Establish workload model, critical paths, concurrency, throughput, latency percentiles, queue depth, burst, seasonality, growth, and dependency limits.
2. Measure CPU, memory, GC, file descriptors, connections, threads, pools, IOPS, throughput, disk, network, DNS, API rate limits, startup, and scheduling latency.
3. Audit HPA, VPA, KEDA or custom metrics for signal quality, target semantics, stabilization, scale-up and scale-down policy, missing metrics, zero state, and cooldown.
4. Audit cluster autoscaler or provider autoscaling for node groups, zones, taints, architectures, quotas, daemon overhead, PDBs, local storage, scale-from-zero, consolidation, and interruption.
5. Verify requests support scheduling and capacity planning, while limits do not create throttling, OOM loops, noisy-neighbor behavior, or false efficiency.
6. Run baseline, expected peak, burst, soak, degradation, failover, cold-start, and recovery tests in a representative environment.
7. Correlate application metrics, infrastructure saturation, user latency, errors, retries, queue age, and cost during tests.
8. Define capacity headroom, quota alerts, procurement or quota lead time, and degradation behavior before exhaustion.

### 25.2 Minimum Evidence

- Workload model and capacity assumptions.
- Load, scaling, saturation, recovery, and cost test results.
- Resource and autoscaling recommendation with measured tradeoffs.

### 25.3 Exit Criteria

1. Critical journeys meet defined SLOs at expected peak with accepted headroom.
2. Autoscaling converges without oscillation, queue runaway, unavailable capacity, or excessive cost.
3. Exhaustion and quota risks have actionable early warning and degradation plans.

