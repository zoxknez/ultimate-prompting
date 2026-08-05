## Faza 6 - Router arhitektura, layout-i i navigacija

Mapiraj stvarni routing model i dokazi identitet ruta, layout lifetime, navigation semantiku i autorizaciju.

### Zahtevi audita

- Inventarisi App Router, Pages Router, mixed granice, group-e, parallel/intercepting rute, dynamic/catch-all segmente i locale-e.
- Mapiraj layout-e, template-e, loading, error, not-found, forbidden, unauthorized, default i global-error granice.
- Proveri precedence, kolizije, normalizaciju, trailing slash, basePath, locale, case, encoding i direct entry.
- Pregledaj Link, prefetch, refresh, back/forward, scroll, fokus, optimistic navigaciju i ne-sacuvane forme.
- Osiguraj da direktni URL-ovi, reload-i, alternativni locale-i i modal/intercepted rute sprovode identican ownership.
- Kada router-i koegzistiraju, testiraj cookie-je, error-e, serializaciju, navigaciju i pretpostavke shared komponenti.

### Obavezni dokazi

- Kompletna tabela ruta sa runtime, rendering, auth, tenant, cache, owner i SLO kolonama.
- Dijagram lifetime-a layout-a i error boundary-ja.
- Poredjenje direct-entry naspram client navigacije.
- Mixed-router matrica kompatibilnosti gde je primenljivo.

### Obavezni failure i acceptance testovi

- Poseti kriticne rute direktnim URL-om, client navigacijom, reload-om, back/forward akcijom i neautorizovanim deep link-om.
- Izvrsi encoded, malformed, duplicate-slash, locale i case varijante.
- Aktiviraj svako loading, missing, auth, local error i global error stanje.
- Dokazi da intercepted rute ne mogu zaobici auth ili izloziti stale parent-layout podatke.

