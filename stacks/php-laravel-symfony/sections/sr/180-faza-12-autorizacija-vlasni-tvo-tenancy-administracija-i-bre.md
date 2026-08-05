## Faza 12 - Autorizacija, vlasništvo, tenancy, administracija i break-glass

### Cilj

Dokaži serverske permission, ownership, tenant isolation, delegated access i emergency privilege granice.

### Zahtevi audita

- Mapiraj svaku privilegovanu rutu, komandu, job, poruku, export, fajl, webhook, admin akciju, support akciju i interni endpoint na eksplicitnu policy.
- Proveri autorizaciju posle canonical učitavanja resursa i pre svakog read-a, mutation-a, side effect-a, serializacije, cache hit-a i download-a.
- Testiraj BOLA i IDOR kroz route binding, nested resurse, UUID ili slug lookup, bulk endpoint-e, indirektne reference i soft-deleted zapise.
- Audituj propagaciju tenant scope-a kroz ORM upite, raw SQL, cache ključeve, sesije, queue-ove, notification-e, search index-e, fajlove, logove i analytics.
- Pregledaj role i permission mutation, invitation, prenos vlasništva, spajanje organizacija, account switching, impersonation i delegated access.
- Zahtevaj vremenski ograničen, odobren, snažno autentikovan, logovan, pregledljiv i opoziv break-glass pristup sa naknadnom revizijom.

### Obavezni dokazi

- Authorization matrica endpoint-a i operacija uključujući tenant i ownership dimenzije.
- Cross-tenant i lower-privilege negativni testovi kroz HTTP, CLI, queue, cache, storage, search i export putanje.
- Dokaz break-glass odobrenja, korišćenja, isteka, opoziva i revizije.

### Kriterijumi prihvatanja

- Nijedan identifikator, binding prečica, cache hit, queued job ili interna ruta ne zaobilazi resource-level autorizaciju.
- Tenant podaci i ovlašćenja ostaju izolovani kroz retry, reuse worker-a, export-e, backup-e, logove i recovery.

