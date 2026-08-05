## Faza 26 - Database migracije, backfill, mixed verzije i schema recovery

### Cilj

Dokaži forward-compatible schema evoluciju, ograničenu transformaciju podataka, observability, repair i recovery tokom stvarnih deployment-a.

### Zahtevi audita

- Inventariši Laravel, Doctrine, Phinx, custom SQL, online-schema, backfill, data-fix, trigger, view, function i search-index promene.
- Klasifikuj additive, compatibility, destructive, long-running, locking, rewrite, backfill i nepovratne operacije po engine-u i data scale-u.
- Koristi expand-and-contract sekvenciranje tako da stare i nove application ili worker verzije mogu da koegzistiraju tokom rollout i rollback prozora.
- Proveri default-e, nullability, index-e, constraint-e, generated vrednosti, trigger ponašanje, ORM metadata, serializaciju i read ili write kompatibilnost.
- Dizajniraj resumable, idempotent, rate-limited, observabilne backfill-eve sa checkpoint-ima, verification upitima, pause-om, retry-jem i reconciliation-om.
- Definiši rollback, forward repair, point-in-time recovery, data correction i manuelnu intervenciju za svaki migration failure mode.

### Obavezni dokazi

- Migration compatibility matrica kroz staru aplikaciju, novu aplikaciju, stari worker, novi worker i schema stanja.
- Production-like dokaz izvršavanja, lock-a, trajanja, backfill-a, pause-a, resume-a i verifikacije.
- Dokaz restore, forward-repair i data-reconciliation vežbe.

### Kriterijumi prihvatanja

- Nijedan rollout ili rollback prozor ne izlaže application verziju nekompatibilnoj schema-i.
- Dugotrajne i nepovratne promene podataka imaju ograničen uticaj, resumability, verifikaciju i recovery.

