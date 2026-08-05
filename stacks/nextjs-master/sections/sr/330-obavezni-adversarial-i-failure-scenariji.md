## Obavezni adversarial i failure scenariji

Izvrsi svaki primenljiv scenario bezbedno. Blokiran scenario ostaje UNVERIFIED sa tacnim blocker-om, rizikom i evidence planom.

- **S1** - Cross-user i cross-tenant citanja kroz URL, cache, RSC, fajl, export, search i job-ove.
- **S2** - Privilege escalation kroz rute, akcije, API-je, hidden polja, bound argumente i stale sesije.
- **S3** - Duplicate/concurrent mutation-e iz tab-ova, uredjaja, retry-ja, redirect-a, timeout-a i restart-a.
- **S4** - Crash pre commit-a, tokom ambiguity-ja, posle commit-a pre response-a i pre acknowledgement-a.
- **S5** - Old/new browser, server, schema, cache, session, action, queue i service worker overlap.
- **S6** - Cold-cache i cold-runtime burst sa degradiranom bazom, provider-om ili regionom.
- **S7** - Nested retry i reconnect petlje koje amplifikuju request-e, queue-eve, payment-e, email ili cost.
- **S8** - Dependency timeout, malformed/oversized response, redirect, DNS, sertifikat i partial success.
- **S9** - Client disconnect tokom streaming-a, upload-a, akcije, database rada i spoljnog efekta.
- **S10** - Memory, CPU, event-loop, connection, descriptor, bandwidth, queue i quota exhaustion.
- **S11** - Rotacija kljuca, tokena, cookie-ja, tajne, sertifikata, action encryption-a i provider credential-a.
- **S12** - Zlonamerni HTML, Markdown, SVG, URL, redirect, fajl, arhiva, webhook, parser, RSC i SSRF.
- **S13** - Proxy matcher bypass kroz putanje, host-ove, locale-e, tipove ruta, RSC request-e i rewrite-e.
- **S14** - Offline account switch, logout, vise tab-ova, worker update, stale HTML i queued konflikti.
- **S15** - Migration interruption, mixed-version citanja/write operacije, validacija, rollback pokusaj i repair.
- **S16** - Observability outage, redaction failure, cardinality spike, source-map exposure i evidence preservation.
- **S17** - Untrusted PR, kompromitovana zavisnost, poisoned cache, mutable artefakt i release credential kompromitacija.
- **S18** - Traffic rollback posle nepovratnih data, cache, email, payment, queue, file ili worker efekata.
- **S19** - Izolovani restore sa kljucevima, schemom, object storage-om, queue-evima, search-om, cache warmup-om i tenant proverom.
- **S20** - Framework/RSC emergency advisory koji zahteva containment, patch, canary, rollback i trusted rebuild.

