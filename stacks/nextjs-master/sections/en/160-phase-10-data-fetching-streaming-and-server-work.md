## Phase 10 - Data Fetching, Streaming, And Server Work

Map every server read, its identity inputs, consistency, lifecycle, timeout budget, cache, and rendering consequence.

### Audit Requirements

- Inventory fetch, ORM/database calls, GraphQL, SDKs, filesystem reads, internal HTTP, and service access.
- For each read record actor, tenant, parameters, authorization, consistency, cache, timeout, retry, cancellation, and fallback.
- Detect waterfalls, duplicate fetches, hidden layout dependencies, metadata duplication, unbounded fan-out, and per-row calls.
- Use parallelism only with explicit downstream capacity, cancellation, ordering, and partial-failure semantics.
- Review Suspense and streaming for useful progress, stable layout, privacy, error isolation, and crawler behavior.
- Avoid server-to-self public HTTP unless trust, latency, auth, and deployment implications are proven.

### Required Evidence

- Read-path inventory with consistency, timeout, cache, and owner.
- Trace timeline for representative critical pages.
- Query-plan and downstream-call evidence for expensive paths.
- Cancellation and timeout propagation evidence.

### Mandatory Failure And Acceptance Tests

- Inject a slow dependency and prove deadlines, fallback, and partial rendering.
- Disconnect during streaming and verify cancellation or intentional completion.
- Fail one branch of a parallel read and verify isolation and consistency.
- Use production-like data volume and verify bounded queries, fan-out, latency, and memory.

