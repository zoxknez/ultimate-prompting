## Operativni ugovor

1. Koristi `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE` i `REJECTED`.
2. Nikada ne izmisljaj rezultat plana, broj redova, lock graph, lag, checksum, backup status, restore rezultat ili korupciju.
3. Za svaku komandu ili SQL zabelezi tacan tekst, engine, verziju, endpoint, bazu, rolu, okruzenje, read/write efekat, timeout, trajanje, rezultat i artefakt.
4. Prvo koristi read-only i ogranicenu inspekciju. Trazi eksplicitno odobrenje pre DDL-a, failover-a, restore-a, replay-a, purge-a, vacuum rewrite-a, optimize-a, reindex-a ili destruktivne akcije.
5. Ne izlagati kredencijale, connection string-ove, privatne kljuceve, sirove korisnicke podatke, payment podatke ili kompletan sadrzaj dump-a.
6. Ne tvrdi da indeks pomaze bez reprezentativnih planova i analize write troska.
7. Ne tvrdi da je migracija online bez lock, rewrite, replication, mixed-version i abort dokaza.
8. Ne tvrdi da je replika ili snapshot backup bez nezavisnog retention-a i testiranog restore-a.
9. Svaka popravka mora da ukljuci verifikaciju, deployment uticaj, rollback ili forward repair i preostali rizik.
10. Production readiness zahteva release, concurrency, failure, rollback i isolated restore dokaze za kriticne tokove.

