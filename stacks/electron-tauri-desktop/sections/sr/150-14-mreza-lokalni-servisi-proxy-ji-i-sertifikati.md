## 14. Mreza, lokalni servisi, proxy-ji i sertifikati

### 14.1 Udaljeni mrezni pozivi

1. Popisi frontend, main/Rust, plugin, sidecar, updater, telemetry, crash, licensing, payment i installer network klijente.
2. Definisi connect, TLS, header, body, idle, stream, total i retry deadline-e. Propagiraj cancellation i razlikuj korisnicko otkazivanje od mreznog otkaza.
3. Retry samo bezbedne ili idempotentne operacije sa ogranicenim brojem pokusaja, exponential backoff-om, jitter-om, retry budget-om i postovanjem server rate-limit signala.
4. Validiraj redirect-e, finalni origin, content type, velicinu, sertifikat, proxy ponasanje i DNS promene za privilegovane download-e i update metadata.
5. Zastiti se od SSRF-a gde user-controlled URL-ovi mogu da dosegnu localhost, privatne opsege, metadata servise, Unix socket-e, named pipe-ove ili privilegovane lokalne endpoint-e.
6. Ne iskljucuj TLS verifikaciju globalno. Ako se koriste certificate pinning ili custom root-ovi, definisi rotaciju, expiry, backup trust, proxy kompatibilnost i recovery.
7. Rediguj authorization header-e, cookie-je, tokene, device identifikatore, license podatke, licni sadrzaj i query tajne iz logova i crash report-ova.
8. Testiraj offline, captive portal, DNS failure, proxy auth, TLS interception, istekao sertifikat, clock skew, slowloris, partial response, oversized response i retry storm.

### 14.2 Lokalni HTTP, socket, pipe i service interfejsi

1. Popisi svaki localhost listener, Unix socket, named pipe, loopback WebSocket, custom URI broker, privilegovani servis, browser callback server i developer port.
2. Bind-uj na najuzi interfejs i koristi OS dozvole, random nepredvidive endpoint-e, autentikaciju, origin provere, request seme, rate limit-e i lifecycle kontrole.
3. Ne pretpostavljaj da je localhost pouzdan. Browser-i, drugi korisnici, sandboxed aplikacije, malware i lokalna mrezna izlozenost mogu dosegnuti pogresno bind-ovane servise.
4. Zastiti se od DNS rebinding-a, browser cross-origin zahteva, CSRF-like lokalnih zahteva, predvidjanja port-a, stale socket fajlova, named-pipe squatting-a i service impersonation-a.
5. Validiraj peer identitet za privilegovanu service ili helper komunikaciju. Vezi zahteve za trenutnu app instancu, korisnika, session, verziju i namenjenu operaciju.
6. Definisi startup race, konflikte port-a, redosled upgrade-a servisa, version handshake, reconnect, graceful shutdown i orphan cleanup.
7. Nikada ne izlaži genericke shell, filesystem, database, update ili credential funkcije preko lokalnog endpoint-a bez jake autentikacije i uske autorizacije.
8. Testiraj neautentifikovane lokalne zahteve, cross-origin browser zahteve, drugog OS korisnika, stale klijent, pogresnu verziju, replay, oversized payload, spor klijent i process crash.

