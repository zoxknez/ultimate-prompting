## Faza N - Transakcije, Concurrency I Idempotency

- Definisi granice transakcije oko poslovnih invarijanti, a ne oblika controller-a ili duzine metode.
- Proveri isolation level, lock order, lock timeout, deadlock retry, optimistic locking i `SELECT FOR UPDATE` semantiku.
- Testiraj lost update, write skew, dupli submit, stale formu, paralelne workere i retry posle nepoznatog rezultata commit-a.
- Koristi database constraint-e i atomske statement-e kao poslednji sloj sprovodjenja kriticne jedinstvenosti i state transition-a.
- Dizajniraj idempotency kljuceve sa actor ili tenant scope-om, request fingerprint-om, atomskom rezervacijom, cuvanjem rezultata, expiry-jem i odbijanjem mismatch-a.
- Drzi spoljne side effect-e van nezasticenih transaction gap-ova; koristi outbox, reconciliation ili compensating action gde je potrebno.

