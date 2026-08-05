## Faza 11 - Cache Components, kljucevi, invalidacija i privatnost

Tretiraj svaki cache kao data-sharing granicu. Dokazi potpunost kljuca, privatnost, freshness, invalidaciju, failure i observability.

### Zahtevi audita

- Identifikuj cache semantiku tacne verzije, cacheComponents, use cache/private/remote, fetch ponasanje, route cache, memoization i platformske cache-eve.
- Definisi ulaze kljuca ukljucujuci tenant, korisnika, rolu, locale, valutu, flag-ove, dozvole, data verziju i auth-sensitive context.
- Klasifikuj entry-je kao public, tenant-shared, user-private, request-private ili zabranjene za cache.
- Definisi TTL, stale politiku, cache life, tag-ove, path invalidaciju, update ordering i tolerisanu zastarelost.
- Spreci stampede, hot-key overload, cache penetration, invalidation storm i unbounded cardinality.
- Proveri outage, eviction, regionalnu replikaciju, deployment namespace, schema promenu i rollback ponasanje.

### Obavezni dokazi

- Cache inventar i tabela derivacije kljuca.
- Posmatrani TTL, header-i, hit/miss, stale, invalidacija i regionalno ponasanje.
- Dokaz da privatni i tenant podaci ne mogu da se sudare.
- Invalidation trace od autoritativnog write-a do svih reprezentacija.

### Obavezni failure i acceptance testovi

- Menjaj korisnike, role, tenant-e, locale-e i flag-ove na istom URL-u.
- Izvrsi write tokom stale serving-a i proveri bounded freshness i ordering.
- Simuliraj cache outage i cold restart pod opterecenjem bez kolapsa baze.
- Deploy-uj nekompatibilnu cache schemu i dokazi namespace izolaciju ili kontrolisanu invalidaciju.

