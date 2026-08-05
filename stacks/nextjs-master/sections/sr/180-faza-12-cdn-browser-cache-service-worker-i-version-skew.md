## Faza 12 - CDN, browser cache, service worker i version skew

Auditiraj cache-eve van application koda i dokazi koherentno ponasanje kroz deployment-e, regione, tab-ove, browser-e i offline stanja.

### Zahtevi audita

- Inventarisi CDN pravila, surrogate key-eve, Cache-Control, Vary, cookie-je, auth header-e, image optimizaciju, static asset-e, HTML i RSC cache.
- Dokazi da public response-i ne variraju po nenavedenim identity ulazima i da private response-i ne mogu postati public.
- Mapiraj service-worker precache, runtime rute, navigation fallback, API caching, aktivaciju i cleanup.
- Spreci stari HTML koji referencira obrisane asset-e, nove klijente koji pozivaju nekompatibilne stare servere i stare tab-ove koji salju nekompatibilne mutation-e.
- Koristi deployment ID, zadrzavanje asset-a, compatibility prozore ili eksplicitan reload handling.
- Pregledaj multi-region propagation, purge kasnjenje, stale-if-error, CDN outage i origin shielding.

### Obavezni dokazi

- Efektivni header-i za public, autentifikovane, tenant, error, redirect i RSC response-e.
- Service-worker route i cache inventar sa privacy klasom.
- Old/new deployment kompatibilnost i politika zadrzavanja asset-a.
- Regionalna purge i propagation merenja.

### Obavezni failure i acceptance testovi

- Drzi stari tab otvoren kroz deployment i izvrsi citanja, write operacije, navigaciju i reload.
- Namerno posluzi stale HTML ili RSC i proveri version-skew zastitu.
- Idi offline, azuriraj service worker, ponovo se povezi i proveri bezbednost privatnih podataka i mutation-a.
- Odlozi jedan regionalni purge i dokazi bounded nekonzistentnost ili traffic izolaciju.

