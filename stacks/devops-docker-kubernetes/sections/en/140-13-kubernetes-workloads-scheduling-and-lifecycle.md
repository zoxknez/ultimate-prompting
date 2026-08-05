## 13. Kubernetes Workloads, Scheduling And Lifecycle

**Objective:** Ensure workloads start, stop, scale, update, and fail predictably.

### 13.1 Required Checks

1. Audit Deployments, StatefulSets, DaemonSets, Jobs, CronJobs, custom workloads, revisions, selectors, ownership, update strategies, and history limits.
2. Separate startup, readiness, liveness, and gRPC probe semantics. Verify failure thresholds, timeouts, dependency behavior, and probe cost.
3. Set measured requests and justified limits for CPU, memory, ephemeral storage, huge pages, GPUs, and extended resources.
4. Verify terminationGracePeriodSeconds, preStop, signal handling, connection draining, finalizers, job interruption, and shutdown ordering.
5. Audit affinity, anti-affinity, topology spread, taints, tolerations, priorities, preemption, PDBs, and capacity assumptions together.
6. Test rolling update, rollback, unavailable dependency, slow startup, OOM, disk pressure, node drain, duplicate delivery, job retry, and missed schedule behavior.
7. Ensure init containers, sidecars, ephemeral containers, and service-mesh injection do not hide lifecycle, security, or resource failures.

### 13.2 Minimum Evidence

- Rendered and live workload configuration with effective defaults.
- Measured resource, startup, shutdown, update, and disruption results.
- Workload failure matrix including Jobs and stateful workloads.

### 13.3 Exit Criteria

1. Critical workloads have correct probes, resources, shutdown, scheduling, and disruption behavior.
2. Rollout and rollback complete within defined safety and availability bounds.
3. Retry and scheduling behavior does not create uncontrolled duplication, loss, or resource exhaustion.

