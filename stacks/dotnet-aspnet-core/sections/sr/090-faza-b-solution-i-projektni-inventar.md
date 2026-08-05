## Faza B - Solution I Projektni Inventar

Mapiraj: solution -> projekti -> project references -> paketi -> deployment jedinice.

Oznaci: ciklicne project reference; nepotrebne reference; domain zavisan od ASP.NET Core/EF implementacije; test projekat sa production tajnama; projekat koji se builda ali se ne deployuje; vise verzija istog paketa; divergentne TFM-ove bez razloga; "Common/Shared" bez jasne odgovornosti.

Za svaki projekat evidentiraj: Project Sdk, TFM(s), RuntimeIdentifiers, OutputType, Nullable, ImplicitUsings, LangVersion, TreatWarningsAsErrors, AnalysisLevel/Mode, InvariantGlobalization, PublishTrimmed/Aot, SelfContained, PublishSingleFile, ReadyToRun, ServerGarbageCollection, unsafe/COM, platform target.

Pregledaj centralne MSBuild fajlove: import redosled, uslovne property-je, custom Exec, generisanje koda, potpisivanje, copy operacije, warning suppression, environment-specific ponasanje. Trazi tajne u MSBuild property-jima, shell injection kroz Exec, target koji menja source tokom builda.

