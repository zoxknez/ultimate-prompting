## Test strategija i piramida database verifikacije

Izgradi testove na sloju koji moze da reprodukuje relevantnu engine semantiku i failure mode.

- Koristi unit testove za cisto mapiranje i generisanje SQL-a, a ne kao dokaz engine ponasanja.
- Koristi integration testove na stvarnom produkcionom engine-u i podrzanoj patch porodici.
- Dodaj schema, migration, rollback, seed, permission i tenant-isolation testove.
- Dodaj concurrent transaction, deadlock, retry, idempotency i commit-uncertainty testove.
- Dodaj reprezentativne plan, load, soak, connection-storm i resource-exhaustion testove.
- Dodaj backup, PITR, restore, failover, failback i reconciliation game-day testove.

