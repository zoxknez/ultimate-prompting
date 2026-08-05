## Faza P - Test Strategija I Popravke

Inventarisi: unit, integration, race, fuzz, Miri/sanitizer, contract, security, concurrency, migration, E2E, load, recovery, publish smoke.

Svaka P0-P2 popravka zahteva test koji demonstrira staro neispravno i novo ispravno ponasanje.

Pre izmene: nalaz, hipoteza, minimalna izmena, ugovor koji se cuva, rizik, test koji moze opovrgnuti, rollback. Menjaj najmanji skup fajlova. Ne menjaj `go.mod`/`go.sum`/`Cargo.lock` bez pregleda.

