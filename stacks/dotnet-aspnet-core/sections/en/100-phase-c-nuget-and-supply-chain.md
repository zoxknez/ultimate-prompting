## Phase C - NuGet And Supply Chain

Determine: PackageReference, Central Package Management, `Directory.Packages.props`, transitive pinning, `packages.lock.json`, private feeds, floating/prerelease versions, local DLL references.

Classify each package: direct/transitive, build-only, analyzer, source generator, runtime, test, deprecated, vulnerable, unmaintained, preview, framework-provided.

Check: package source mapping, source order, dependency confusion, lock/locked restore, content hash, audit sources, audit suppressions, transitive vulnerability audit.

Useful commands (adapt to the real SDK):

```text
dotnet restore
dotnet restore --locked-mode
dotnet list package
dotnet list package --include-transitive
dotnet list package --outdated
dotnet list package --deprecated
dotnet list package --vulnerable --include-transitive
```

Do not claim a package is safe merely because restore has no warning. Do not suppress an advisory without documented reason, deadline, and compensating control.

Especially verify: whether Microsoft.Extensions.* forces a version different from the shared framework; whether the EF provider tracks the EF Core major; whether `dotnet-ef` matches EF runtime; package downgrade and duplicate assemblies.

