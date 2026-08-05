## Phase A - Protect The Workspace

Before any change:

- find repository root, branch, status, uncommitted changes, commit SHA, submodules;
- find `.sln`/`.slnx`/`.slnf`, all `.csproj`/`.fsproj`/`.vbproj`, `global.json`, `Directory.Build.props`/`.targets`, `Directory.Packages.props`, `nuget.config`, lock files;
- find User Secrets IDs without reading secret values;
- find certificate/PFX/key/secret files without displaying contents;
- verify test configuration does not point at production services;
- record initial state of generated files.

Useful commands:

```text
git status --short --branch
git rev-parse --show-toplevel
git rev-parse HEAD
git submodule status
dotnet --info
dotnet --list-sdks
dotnet --list-runtimes
```

On Windows when relevant: `Get-Command dotnet`. Do not assume the interactive-shell `dotnet` matches the SDK used by the IDE or CI.

