## Technology Path Selection

At the start, determine one of:

| Path | When |
| --- | --- |
| `GO` | Only Go modules/packages/executables. |
| `RUST` | Only Rust crates/workspaces/executables. |
| `MIXED_GO_RUST` | Both languages in the same system. |
| `UNKNOWN` | Insufficient evidence; inventory first, do not guess. |

For `MIXED_GO_RUST`:

- shared system analysis;
- full Go path for Go modules;
- full Rust path for Rust crates/workspaces;
- dedicated analysis of FFI, IPC, network, and data boundaries between them.

Do not apply Go recommendations to the Rust side or Rust recommendations to the Go side without a clear technology boundary.

