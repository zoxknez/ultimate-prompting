## 13. Faza H - Podaci, Storage, Offline I Sinhronizacija

### 13.1 Room I Database Ispravnost

1. Pregledaj entity-je, primary key-eve, foreign key-eve, index-e, uniqueness, nullability, default-e, converter-e, view-e, FTS i embedded modele.
2. Proveri da query-ji koriste index-e i vracaju samo potrebne podatke na hot putanjama.
3. Detektuj main-thread pristup, N+1 pattern-e, unbounded read, cursor leak i ucitavanje velikih objekata.
4. Proveri da multi-step write operacije koriste transaction i cuvaju invarijante.
5. Proveri da conflict strategy odgovara poslovnoj semantici i ne odbacuje podatke precutno.
6. Pregledaj migration graph iz svake podrzane produkcione verzije.
7. Testiraj migracije sa stvarnim istorijskim semama i reprezentativnim podacima.
8. Proveri da se destructive fallback nikada ne koristi za korisnicke podatke bez eksplicitnog product odobrenja i recovery dizajna.
9. Proveri downgrade, backup, restore, prepackaged database, WAL, multi-process i encryption ponasanje gde je primenjivo.
10. Proveri da su schema export i migration testovi version-controlled.

### 13.2 DataStore, Fajlovi, Cache I Content

1. Proveri ownership preferences i typed DataStore-a, corruption handling, migracije i concurrency.
2. Ne cuvaj relacione ili velike mutable podatke u preferences.
3. Proveri da fajlovi koriste odgovarajuce internal, external, media ili shared storage API-je.
4. Proveri scoped storage, FileProvider putanje, URI permissions, MIME type i lifetime.
5. Spreci path traversal, arbitrary file overwrite, nebezbedno raspakivanje arhiva i izlaganje preko exported provider-a.
6. Proveri da cache ima granice, eviction, ownership, privacy, invalidation i low-storage ponasanje.
7. Proveri da backup i restore pravila iskljucuju tajne, ephemeral podatke, tokene i device-bound encrypted materijal.
8. Testiraj reinstall, clear data, restore, device transfer, account change i logout ponasanje.

### 13.3 Offline-First, Sync I Resavanje Konflikata

1. Definisi authoritative source za svaki tip podataka.
2. Proveri offline read, queued write, retry, ordering, idempotency, deduplication i conflict policy.
3. Proveri da se timestamp i version vector ne smatraju pouzdanim bez clock i server semantike.
4. Testiraj reconnect nakon partial write-a, duplicate delivery, process death-a, app update-a, token refresh-a i server konflikta.
5. Proveri da UI komunicira pending, synced, failed, stale i conflicted state.
6. Spreci infinite sync loop, battery drain, unbounded queue i silent data loss.
7. Proveri da WorkManager constraints i backoff odgovaraju poslovnoj hitnosti i zdravlju uredjaja.
8. Testiraj multi-device i multi-account ponasanje gde je primenjivo.

