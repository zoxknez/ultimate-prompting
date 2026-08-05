## Phase 5 - Next.js Configuration, Build Graph, And Output

Audit effective Next.js configuration and emitted route/runtime graph for the exact version and target.

### Audit Requirements

- Inspect next.config branches, plugins, compiler options, experimental flags, output, basePath, assetPrefix, images, redirects, rewrites, headers, and cache settings.
- Verify Turbopack or alternative bundler behavior, loader/plugin compatibility, source maps, minification, and tree shaking.
- Record static, dynamic, partially prerendered, edge, Node, client, and handler decisions from build output.
- Detect ignored build errors, warning-as-success, type/lint bypass, missing env validation, and route conflicts.
- Verify output tracing, standalone packaging, serverExternalPackages, native modules, and runtime files.
- Compare local, CI, preview, staging, and production builds and explain every difference.

### Required Evidence

- Effective next.config per environment class.
- Build output and route/runtime manifest inventory.
- Bundle and traced-file evidence for critical routes.
- List of warnings, suppressions, experimental flags, and deployment branches.

### Mandatory Failure And Acceptance Tests

- Start the production artifact with only documented runtime files.
- Fail on missing or malformed required environment variables.
- Exercise every runtime class and detect unsupported Edge APIs.
- Verify source-map upload and access control without exposing source or secrets.

