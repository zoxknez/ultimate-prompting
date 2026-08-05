## Faza 17 - Bezbednost aplikacije, browser bezbednost i abuse otpornost

Proveri stvarno response i runtime ponasanje, ne samo nameru konfiguracije.

### Zahtevi audita

- Proveri CSP, nonce/hash strategiju, HSTS, frame zastitu, Referrer-Policy, Permissions-Policy, COOP, COEP, CORP i MIME zastite.
- Inventarisi HTML, Markdown, rich text, MDX, embed-e, SVG, URL rendering i svaki opasan HTML sink.
- Validiraj i canonicalize-uj URL-ove, redirect-e, host-ove, protokole, putanje, nazive fajlova, object key-eve i outbound destination-e.
- Spreci SSRF destination politikom, DNS/IP proverama, redirect revalidacijom, private-network kontrolama, protocol limitima i egress kontrolama.
- Pregledaj CSRF za cookie-auth mutation-e, CORS, host/origin validaciju, same-site pretpostavke i alternativne klijente.
- Zastiti login, reset, invitation, verification, akcije, API-je, search, upload, export, skup rendering i third-party trosak.

### Obavezni dokazi

- Posmatrani security header-i i CSP violation dokaz.
- Input/output/URL/file/outbound trust-boundary inventar.
- Rate-limit key, scope, storage, bypass, failure i capacity dokaz.
- Reachability i patch dokaz za relevantne advisory-je.

### Obavezni failure i acceptance testovi

- Ubrizgaj script, URL, SVG, Markdown, rich-text, header i template payload-e.
- Testiraj SSRF kroz IP adrese, redirect-e, encoded host-ove, protokole i metadata ciljeve u izolaciji.
- Testiraj rate-limit bypass po account-u, tenant-u, IP-u, sesiji, alias-u, regionu i distribuiranoj konkurentnosti.
- Pokreni regresije izvedene iz aktuelnih Next.js, React, RSC, auth, parser i platform advisory-ja.

