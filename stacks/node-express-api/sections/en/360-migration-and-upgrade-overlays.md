## Migration And Upgrade Overlays

### Node.js Release-Line Upgrade

- Verify runtime APIs, V8, OpenSSL, ICU, native ABI, permission model, test runner, fetch or Undici behavior, deprecations, and platform support.
- Test every native addon and downloaded binary on all target architecture and libc combinations.
- Compare old and new runtime under integration, load, memory, shutdown, failover, and rollback scenarios.
- Do not use Node Current as the default production target without explicit lifecycle and platform approval.

### Express 4 To Express 5

- Inventory removed APIs, path syntax, query and body changes, MIME behavior, async errors, wrappers, and middleware compatibility.
- Use codemods only as a starting point and review every semantic and public-contract change.
- Run route, error, proxy, static, upload, webhook, and compatibility regression suites before promotion.
- Define rollback constraints if session, cache, schema, client, or error behavior changes.

### Fastify Core Or Plugin Upgrade

- Verify core, plugin, schema, serializer, type-provider, logger, and Node support as one tested graph.
- Diff effective encapsulation, hooks, schemas, parsers, route registration, and error behavior.
- Regenerate and compare contracts and run security, load, and compatibility regression tests.
- Preserve a tested previous artifact and data-compatible rollback path.

### CommonJS To ESM

- Map package type, entrypoints, extensions, exports, conditional exports, require hooks, dirname usage, dynamic import, and tooling.
- Test workers, migrations, scripts, CLI, instrumentation, preload, native addons, and package consumers.
- Avoid dual-package state duplication and verify singleton assumptions across module graphs.
- Release with explicit compatibility and rollback criteria.

### TypeScript 6 To TypeScript 7

- Verify editor, CI, build, generators, lint, tests, language-service plugins, decorators, declarations, and source maps.
- Compare compiler diagnostics and transformed output for critical packages.
- Do not hide new errors through noCheck, expanded skipLibCheck, transpile-only paths, or broad suppressions.
- Keep a tested compiler and toolchain rollback until release confidence is established.

