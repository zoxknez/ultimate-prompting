## Phase H - RUST PATH: Build, Lint, Ownership, Errors

### Baseline

```text
cargo fmt --all -- --check
cargo check --workspace --all-targets
cargo build --workspace --all-targets --locked
cargo build --release --workspace --locked
cargo clippy --workspace --all-targets --locked -- -D warnings
cargo doc --workspace --no-deps --locked
cargo test --doc --workspace --locked
cargo test --workspace --locked
```

`cargo check` is a fast check, **not** a substitute for `cargo build`. Do not enable `--all-features` blindly if features are mutually exclusive; build a feature matrix. Do not enable full pedantic/nursery/restriction groups blindly.

### Ownership and types

Check: unnecessary clone, oversized lifetimes, cyclic Rc/Arc, Weak, borrows across async boundaries, self-referential structures, Pin.

Send/Sync: whether a type may truly cross thread boundaries; `unsafe impl Send/Sync` without a formal invariant is a P0/P1 candidate.

Interior mutability: `Cell`/`RefCell`/`Mutex`/`RwLock`/`Atomic*`; lock scope; poison; deadlock; async + `std::sync::Mutex` on executor threads.

### Error handling

Check: `Result` vs panic, `unwrap`/`expect` on production paths, `?` and error context (`thiserror`/`anyhow` where present), discarded `Result`, partial cleanup, `catch_unwind` as a universal solution. Do not add panic/unwrap as a quick fix.

