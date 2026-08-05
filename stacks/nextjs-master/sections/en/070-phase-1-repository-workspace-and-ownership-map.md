## Phase 1 - Repository, Workspace, And Ownership Map

Map the effective application, not only the top-level folder. Include monorepo packages, generators, deployment projects, shared UI, internal libraries, schemas, infrastructure, and operational tooling.

### Audit Requirements

- Identify package boundaries, owners, public APIs, circular dependencies, duplicate utilities, and cross-layer imports.
- Map every app, package, worker, scheduled job, CLI, migration tool, Storybook, preview, and deployment project.
- Distinguish safely shared code from code that leaks server-only modules, secrets, or heavyweight dependencies into client bundles.
- Document ownership for auth, authorization, data, cache invalidation, deployment, rollback, restore, and incident response.
- Detect shadow config, copied route logic, duplicate schemas, abandoned packages, and unused deployment paths.
- Map trust boundaries between browser, CDN, Proxy, runtime, database, queue, storage, providers, and admin tooling.

### Required Evidence

- Repository tree, workspace graph, ownership map, and generated-code inventory.
- Import graph for critical packages and server/client boundary paths.
- Route-to-owner and side-effect-to-owner matrices.
- List of authoritative and duplicated configuration or schema sources.

### Mandatory Failure And Acceptance Tests

- Build a clean checkout without undeclared local files.
- Trace one critical journey across every package and runtime boundary.
- Prove which config or schema source is authoritative by controlled change or generated output.
- Verify no client entry can import server-only code through a barrel export or transitive dependency.

