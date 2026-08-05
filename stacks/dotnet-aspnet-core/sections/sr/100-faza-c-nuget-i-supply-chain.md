## Faza C - NuGet I Supply Chain

Utvrdi: PackageReference, Central Package Management, `Directory.Packages.props`, transitive pinning, `packages.lock.json`, privatne feedove, floating/prerelease verzije, lokalne DLL reference.

Za svaki paket klasifikuj: direct/transitive, build-only, analyzer, source generator, runtime, test, deprecated, vulnerable, unmaintained, preview, framework-provided.

Proveri: package source mapping, redosled izvora, dependency confusion, lock/locked restore, content hash, audit sources, audit suppression, transitive vulnerability audit.

Korisne komande (prilagodi stvarnom SDK-u):

```text
dotnet restore
dotnet restore --locked-mode
dotnet list package
dotnet list package --include-transitive
dotnet list package --outdated
dotnet list package --deprecated
dotnet list package --vulnerable --include-transitive
```

Ne tvrdi da je paket bezbedan samo zato sto restore nema warning. Ne suppression-uj advisory bez dokumentovanog razloga, roka i compensating control-a.

Posebno proveri: da li Microsoft.Extensions.* forsira verziju razlicitu od shared framework-a; da li EF provider prati EF Core major; da li `dotnet-ef` odgovara EF runtime-u; package downgrade i duplicate assembly.

