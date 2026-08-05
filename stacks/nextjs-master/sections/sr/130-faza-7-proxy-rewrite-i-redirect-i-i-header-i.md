## Faza 7 - Proxy, rewrite-i, redirect-i i header-i

Tretiraj Proxy ili legacy Middleware kao routing infrastrukturu, nikada kao jedinu security granicu.

### Zahtevi audita

- Inventarisi proxy.ts, middleware.ts, matcher-e, negativne matcher-e, locale logiku, auth redirect-e, eksperimente i bot handling.
- Proveri semantiku verzije, runtime ogranicenja, API podrsku, redosled izvrsavanja i interakciju sa platformskim routing-om.
- Detektuj matcher rupe za encoded putanje, alternativne host-ove, handler-e, image rute, RSC request-e i slash varijante.
- Validiraj host, forwarded host, protokol, origin, locale, tenant i redirect cilj prema trusted config-u.
- Spreci open redirect, loop, cache poisoning, header spoofing, auth confusion i tenant crossover.
- Ponovo proveri autorizaciju u destination ruti, data layer-u i mutation-u.

### Obavezni dokazi

- Matcher truth tabela koja pokriva zasticene i iskljucene klase putanja.
- Posmatrani routing redosled i efektivni response header-i.
- Trusted proxy i host konfiguracioni dokaz.
- Middleware-to-Proxy migration status gde je relevantno.

### Obavezni failure i acceptance testovi

- Pokusaj zasticene putanje kroz encoded, rewritten, alternate-host, prefetch, RSC i direct API varijante.
- Testiraj nepoverljive Host, X-Forwarded-Host, Origin i protocol kombinacije.
- Dokazi da redirect ciljevi ne mogu napustiti allowlist-u ili napraviti petlju.
- Zaobidji Proxy u integration testu i dokazi da destination odbija neautorizovan pristup.

