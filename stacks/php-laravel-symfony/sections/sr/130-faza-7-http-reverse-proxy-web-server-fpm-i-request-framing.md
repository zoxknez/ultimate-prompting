## Faza 7 - HTTP, reverse proxy, web server, FPM i request framing

### Cilj

Proveri end-to-end HTTP semantiku i spreči neslaganja između network hop-ova i application parsing-a.

### Zahtevi audita

- Mapiraj client, CDN, WAF, load balancer, ingress, reverse proxy, web server, FastCGI, FPM pool i application limite i timeout-e.
- Audituj trusted proxy konfiguraciju, forwarded header-e, client IP, scheme, host, port, prefix, absolute URL-ove i generisanje redirect-a.
- Testiraj duplirani `Content-Length`, konfliktni `Transfer-Encoding`, malformed header-e, encoded putanje, null byte-ove, path normalization, method override i smuggling odbrane.
- Proveri body, header, URI, multipart, file, decompression, execution, idle, upstream, keepalive i shutdown limite kroz sve hop-ove.
- Audituj Nginx ili Apache FastCGI parametre, razrešavanje script putanje, document root, static handling, internal redirect-e, error page-ove i source disclosure.
- Proveri client disconnect, aborted request, output buffering, streaming, SSE, large response i partial-response cleanup semantiku.

### Obavezni dokazi

- Hop-by-hop matrica timeout-a i size limit-a.
- Trusted proxy i effective URL dokaz koristeći stvarnu deployment topologiju.
- Negativni protocol testovi na edge i application granici.

### Kriterijumi prihvatanja

- Nijedan untrusted hop ne može da spoof-uje identitet, scheme, host, tenant, rate-limit ključ ili secure-cookie ponašanje.
- Request framing i timeout politika sprečavaju dvosmisleno parsing ponašanje i iscrpljivanje resursa.

