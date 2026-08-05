## Faza 16 - Cache, sesije, lock-ovi, fajlovi, object storage i search

### Cilj

Audituj izvedeno stanje, distribuiranu koordinaciju, storage authority, invalidaciju, izolaciju i recovery.

### Zahtevi audita

- Inventariši application cache, HTTP cache, session cache, tag cache, ORM cache, rate-limit stanje, distributed lock-ove, filesystem-e, object store-ove i search index-e.
- Proveri da cache ključevi uključuju svaku authorization, tenant, locale, currency, feature, schema i representation dimenziju koja menja rezultat.
- Audituj TTL, invalidaciju, stampede kontrolu, stale ponašanje, negative caching, compatibility serializacije, poisoning i regionalnu konzistentnost.
- Pregledaj availability session storage-a, konzistentnost, locking, fixation otpornost, serializaciju, failover, expiry i deployment kompatibilnost.
- Tretiraj distributed lock-ove kao lease; proveri ownership, renewal, expiry, fencing, clock pretpostavke, split brain i stale-owner ponašanje.
- Audituj file i object autorizaciju, namespace izolaciju, signed URL scope, retention, versioning, enkripciju, malware postupanje, konzistentnost i restore.
- Proveri search indexing authority, tenant filtere, propagaciju brisanja, stale rezultate, reindex, alias cutover i reconciliation.

### Obavezni dokazi

- Matrica autoriteta cache-a, sesije, lock-a, storage-a i search-a.
- Cross-tenant, stale-cache, stampede, lease-expiry, failover, deletion i reindex testovi.
- Restore i reconciliation dokaz za authoritative i derived store-ove.

### Kriterijumi prihvatanja

- Izvedeno stanje ne može da dodeli pristup, pređe tenant granice ili postane neispratljiv source of truth.
- Lease expiry, gubitak cache-a, storage failover ili search lag degradira bezbedno i observabilan je.

