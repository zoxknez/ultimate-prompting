## Faza 23 - Accessibility, internacionalizacija, SEO i PWA

Proveri kriticne tokove za korisnike, assistive tech, locale-e, crawler-e, offline stanja i vise tab-ova.

### Zahtevi audita

- Koristi semanticki HTML, ispravne name/role vrednosti, label-e, focus order, keyboard ponasanje, kontrast, target size, reduced motion i zoom.
- Testiraj loading, error, empty, validation, optimistic, modal, menu, table, virtualized, drag/drop, media i notification stanja.
- Proveri locale routing, fallback, RTL, pluralization, collation, vremensku zonu, datum, broj, valutu i hydration stabilnost.
- Auditiraj metadata, canonical, hreflang, robots, sitemap, status code-ove, redirect-e, structured data, social preview-e i soft 404.
- Inventarisi service worker, browser storage, offline mutation queue-eve, push, account switch, logout i multi-tab koordinaciju.
- Nikada ne cache-uj private HTML, RSC, API, export ili file podatke bez dokazanog identity binding-a i invalidacije.

### Obavezni dokazi

- Accessibility matrica sa automatizovanim i manuelnim dokazima.
- Locale/RTL/timezone/currency matrica za kriticne tokove.
- Renderovana metadata, status, canonical, robots, sitemap i structured-data capture-i.
- Browser storage, service-worker, offline queue i push lifecycle inventar.

### Obavezni failure i acceptance testovi

- Zavrsi tokove tastaturom, screen reader-om, 200 procenata zoom-a, reduced motion-om i high contrast-om.
- Promeni locale, RTL, vremensku zonu, valutu i velicinu fonta tokom server/client navigacije.
- Crawl-uj direktne i client-navigated stranice i uporedi status, metadata i vidljivi sadrzaj.
- Izloguj se i promeni account offline kroz vise tab-ova i proveri da nema data ili mutation leakage-a.

