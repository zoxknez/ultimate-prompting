# Stack overlay — Go

Load with: `core/*` + this file (not the full Rust half of the mega-prompt).

## Path selection

Confirm modules, `go.work`, build tags, CGO, targets.

## Mandatory focus

- `go` / `toolchain` directives, `GOTOOLCHAIN`, GODEBUG
- `go test -race`, fuzz targets, `govulncheck` (reachability limits)
- goroutine ownership, context cancel, channel close ownership
- `database/sql` pools, transactions, migrations
- HTTP timeouts, SSRF, supply chain (`go.mod`/`sum`)
- graceful shutdown

## Prefer commands scoped to packages

Discover packages first (`go list ./...`). Do not invent fuzz target names.

## Entry prompt

For a single-file convenience entry, see `go-rust-backend-audit-prompt.*.md` and **skip Rust sections** when path is pure Go.
