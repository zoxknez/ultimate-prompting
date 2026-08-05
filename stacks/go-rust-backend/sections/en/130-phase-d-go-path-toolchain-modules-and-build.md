## Phase D - GO PATH: Toolchain, Modules, And Build

Run for every Go module.

### Toolchain

Check: `go version`, GOROOT/GOPATH, GOMOD/GOWORK, GOTOOLCHAIN, GOOS/GOARCH, CGO_ENABLED, GOEXPERIMENT, GODEBUG, GOPROXY/GOSUMDB/GOPRIVATE/GONOSUMDB, build cache. Do not disclose credentials from proxy/VCS configuration.

### go.mod and workspace

Check: module path, `go` directive, `toolchain` directive, require/indirect, replace/exclude/retract, local paths, pseudo/prerelease versions, major `/vN` path, private modules, dependencies that require a newer Go.

Especially: replace to a local dir that will not exist in CI; undocumented forks; replace hiding a security update; different versions of the same module across workspace members.

If `go.work` exists: use entries, local modules, whether CI uses the workspace, difference with `GOWORK=off`, whether the workspace hides a missing published dependency.

### Verification

```text
go env
go list -m -json all
go mod graph
go mod verify
go mod tidy -diff
```

Do not run mutating `go mod tidy` before reviewing `-diff`. If vendored: check `go mod verify` and `-mod=vendor`; do not regenerate vendor without reviewing the diff.

### Build baseline

```text
go build ./...
go test ./...
go vet ./...
go build -trimpath -o ./dist/app ./cmd/app
```

Adapt package, output, build tags, CGO, target OS/arch, linker flags, version metadata. Do not claim the production build works merely because `go test ./...` passes.

