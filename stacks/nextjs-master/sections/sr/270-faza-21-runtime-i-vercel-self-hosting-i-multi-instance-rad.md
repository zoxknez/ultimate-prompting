## Faza 21 - Runtime-i, Vercel, self-hosting i multi-instance rad

Tretiraj Node, Edge, serverless, container-e, Vercel i adapter-e kao posebne proizvode sa razlicitim garancijama.

### Zahtevi audita

- Inventarisi runtime po ruti, akciji, handler-u, metadata zadatku, image putanji, job-u i funkciji.
- Proveri API-je, native module, WASM, crypto, filesystem, socket-e, driver-e, telemetry i SDK podrsku u svakom runtime-u.
- Ne oslanjaj correctness na warm instance, globale, lokalnu perzistenciju, in-memory lock-ove, counter-e, sesije ili cache.
- Mapiraj duration, CPU, memoriju, payload, streaming, connection, region, cold start, concurrency i billing limite.
- Za Vercel proveri project linkage, env scope-ove, domene, alias-e, deployment protection, regione, funkcije, cache i pristup.
- Za self-hosting proveri standalone output, traced fajlove, asset-e, proxy header-e, health, signal-e, shared cache, deploymentId, draining i retention.

### Obavezni dokazi

- Route-to-runtime i capability matrica.
- Izmereni cold/warm latency, memorija, duration, payload i concurrency.
- Platform project ili container konfiguracija vezana za deployment.
- Multi-instance cache, deployment ID, draining i asset-retention dokaz.

### Obavezni failure i acceptance testovi

- Izazovi cold start-ove, scale-out, nagli termination, old/new overlap i promene regiona.
- Pokreni svaku Edge rutu protiv detekcije nepodrzanih API-ja i zavisnosti.
- Iscrpi database connection-e pod serverless burst-om.
- Prekini mutation posle commit-a ali pre response-a i proveri idempotent recovery.

