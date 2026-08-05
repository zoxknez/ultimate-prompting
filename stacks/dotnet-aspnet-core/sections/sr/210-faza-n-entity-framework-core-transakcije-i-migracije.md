## Faza N - Entity Framework Core, Transakcije I Migracije

DbContext: scoped lifetime, factory, pooling (oprezno sa mutable state/interceptor/tenant), background service scope po operaciji, disposal. DbContext nije thread-safe i ne sme se koristiti paralelno iz vise taskova.

Model: PK/AK, concurrency token/rowversion, FK, cascade/restrict, owned/complex types, value converters, precision, indexes, unique/check constraints, query filters (tenant/soft delete), audit polja.

Ne vracaj EF entity direktno kao javni API ugovor bez opravdanja. Proveri tracking vs `AsNoTracking`, N+1, cartesian explosion, prevelik Include, split query, projekciju, client evaluation, generated SQL, pagination (offset vs keyset), raw SQL sa parametrima.

Kriticne invarijante pripadaju bazi kada je moguce. Za svaki kritican upis dokumentuj: sta se cita/validira/menja, invarijantu, concurrency, atomsku granicu, ponasanje pri neuspehu zavisnosti, rollback/kompenzaciju, audit. Testiraj lost update, write skew, duplu uplatu/porudzbinu/job, negativan inventory, duplu rezervaciju, parcijalnu operaciju.

Idempotency za retryable/spolja pokrenute upise: tenant/user-scoped key, fingerprint, unique constraint, sacuvan outcome, conflict response, atomic boundary sa business write ili transactional outbox.

Migracije su verzionsane izmene seme, ne automatski production side effect. Pregledaj generisani SQL pre primene. Production rollout: vlasnik, backup/restore verifikacija, lock/duration, rolling compatibility, backfill, forward repair, testiran rollback ili kompenzujuca migracija. Preferiraj pregledane SQL skripte ili migration bundle. Ne pozivaj `Database.Migrate()` sa svake production replike osim ako serijalizovan deployment dizajn dokazuje bezbednost. Ne izvrsavaj destruktivne migracije u auditu.

