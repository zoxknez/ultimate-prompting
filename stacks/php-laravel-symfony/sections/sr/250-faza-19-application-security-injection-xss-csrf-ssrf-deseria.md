## Faza 19 - Application security, injection, XSS, CSRF, SSRF, deserializacija i zloupotreba

### Cilj

Identifikuj i proveri kontrole za attacker-controlled podatke, opasne interpreter-e, privilege granice i resource abuse.

### Zahtevi audita

- Mapiraj nepoverljive podatke u SQL, shell, template, HTML, URL, header, log, file putanju, regex, expression language, LDAP, XML, YAML, CSV i mail kontekste.
- Proveri parametrizaciju, contextual encoding, autoescape granice, trusted HTML postupanje, CSP, sanitizaciju, header bezbednost i formula-injection kontrole.
- Audituj CSRF za browser-authenticated mutation-e, SameSite pretpostavke, CORS, origin provere, login CSRF, logout CSRF i token lifecycle.
- Audituj SSRF kroz URL fetcher-e, preview-e, webhook-ove, importer-e, redirect-e, DNS rebinding, alternativnu IP sintaksu, metadata servise i interne protokole.
- Odbaci nebezbednu native deserializaciju, object injection, PHAR metadata zloupotrebu, nepoverljive YAML tagove, XML entity-je, dynamic class resolution i gadget chain-ove.
- Testiraj resource abuse kroz skupe regex-e, duboke strukture, velike kolekcije, decompression, obradu slika, export-e, search, paginaciju i konkurentne zahteve.
- Pregledaj debug rute, profiler, Telescope, Horizon, Pulse, Ignition, Symfony profiler, phpinfo, stack trace-ove, source map-e i izlaganje tajni.

### Obavezni dokazi

- Matrica nepoverljivog izvora do opasnog sink-a sa kontrolom i dokazom testa.
- Exploit-oriented negativni testovi za injection, XSS, CSRF, SSRF, deserializaciju, traversal i resource exhaustion.
- Produkcioni dokaz da su debug i diagnostic površine nedostupne ili odgovarajuće zaštićene.

### Kriterijumi prihvatanja

- Nijedna attacker-controlled vrednost ne stiže do interpreter-a, privilegovanog sink-a ili internog network cilja bez proverene kontrole.
- Malformed ili namerno skup input se odbacuje unutar ograničenog CPU, memory, time i downstream troška.

