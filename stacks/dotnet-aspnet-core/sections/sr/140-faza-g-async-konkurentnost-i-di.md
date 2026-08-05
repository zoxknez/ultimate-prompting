## Faza G - Async, Konkurentnost I DI

Proveri: sync-over-async, `.Result`/`.Wait()`/`.GetAwaiter().GetResult()`, `ConfigureAwait` gde je relevantan (biblioteke), `CancellationToken` propagaciju, fire-and-forget, `async void` (osim event handlere), paralelni pristup istom `DbContext`, nekontrolisanu paralelizaciju, shared mutable state, process-local lock u multi-replica okruzenju.

Proveri DI lifetime-ove: singleton koji hvata scoped (captive dependency), scoped u background service bez scope-a po operaciji, rucni root `ServiceProvider`, dispose, `IOptions` vs `IOptionsSnapshot` vs `IOptionsMonitor`, keyed services.

