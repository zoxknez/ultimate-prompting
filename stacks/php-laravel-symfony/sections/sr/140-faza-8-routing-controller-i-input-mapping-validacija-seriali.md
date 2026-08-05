## Faza 8 - Routing, controller-i, input mapping, validacija, serializacija i API ugovori

### Cilj

Dokaži da se svaki request mapira, validira, autorizuje, izvršava i serializuje prema eksplicitnom ugovoru.

### Zahtevi audita

- Popiši rute, hostove, metode, domene, prefikse, middleware, default-e, requirements, model binding, parameter conversion, fallback rute i prioritete.
- Otkrij route shadowing, dvosmislene metode, nebezbedne wildcard rute, slučajne javne endpoint-e, debug rute i environment-only rute u produkciji.
- Validiraj path, query, header, cookie, body, multipart, file, JSON, XML, form, CLI, message i webhook input u runtime-u.
- Odvoji strukturnu validaciju, semantičku validaciju, autorizaciju, ownership provere, state provere i spoljne lookup-e.
- Spreči mass assignment eksplicitnim DTO-ovima, request objektima, allowlist-ama, serializer grupama, writable-field politikama i domain komandama.
- Proveri response šeme, error-e, Problem Details, paginaciju, filtering, sorting, expansion, includes, field mask-e, versioning i generisane klijente.

### Obavezni dokazi

- Matrica ruta i komandi sa autentikacijom, autorizacijom, tenant-om, validacijom, transakcijom, idempotency-jem, limitima i testovima.
- OpenAPI ili ekvivalentni contract diff prema stvarnom runtime ponašanju.
- Negativni testovi za malformed, oversized, ambiguous, unauthorized i cross-tenant input.

### Kriterijumi prihvatanja

- Nijedan kritični endpoint se ne oslanja na PHP tipove, UI ograničenja ili ORM fillable default-e kao jedinu runtime validaciju.
- Javni i machine ugovori su versioned, ograničeni, testirani i kompatibilni ili eksplicitno migrirani.

