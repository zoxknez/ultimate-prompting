## Migration And Upgrade Overlays

### Next.js 15/16 To 16.3

- Read every intermediate migration guide and security advisory; do not jump major or maintained patch lines without evidence.
- Inventory async request APIs, routing, caching, Proxy migration, Turbopack, images, runtimes, and removed config.
- Verify App Router, Pages Router, mixed mode, custom server, adapters, instrumentation, auth, tests, and observability at each step.
- Separate framework upgrade from TypeScript major, React Compiler, database, auth, infrastructure, and cache redesign.
- Maintain tested rollback or forward repair for code, schema, cache, assets, sessions, and long-lived clients.

### Middleware To Proxy

- Use the official codemod or controlled rename only after mapping matchers, imports, tests, deployment rules, and docs.
- Verify semantics, runtime, coverage, redirects, rewrites, headers, and auth assumptions after migration.
- Move security decisions to destination data and mutation boundaries when they were concentrated in Middleware.
- Retest routes, APIs, RSC requests, static assets, hosts, locales, and encoded paths.

### React Compiler 1.0

- Confirm React/compiler compatibility, syntax, library behavior, lint, source maps, debugging, and cache behavior.
- Start with measured routes or packages, explicit cohorting, before/after metrics, correctness tests, and a fast disable path.
- Do not remove manual memoization until behavior and performance are proven under the compiler.
- Audit external stores, identity-sensitive values, mutable objects, effects, and library components.

### TypeScript 6 To 7

- Treat TypeScript 7 as stable, but verify its native compiler, language service, APIs, editor, plugin, generator, bundler, and library compatibility before production adoption.
- Run compiler, editor, Next build, ESLint, test runner, Storybook, generators, monorepo tools, and libraries on a compatibility branch.
- Record diagnostics, resolution, emit/bundle differences, performance, declarations, and suppressed errors.
- Do not combine the TypeScript major with unrelated framework, React, schema, cache, or deployment redesign.

