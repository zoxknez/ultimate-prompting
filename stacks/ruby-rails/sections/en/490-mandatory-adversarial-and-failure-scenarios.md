## Mandatory Adversarial And Failure Scenarios

### S1

Two concurrent requests perform the same critical mutation.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S2

The client retries after the database committed but before the response arrived.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S3

Authorization context changes while a stale page, job or websocket remains active.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S4

A tenant identifier is changed in a route, nested parameter, GlobalID, cache key or job argument.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S5

The database becomes slow or unavailable while web and jobs continue receiving work.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S6

The cache or Redis backend loses data, evicts keys or returns stale values.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S7

A worker crashes before, during or after an external side effect.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S8

The same job is delivered twice, out of order or after its resource was deleted.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S9

An old worker processes a job enqueued by the new release.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S10

A new worker processes a payload created by the old release.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S11

A deployment terminates a web, Cable or job process with in-flight work.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S12

A migration partially completes, times out or is retried.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S13

A direct upload, file parser or image processor receives malicious or oversized content.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S14

A webhook is replayed, reordered, delayed or signed with a rotated key.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S15

A secret, cookie key, database credential or deployment token is compromised.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S16

The system experiences a burst that saturates threads, pools, queues or memory.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S17

Clock skew or DST affects token expiry, recurring work or business dates.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S18

An isolated restore starts with old data while external systems contain newer effects.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S19

Rollback occurs after a cache, job payload, encrypted field or schema format changed.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

### S20

A compromised gem or base image requires revocation and trusted rebuild.

- Required evidence: setup, exact steps, observed result, invariant, telemetry, cleanup and residual risk.

