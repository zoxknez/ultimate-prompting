## Phase G - Async, Concurrency, And DI

Check: sync-over-async, `.Result`/`.Wait()`/`.GetAwaiter().GetResult()`, `ConfigureAwait` where relevant (libraries), `CancellationToken` propagation, fire-and-forget, `async void` (except event handlers), parallel use of the same `DbContext`, uncontrolled parallelization, shared mutable state, process-local locks in multi-replica environments.

Check DI lifetimes: singleton capturing scoped (captive dependency), scoped use in background services without per-operation scope, manual root `ServiceProvider`, dispose, `IOptions` vs `IOptionsSnapshot` vs `IOptionsMonitor`, keyed services.

