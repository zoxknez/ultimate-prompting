## Faza 9 - Laravel application putanja

### Cilj

Audituj efektivno Laravel ponašanje od bootstrap-a kroz HTTP, console, queue, scheduler, events, storage i deployment.

### Zahtevi audita

- Proveri tačan Laravel patch, PHP podršku, first-party package verzije, package discovery, bootstrap konfiguraciju, service provider-e, middleware i exception handling.
- Audituj route model binding, Form Request-e, DTO-ove, cast-ove, accessor-e, mutator-e, resource-e, policy-je, gate-ove, middleware alias-e i redosled autorizacije.
- Pregledaj Eloquent fillable ili guarded polja, hidden i visible atribute, global scope-ove, soft delete, observer-e, model event-e, touching, pruning i serializaciju.
- Proveri Sanctum, Passport, session auth, password reset, email verifikaciju, Fortify, Socialite i custom guard ponašanje gde se koriste.
- Audituj queue-ove, Horizon, batch-eve, chain-ove, unique job-ove, middleware, retry, failed jobs, scheduler lock-ove, maintenance mode i worker reload.
- Audituj Octane kompatibilnost, scoped binding-e, singleton stanje, container reset, timer-e, task worker-e, concurrent taskove i izbor servera.
- Proveri generisanje config, route, event i view cache-a, storage linkove, signed URL-ove, Telescope, Horizon, Pulse, Ignition i pristup debug alatima.

### Obavezni dokazi

- Efektivna Laravel verzija i package matrica sa produkcionim bootstrap dokazom.
- Policy, middleware, model, queue, scheduler i Octane lifecycle regresioni testovi.
- Dokaz deployment cache-a i worker reload-a povezan sa artifact revizijom.

### Kriterijumi prihvatanja

- Kritična autorizacija i data invarijante ne zavise od skrivenog Eloquent ili package ponašanja.
- Svaki dugovečni Laravel proces resetuje request-scoped stanje i bezbedno se zamenjuje tokom deployment-a.

