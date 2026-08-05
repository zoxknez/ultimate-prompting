## 19. Mreža, TLS, autentikacija, retry i streaming

### 19.1 Obim audita

1. Inventariši QNetworkAccessManager instance, Python HTTP klijente, WebSocket/SSE/gRPC klijente, proxy konfiguraciju, DNS, certificate store-ove i custom transporte.
2. Zabeleži connection, TLS, request, read, write, total, idle i pool-acquisition timeout-e plus cancellation i deadline propagation.
3. Pregledaj validaciju sertifikata, hostname verification, redirect-e, proxy autentikaciju, client sertifikate, pinning gde je opravdan i ponašanje rotacije.
4. Proceni pribavljanje tokena, serializaciju refresh-a, expiry, revocation, logout, promenu naloga, MFA/passkey tokove i bezbedan browser handoff.
5. Proveri klasifikaciju retry-ja, idempotency, jitter, budget, circuit breaking, offline queueing, reconnect, resume, duplu isporuku i replay.
6. Za streaming i velike transfere pregledaj backpressure, partial fajlove, checksum-e, disk limite, sparse fajlove, cancellation, resume metadata i cleanup.

### 19.2 Obavezna verifikacija

1. Testiraj spor DNS, TLS kvar, rotaciju sertifikata, promene proxy-ja, captive portal, offline tranziciju, packet loss, partial odgovor, malformed odgovor i server throttling.
2. Pokreni konkurentne expiry i refresh scenarije da dokažeš jednu bezbednu refresh putanju i pravilno propagation kvara.
3. Verifikuj da retry ne duplira kupovine, write operacije, upload-e, download-e, komande uređaju ili lokalne tranzicije stanja.
4. Izmeri rast queue-a, memoriju, disk, UI responsiveness i oporavak tokom dugih ili zaglavljenih transfera.
5. Potvrdi da tajne i osetljivi payload-i ne postoje u URL-ovima, proxy logovima, debug trace-ovima, crash izveštajima, telemetriji i support bundle-ovima.

