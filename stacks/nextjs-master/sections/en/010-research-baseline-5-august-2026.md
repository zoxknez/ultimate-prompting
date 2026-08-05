## Research Baseline - 5 August 2026

This is a dated starting point. Re-check primary sources, installed packages, lockfile, platform image, and the running process before every lifecycle, migration, security, or compatibility decision.

| Component | Baseline | Mandatory verification |
| --- | --- | --- |
| Next.js | 16.3.x latest stable feature line; 16.2.11 Active LTS and 15.5.21 Maintenance LTS after the July 2026 security release | Exact patch, maintained line, canary use, router mode, platform support, and advisories |
| React | 19.2.x stable; React Compiler 1.0 stable but optional | react/react-dom alignment, RSC patches, compiler config, and library compatibility |
| TypeScript | 7.0 stable; 6.0 remains the transition and compatibility line | Compiler used by editor, CI, Next build, tests, generators, and monorepo tasks |
| Node.js | 24 LTS and 22 LTS supported; 26 Current | Build/runtime image, architecture, libc, native ABI, and platform support |
| Routing | Next.js 16 renamed Middleware to Proxy | Actual file, matchers, semantics, runtime, rewrite, redirect, header, and bypass paths |
| Caching | Cache Components and use cache/private/remote are version-specific | Effective flags, cache keys, scope, invalidation, CDN behavior, and private-data isolation |

### Primary Source Policy

- Use official Next.js, React, Node.js, TypeScript, hosting-platform, ORM, database, auth-provider, and standards documentation.
- Record URL, access date, exact claim, selected version, and whether repository and runtime evidence confirm it.
- Do not replace official lifecycle, security, or migration guidance with summaries, social posts, snippets, or package popularity.
- When sources conflict, show the conflict and keep the decision conditional until the exact component and runtime are verified.

