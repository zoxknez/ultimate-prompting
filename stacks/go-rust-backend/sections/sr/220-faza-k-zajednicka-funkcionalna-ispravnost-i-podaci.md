## Faza K - Zajednicka Funkcionalna Ispravnost I Podaci

Za svaki kritican tok: `ulaz -> authn -> authz -> validacija -> use case -> transakcija -> DB/cache/broker/spoljni servis -> odgovor -> telemetry`.

Proveri nedozvoljene state transition-e, race scenarije, pravila za novac/inventar, audit trail. Domain pravila ne smeju postojati samo u handleru ili klijentu.

Transakcije: stvarna granica (ne samo ime funkcije), isolation, deadlock retry, partial failure, outbox/inbox, saga/kompenzacija. Idempotency za retryable upise: key, unique constraint, stored outcome, conflict response. Process-local/in-memory idempotency ne stiti multi-replica sistem.

Migracije: vlasnik, SQL review, lock/duration, rolling compatibility, backup/restore, rollback/forward repair. Ne izvrsavaj destruktivne migracije u auditu.

