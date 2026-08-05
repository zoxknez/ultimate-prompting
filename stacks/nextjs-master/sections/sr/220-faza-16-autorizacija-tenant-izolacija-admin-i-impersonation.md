## Faza 16 - Autorizacija, tenant izolacija, admin i impersonation

Dokazi object, action, tenant i administratorsku autorizaciju na svakoj data i mutation granici.

### Zahtevi audita

- Napravi authz matricu za svaku rutu, akciju, handler, query, fajl, cache, poruku, export, search i admin operaciju.
- Izvedi actor-a i tenant-a iz trusted sesije ili server context-a, nikada samo iz client ID-ja.
- Sprovodi ownership u autoritativnim query-jima i constraint-ima, ne fetch-then-check obrascima.
- Proveri role, permission, plan, feature, region, data class i state-transition constraint-e nezavisno.
- Auditiraj support, admin, impersonation, delegated access, break-glass, approval, marking, audit, expiry i review.
- Spreci tenant leakage kroz globale, module cache-eve, singleton-e, job-ove, retry-je, telemetry, error-e i linkove.

### Obavezni dokazi

- Route/action/resource authorization matrica sa negativnim slucajevima.
- Autoritativni query i constraint dokaz za ownership.
- Admin/impersonation approval, audit, expiry i revocation dokaz.
- Cross-tenant cache, queue, file, export i search isolation dokaz.

### Obavezni failure i acceptance testovi

- Promeni resource ID, tenant, rolu, plan, state i ownership iz nize privilegije.
- Pokusaj direct route, action, API, file, export, search i cache pristup preko tenant-a.
- Ukloni privilegiju tokom aktivne sesije i in-flight mutation-a.
- Pokreni impersonation kroz deployment i vise tab-ova i proveri marking, expiry, ogranicenja i audit.

