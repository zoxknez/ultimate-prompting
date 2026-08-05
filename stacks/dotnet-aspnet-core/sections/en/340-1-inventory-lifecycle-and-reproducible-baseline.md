## 1. Inventory, Lifecycle, And Reproducible Baseline

Map solution/project topology, TFM, `global.json`, SDK/runtime, CPM/package references, lock files, NuGet sources, analyzers, nullable/implicit-using, trimming/AOT, build/publish profiles, entry points, host type, DI, middleware order, endpoints, EF contexts/migrations, jobs, queues, cache, auth, configuration, deployment, CI/CD, and tests.

Confirm the production runtime is supported and on its current servicing patch. LTS receives three years of support, STS two; an unsupported or unpatched runtime is a production risk. Distinguish framework-dependent and self-contained; self-contained must be rebuilt when the bundled runtime needs an update.

Create the map: `client → CDN/load balancer/reverse proxy → Kestrel/IIS → middleware → endpoint → authentication → authorization → validation → application operation → database/cache/queue/external dependency → response`.

Run deterministic restore, build, analyzers, tests, publish, production-like startup, migration status, health/readiness, and graceful shutdown where supported. Record commands, versions, exit codes, and the cause of the first failure.

