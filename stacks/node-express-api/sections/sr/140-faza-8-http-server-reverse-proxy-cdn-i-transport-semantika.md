## Faza 8 - HTTP Server, Reverse Proxy, CDN I Transport Semantika

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Mapiraj client, CDN, WAF, load balancer, ingress, service mesh, reverse proxy, Node server i downstream hop-ove.
- Proveri request, headers, keep-alive, idle, body, upstream i shutdown timeout-e kroz sve hop-ove.
- Audituj HTTP/1.1, HTTP/2, TLS termination, ALPN, connection reuse, proxy protocol i forwarded header-e.
- Testiraj request smuggling, duplicate content-length, transfer-encoding dvosmislenost, malformed header-e i neslaganje hop-ova.
- Validiraj host, origin, absolute-form URL, path normalization, encoded separator-e i method override obradu.
- Proveri overload, slowloris, half-open connection, compression, range, cache i client-abort cleanup ponasanje.

### Obavezni Dokazi

- Proizvedi i sacuvaj hop-by-hop timeout i header matricu.
- Proizvedi i sacuvaj mapu trusted proxy-ja, TLS-a i parser konfiguracije.
- Proizvedi i sacuvaj rezultate smuggling i malformed-request testova.

### Obavezni Failure I Acceptance Testovi

- Dokazi da spoofed host i forwarded header-i se odbijaju ili normalizuju.
- Dokazi da spor klijent ne moze da zadrzi neogranicene resurse.
- Dokazi da proxy i aplikacija se slazu o request framing-u.

