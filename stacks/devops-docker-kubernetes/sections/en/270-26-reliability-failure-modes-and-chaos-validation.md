## 26. Reliability, Failure Modes And Chaos Validation

**Objective:** Validate resilience through controlled, hypothesis-driven failure experiments.

### 26.1 Required Checks

1. Create a failure-mode and effects analysis for dependencies, zones, regions, nodes, control planes, DNS, identity, KMS, registries, storage, queues, databases, observability, and third parties.
2. For every experiment define hypothesis, steady-state indicators, scope, owner, approvals, safety controls, blast radius, stop conditions, recovery steps, and evidence.
3. Test timeout, retry, backoff, jitter, circuit breaker, bulkhead, queue, rate-limit, load-shed, cache, fallback, and idempotency behavior together.
4. Inject realistic latency, errors, partial responses, network loss, stale data, clock skew, dependency unavailability, process death, node loss, and zone loss in an approved environment.
5. Verify retries do not amplify load, duplicate side effects, violate ordering, exhaust pools, or hide persistent failure.
6. Verify graceful degradation protects critical journeys and data integrity rather than only returning a healthy status.
7. Repeat corrected experiments and preserve before-and-after evidence.

### 26.2 Minimum Evidence

- Failure-mode matrix with expected and observed outcomes.
- Approved experiment definitions and captured telemetry.
- Recovery and repeat-test evidence after fixes.

### 26.3 Exit Criteria

1. Critical failure assumptions are experimentally verified within safe bounds.
2. Retries, fallbacks, and degradation preserve data and avoid cascading failure.
3. Runbooks and alerts reflect observed failure behavior.

