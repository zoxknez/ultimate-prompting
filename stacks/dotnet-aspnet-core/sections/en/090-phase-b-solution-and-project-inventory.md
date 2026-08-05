## Phase B - Solution And Project Inventory

Map: solution → projects → project references → packages → deployment units.

Flag: cyclic project references; unnecessary references; domain depending on ASP.NET Core/EF implementation; test project using production secrets; project that builds but is not deployed; multiple versions of the same package; divergent TFMs without reason; “Common/Shared” without clear responsibility.

For each project record: Project Sdk, TFM(s), RuntimeIdentifiers, OutputType, Nullable, ImplicitUsings, LangVersion, TreatWarningsAsErrors, AnalysisLevel/Mode, InvariantGlobalization, PublishTrimmed/Aot, SelfContained, PublishSingleFile, ReadyToRun, ServerGarbageCollection, unsafe/COM, platform target.

Review central MSBuild files: import order, conditional properties, custom Exec, code generation, signing, copy operations, warning suppressions, environment-specific behavior. Look for secrets in MSBuild properties, shell injection via Exec, and targets that modify source during build.

