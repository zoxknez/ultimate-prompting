## Phase 21 - Runtimes, Vercel, Self-Hosting, And Multi-Instance Operation

Treat Node, Edge, serverless, containers, Vercel, and adapters as distinct products with different guarantees.

### Audit Requirements

- Inventory runtime per route, action, handler, metadata task, image path, job, and function.
- Verify APIs, native modules, WASM, crypto, filesystem, sockets, drivers, telemetry, and SDK support in each runtime.
- Do not rely on warm instances, globals, local persistence, in-memory locks, counters, sessions, or cache for correctness.
- Map duration, CPU, memory, payload, streaming, connection, region, cold start, concurrency, and billing limits.
- For Vercel verify project linkage, env scopes, domains, aliases, deployment protection, regions, functions, cache, and access.
- For self-hosting verify standalone output, traced files, assets, proxy headers, health, signals, shared cache, deploymentId, draining, and retention.

### Required Evidence

- Route-to-runtime and capability matrix.
- Measured cold/warm latency, memory, duration, payload, and concurrency.
- Platform project or container configuration tied to the deployment.
- Multi-instance cache, deployment ID, draining, and asset-retention evidence.

### Mandatory Failure And Acceptance Tests

- Force cold starts, scale-out, abrupt termination, old/new overlap, and region changes.
- Run every Edge route against unsupported API and dependency detection.
- Exhaust database connections under serverless burst.
- Terminate a mutation after commit but before response and verify idempotent recovery.

