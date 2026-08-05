## Research Baseline - 5 August 2026

This is a dated starting point. Re-check official sources, the lockfile, installed packages, build image, architecture, libc, native ABI, and the running process before every lifecycle, migration, security, or compatibility decision.

| Component | Baseline | Mandatory audit-time verification |
| --- | --- | --- |
| Node.js | 26 Current; 24 Krypton LTS; 22 Jod LTS. Re-check exact patches and support dates. | Actual binary, release line, architecture, libc, OpenSSL, ICU, V8, native ABI, image, and EOL. |
| Release model | One major per year is planned starting with Node.js 27. | LTS entry, upgrade cadence, support assumptions, and hosting-platform adoption. |
| Express | Express 5 is the latest stable major; Express 4 remains a legacy maintained line. | Exact patch, Node requirement, advisories, path syntax, middleware behavior, and migration state. |
| Fastify | Fastify 5.11.x is the latest documented LTS line at the baseline date. | Exact patch, plugin support, encapsulation, schema compiler, serializer, and Node matrix. |
| TypeScript | TypeScript 7 is stable; TypeScript 6 remains a migration and compatibility line. | Compiler used by editor, CI, build, generators, tests, and production source maps. |
| API security | OWASP API Security Top 10 2023 is the current official API risk edition at the baseline date. | Map applicable risks to concrete routes, identities, resources, data flows, and tests. |
| Observability | OpenTelemetry JavaScript supports Node instrumentation and OTLP exporters; package stability varies. | SDK and instrumentation versions, initialization order, propagation, sampling, redaction, and overhead. |

### Primary Source Policy

- Use official Node.js, Express, Fastify, TypeScript, package-manager, database, hosting-platform, OpenTelemetry, and standards documentation.
- Record source title, URL, access date, exact claim, selected version, and repository or runtime evidence that confirms or contradicts it.
- Do not replace lifecycle, security, migration, or protocol guidance with snippets, popularity, summaries, or AI-generated claims.
- When official sources and runtime evidence conflict, show the conflict and keep the decision conditional until the exact artifact and process are verified.

