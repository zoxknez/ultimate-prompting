## Mandatory Evidence Matrices

Create every applicable matrix. Use `NOT_APPLICABLE` only with a reason and `UNVERIFIED` when evidence is unavailable.

| ID | Matrix | Minimum columns |
| --- | --- | --- |
| M1 | Source, toolchain, and artifact identity | component | commit | toolchain | graph/lock | tags/features | target/profile | artifact digest | runtime proof | status |
| M2 | Executable, module, crate, and deployment inventory | unit | language | entrypoint | owner | data | network | privileges | deployment | criticality | tests |
| M3 | Go target and build-tag support | command/package | GOOS | GOARCH | tags | cgo | libc | toolchain | build | test | artifact | owner |
| M4 | Rust target, feature, MSRV, and profile support | crate/bin | target | features | profile | MSRV | stable | native deps | build | test | artifact | owner |
| M5 | Concurrency and lifecycle ownership | goroutine/task | creator | resource | limit | cancellation | join/supervision | panic | metric | shutdown | test |
| M6 | Unsafe, cgo, FFI, native, and ABI boundary | boundary | caller | callee | safety contract | ownership | ABI/layout | unwind | threading | validation | tool evidence | owner |
| M7 | API, RPC, stream, and protocol contract | method/service | authn | authz/owner | validation | limits | deadline | idempotency | transaction | compatibility | negative test |
| M8 | State-changing business flow | flow | invariant | reads | locks | writes | side effects | commit | retry | reconciliation | rollback | tests |
| M9 | Data schema and migration compatibility | change | old reader | old writer | new reader | new writer | backfill | lock risk | rollback | forward repair | restore test |
| M10 | Dependency and supply-chain trust | dependency/tool | source | pin/lock | license | advisory | build execution | native/unsafe | owner | update | revocation |
| M11 | SLO, capacity, overload, and observability | journey | SLI | objective | load model | bottleneck | admission limit | alert | dashboard | runbook | evidence |
| M12 | Rollout, rollback, restore, and incident readiness | risk | rollout gate | canary | abort signal | rollback action | data compatibility | restore step | RPO/RTO | owner | drill evidence |

