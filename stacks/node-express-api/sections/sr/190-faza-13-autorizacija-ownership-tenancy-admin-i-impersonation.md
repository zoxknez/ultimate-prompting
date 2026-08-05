## Faza 13 - Autorizacija, Ownership, Tenancy, Admin I Impersonation

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Napravi authorization matricu za svaku rutu, job, query, fajl, cache key, poruku, export, search i admin akciju.
- Odvoji identity, role, permission, ownership, tenant, resource state, relationship i contextual policy provere.
- Primeni owner i tenant constraint-e u autoritativnim query-jima ili komandama, ne samo u fetch-then-check logici.
- Testiraj BOLA, BFLA, cross-tenant enumeraciju, batch endpoint-e, nested resurse, indirektne reference i alternativne media type-ove.
- Definisi admin, support, delegated access, impersonation i break-glass approval, scope, razlog, expiry, audit i review.
- Proveri tenant izolaciju kroz cache, queue, storage, telemetry, logove, greske, background job-ove i reconciliation.

### Obavezni Dokazi

- Proizvedi i sacuvaj route-resource authorization matricu.
- Proizvedi i sacuvaj tenant data-flow i negative-test mapu.
- Proizvedi i sacuvaj admin, support i impersonation registar.

### Obavezni Failure I Acceptance Testovi

- Dokazi da cross-tenant object identifikatori se odbijaju bez curenja informacije o postojanju.
- Dokazi da stale role cache ne moze da sacuva opozvan pristup.
- Dokazi da background job-ovi i admin putanje cuvaju tenant scope i audit.

