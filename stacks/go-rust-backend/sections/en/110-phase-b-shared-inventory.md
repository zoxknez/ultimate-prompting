## Phase B - Shared Inventory

Map: executables, libraries, modules/crates, public APIs, generated code, build scripts, CLIs, servers, workers, schedulers, consumers, migrations, protocols, database layer, cache, messaging, FFI, filesystem, deployment/ops, test fixtures, benchmarks, fuzz targets, CI, containers, IaC.

Graph: `repo → module/workspace → package/crate → executable → deployment unit`.

Flag: cyclic dependencies; oversized shared/common; domain depending on infrastructure; duplicated models; multiple implementations of the same business rule; deployment unit sharing a database without clear ownership; hand-edited generated code; stale executables still building; feature/build-tag combinations CI does not exercise.

