## 12. Mreza, API, realtime i fajlovi

### 12.1 Mrezni ugovor
- Popisi svaki base URL, protokol, klijent, interceptor, proxy, certificate policy, redirect pravilo, timeout, retry, cache i offline ponasanje.
- Definisi connect, TLS, write, read, total, idle, upload, download i background-transfer timeout-e.
- Koristi ograniceni retry samo za klasifikovane prolazne greske i uzmi u obzir idempotentnost, retry budget, jitter, deadline i preopterecenje servera.
- Auditiraj obradu redirect-a, validaciju hostname-a, proxy konfiguraciju, lifecycle certificate pinning-a, custom trust store i debug izuzetke.
- Validiraj response schemu, content type, velicinu, kompresiju, encoding, pagination, cursor, error ugovor i partial-response ponasanje.
- Testiraj captive portal, DNS failure, TLS rotaciju, sporu mrezu, network handoff, airplane mode, metered vezu i version skew servera.

### 12.2 Upload, download, import i export
- Validiraj izvor, putanju, URI scheme, MIME type, extension, magic bytes, velicinu, broj, filename i dozvolu za svaku operaciju sa fajlom.
- Koristi streaming i ogranicen buffer za velike fajlove; auditiraj privremene fajlove, partial fajlove, cleanup, resume, integritet i ponasanje kada je disk pun.
- Testiraj content URI, security-scoped URL, cloud-provider fajl, removable storage, shared storage, opozvanu dozvolu i stale bookmark scenario.
- Tretiraj parser slike, medija, PDF-a, arhive, dokumenta, CSV-a, fonta i native codec-a kao granice za hostile input.
- Zastiti od path traversal-a, zip slip-a, decompression bomb-e, prevelikih dimenzija, parser hang-a, malformed metadata i izvrsnog sadrzaja.
- Proveri serversku autorizaciju, malware skeniranje gde je potrebno, potvrdu integriteta, reconciliation i korisniku vidljiv konacni status.

