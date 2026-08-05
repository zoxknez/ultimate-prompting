## Forbidden Shortcuts

- Do not infer production truth from source configuration, `.env.example`, local Docker, a green pipeline, or framework defaults.
- Do not treat `composer install`, unit tests, static analysis, or a successful HTTP smoke test as complete release proof.
- Do not assume CLI and FPM use the same PHP, INI, extensions, environment, working directory, user, or filesystem.
- Do not assume Laravel and Symfony annotations, attributes, policies, voters, middleware, listeners, or service definitions are effective without runtime-path evidence.
- Do not use UI restrictions, hidden fields, model fillable settings, route naming, or TypeScript types as authorization or validation.
- Do not add blind retries around non-idempotent operations, nested clients, transactions, or provider calls.
- Do not use cache, session, distributed lock, search index, queue, or object storage as an unexamined source of truth.
- Do not run destructive migrations, backfills, mass fixes, bulk replays, or cache flushes without approval, bounds, observability, and recovery.
- Do not claim zero downtime while old FPM children, stale OPcache, old workers, incompatible messages, or old schemas remain unverified.
- Do not expose debug, profiler, Horizon, Telescope, Pulse, Ignition, phpinfo, health detail, or stack traces as an operational shortcut.
- Do not deploy a rebuilt artifact under the same version, reuse mutable tags, install dependencies in production, or edit vendor code in place.
- Do not clean a compromised host in place and call it trusted, or restore from an unverified backup.
- Do not mark a finding fixed until the cause, regression test, packaged artifact, deployment path, telemetry, and rollback or recovery are verified.

