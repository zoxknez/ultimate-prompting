## Faza 8 - Server Components, Client Components i RSC granice

Auditiraj trust, serializaciju, bundle, data i lifecycle granice izmedju server i browser koda.

### Zahtevi audita

- Inventarisi use client granice, server-only/client-only module, barrel-e, dynamic import-e i third-party komponente.
- Proveri da tajne, privilegovani klijenti, private env vrednosti, tokeni i database objekti nikada ne ulaze u client bundle ili prop-ove.
- Smanji client island-e prema izmerenoj potrebi interakcije, ne prisilnim prebacivanjem browser-dependent UI-ja na server.
- Pregledaj RSC payload velicinu, duple podatke, privatna polja, error leakage i compatibility serializacije.
- Detektuj ponovljen server rad po komponenti, layout-u, metadata generisanju, request-u ili prefetch-u.
- Tretiraj RSC i framework advisory-je kao obavezne patch i regression-test ulaze.

### Obavezni dokazi

- Server/client boundary mapa sa bundle ownership-om i serializovanim tipovima.
- Client bundle scan za zabranjene module, env vrednosti i osetljive stringove.
- RSC payload capture-i za javne, autentifikovane, tenant i admin rute.
- Patch dokaz za React, react-dom, Next.js i RSC advisory-je.

### Obavezni failure i acceptance testovi

- Pretrazi client asset-e i RSC payload-e za seeded secret canary-je.
- Promeni korisnike i tenant-e i dokazi da payload ili layout state ne prelazi identity granice.
- Izvrsi malformed RSC/navigation request-e podrzane harness-om i proveri bezbedan failure.
- Izmeri JS i RSC payload pre i posle boundary promena.

