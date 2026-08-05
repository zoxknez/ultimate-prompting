## Faza AF - Test Strategija I Matrica Verifikacije

- Koristi unit testove za cista domenska pravila i property testove za invarijante, parser-e, novac, datume i state machine-e.
- Koristi request i integration testove za middleware, sesije, CSRF, autorizaciju, database constraint-e i spoljne ugovore.
- Koristi system testove za kriticne browser i Hotwire tokove, ukljucujuci JavaScript, accessibility i stale-page ponasanje.
- Koristi job testove sa stvarnim adapterom ili vernim integration okruzenjem za retry, duplicate, crash i mixed-version ponasanje.
- Pokreni concurrency i failure testove protiv stvarne podrzane baze, cache-a i queue backend-a, a ne samo transactional fixture-a.
- Proveri production asset build, eager load, release boot, migraciju, health, smoke, shutdown i rollback.

