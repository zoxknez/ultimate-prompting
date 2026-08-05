# Stack overlay — Rust

Load with: `core/*` + this file (not the full Go half of the mega-prompt).

## Path selection

Confirm workspace members, edition, `rust-version`/MSRV, features matrix.

## Mandatory focus

- `cargo build` is authoritative (`cargo check` is not full proof)
- Clippy policy without blind restriction groups
- unsafe inventory + `# Safety` / `// SAFETY:` invariants
- Miri/sanitizer limits when applicable
- async runtime (Tokio/etc.) cancel safety, bounded spawn
- FFI ABI/ownership; no unwind across FFI without design
- lockfile, `--locked`, supply chain (`cargo audit`/`deny` if present)

## Prefer commands scoped to crates/features

Do not run invalid `--all-features` combinations. Discover features first.

## Entry prompt

For a single-file convenience entry, see `go-rust-backend-audit-prompt.*.md` and **skip Go sections** when path is pure Rust.
