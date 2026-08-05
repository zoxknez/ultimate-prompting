## Phase 8 - Server Components, Client Components, And RSC Boundaries

Audit trust, serialization, bundle, data, and lifecycle boundaries between server and browser code.

### Audit Requirements

- Inventory use client boundaries, server-only/client-only modules, barrels, dynamic imports, and third-party components.
- Verify secrets, privileged clients, private env values, tokens, and database objects never enter client bundles or props.
- Minimize client islands by measured interaction need, not by forcing browser-dependent UI onto the server.
- Review RSC payload size, duplicate data, private fields, error leakage, and serialization compatibility.
- Detect repeated server work per component, layout, metadata generation, request, or prefetch.
- Treat RSC and framework advisories as mandatory patch and regression-test inputs.

### Required Evidence

- Server/client boundary map with bundle ownership and serialized types.
- Client bundle scan for forbidden modules, env values, and sensitive strings.
- RSC payload captures for public, authenticated, tenant, and admin routes.
- Patch evidence for React, react-dom, Next.js, and RSC advisories.

### Mandatory Failure And Acceptance Tests

- Search client assets and RSC payloads for seeded secret canaries.
- Switch users and tenants and prove no payload or layout state crosses identity boundaries.
- Exercise malformed RSC/navigation requests supported by the harness and verify safe failure.
- Measure JS and RSC payload before and after boundary changes.

