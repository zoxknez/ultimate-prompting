## 4. JPA/Hibernate, Transakcije, Migracije I Cache

Pregledaj entity mapiranja, fetch planove, lazy-loading granice, serijalizaciju entiteta, N+1/cartesian explosion, query/index upotrebu, siroke selecte, paginaciju, locking/version polja, unique/foreign-key/check ogranicenja, default/nullability, timestamp/time zone, currency precision, connection-pool podesavanja, statement timeout, raw/native SQL, transaction isolation, audit/soft delete i backup/restore pretpostavke. Kriticne invarijante pripadaju bazi kada je moguce; binarni floating point nije izvor istine za novac.

Auditiraj `@Transactional` semantiku, izbor transaction managera, propagation/isolation/read-only/timeout/rollback pravila, checked-exception ponasanje, async/reactive granice i proxy ogranicenja. U podrazumevanom proxy modu, self-invocation i initialization pozivi ne prolaze kroz transactional advice; ne pretpostavljaj da anotacija garantuje transakciju bez testiranja stvarne putanje poziva. Transakcija baze ne ukljucuje automatski eksterni HTTP, message broker, fajl ili email side effect; koristi transactional outbox ili namernu kompenzaciju gde je potrebno.

Pregledaj Flyway/Liquibase migracije kao verzionisane produkcione izmene. Zahtevaj vlasnika migracije, pregled generisanog SQL-a, backup/restore verifikaciju, procenu locka/trajanja, kompatibilnost rolling deploymenta, strategiju data backfill-a, forward repair put i testiran rollback ili kompenzujucu migraciju. Ne dozvoli da svaka replika automatski primeni produkcione migracije osim ako serijalizovan deployment dizajn dokazuje bezbednost.

Za svaki kritican upis dokumentuj citanja, validaciju, promene stanja, invarijantu, ponasanje konkurentnosti, atomsku granicu, ponasanje pri neuspehu zavisnosti, rollback/kompenzaciju i audit zapis. Testiraj lost update, write skew, duplu uplatu/porudzbinu/job, negativan inventory, duplu rezervaciju, parcijalne operacije i cache nekonzistentnost. JVM-local lock ne moze zastititi horizontalno skalirane instance.

Za retryable ili spolja pokrenute upise proveri idempotentnost za duple submisije, timeout, webhook replay, broker redelivery i pad nakon side effecta pre acknowledgementa. Koristi odgovarajuci tenant/user-scoped idempotency key, request fingerprint, unique constraint, sacuvan outcome/state, expiration, definisan conflict response i atomsku granicu uz business write/outbox.

Mapiraj local, distributed, HTTP/CDN, database i computed cache. Proveri dizajn kljuca, tenant/user/permission opseg, TTL, velicinu, invalidaciju, serialization/versioning, stampede/outage ponasanje i stale strategiju. Privatni podaci ne smeju koristiti shared/public cache kljuceve, a cache nije izvor istine za kriticne invarijante.

