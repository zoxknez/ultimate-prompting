## Faza D - GO STAZA: Toolchain, Moduli I Build

Izvrsi za svaki Go modul.

### Toolchain

Proveri: `go version`, GOROOT/GOPATH, GOMOD/GOWORK, GOTOOLCHAIN, GOOS/GOARCH, CGO_ENABLED, GOEXPERIMENT, GODEBUG, GOPROXY/GOSUMDB/GOPRIVATE/GONOSUMDB, build cache. Ne objavljuj credentiale iz proxy/VCS konfiguracije.

### go.mod i workspace

Proveri: module path, `go` direktivu, `toolchain` direktivu, require/indirect, replace/exclude/retract, lokalne putanje, pseudo/prerelease verzije, major `/vN` path, private module, dependency koji zahteva noviji Go.

Posebno: replace ka lokalnom dir koji nece postojati u CI; fork bez razloga; replace koji prikriva security update; razlicite verzije istog modula kroz workspace.

Ako postoji `go.work`: use unosi, lokalni moduli, da li CI koristi workspace, razlika sa `GOWORK=off`, da li workspace prikriva nedostajuci objavljeni dependency.

### Verifikacija

```text
go env
go list -m -json all
go mod graph
go mod verify
go mod tidy -diff
```

Ne izvrsavaj `go mod tidy` koji menja fajlove pre pregleda `-diff`. Ako vendor: proveri `go mod verify` i `-mod=vendor`; ne regenerisi vendor bez pregleda diffa.

### Build baseline

```text
go build ./...
go test ./...
go vet ./...
go build -trimpath -o ./dist/app ./cmd/app
```

Prilagodi paket, output, build tagove, CGO, target OS/arch, linker flagove, version metadata. Ne tvrdi da production build radi samo zato sto `go test ./...` prolazi.

