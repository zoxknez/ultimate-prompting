## Faza S - Migracije, backfill i mixed-version kompatibilnost

Tretiraj svaku schema i data promenu kao distribuirano izdanje.

- Pregledaj tacnu DDL semantiku, snagu lock-a, table rewrite, log volume, replication efekat i cancellation ponasanje.
- Koristi expand-and-contract za nekompatibilne promene i dokazi koegzistenciju stare i nove aplikacije.
- Ucini backfill chunked, checkpointed, restartabilnim, idempotentnim, rate-limited i observable.
- Definisi correctness upit, progress metriku, pause, resume, abort i cleanup.
- Testiraj migraciju iz production-like snapshot-a sa realnim data skew-om i paralelnim saobracajem.
- Razdvoji application rollback, schema rollback, data rollback i forward repair; dokazi koji su stvarno bezbedni.

