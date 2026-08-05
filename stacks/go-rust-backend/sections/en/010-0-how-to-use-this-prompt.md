## 0. How To Use This Prompt

### 0.1 Required Inputs

| Field | Value |
| --- | --- |
| Repository, archive, modules, workspaces, and relevant paths | `[PATHS / URLS]` |
| Business purpose, critical flows, and invariants | `[FLOWS / INVARIANTS]` |
| Technology path and executable artifacts | `[GO / RUST / MIXED / BINARIES]` |
| Targets, architectures, libc, and operating systems | `[TARGET MATRIX]` |
| Protocols, clients, peers, and compatibility promises | `[HTTP / GRPC / TCP / UDP / QUIC / OTHER]` |
| Data stores, queues, caches, files, and schemas | `[SYSTEMS / OWNERS]` |
| Identity, tenant, authorization, and privileged operations | `[MODEL / POLICIES]` |
| Traffic, concurrency, latency, capacity, and SLO targets | `[LOAD / BUDGETS]` |
| Build tags, Cargo features, profiles, and release variants | `[MATRIX]` |
| FFI, cgo, native libraries, kernels, devices, or WASM hosts | `[BOUNDARIES]` |
| Deployment, artifact registry, signing, and rollout | `[PLATFORMS / CHANNELS]` |
| Production access, change authorization, and work mode | `[ACCESS / APPROVERS / MODE]` |

### 0.2 Missing Information And Evidence Ceiling

1. Continue with safe discovery when inputs are incomplete; do not block the entire audit.
2. Infer only from repository state, lock files, resolved graphs, generated output, build metadata, artifacts, runtime evidence, telemetry, database constraints, and authoritative documentation.
3. Mark every unresolved material claim as `UNVERIFIED` and state the exact access, workload, target, fixture, credential, approval, or environment needed to resolve it.
4. Do not issue an unconditional production-ready verdict when release, target, dependency, data, failure, deployment, or recovery evidence is unavailable.

