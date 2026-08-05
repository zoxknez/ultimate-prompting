## Faza 22 - Performanse, Core Web Vitals, kapacitet i trosak

Optimizuj iz izmerenih user, browser, server, database, cache, network i cost dokaza.

### Zahtevi audita

- Izmeri field i lab LCP, INP, CLS, TTFB, navigaciju, hydration, RSC payload, JS, CSS, slike, fontove, third party-je i long task-ove.
- Razlozi latency na queue, cold start, Proxy, auth, cache, database, dependency, rendering, streaming i network.
- Postavi budget-e za JS, route chunk-ove, RSC payload, slike, fontove, third-party rad, memoriju, query-je i external pozive.
- Auditiraj image sizing, formate, remote pattern-e, priority, transformacije, cache, cost i abuse.
- Auditiraj font loading, subset, fallback, variable fontove, preload, shift, privatnost i self-hosting.
- Testiraj cold, warm, burst, sustained, soak, failover, cache-cold i dependency-brownout scenarije.

### Obavezni dokazi

- Field CWV po ruti, uredjaju, geografiji, browser-u, release-u i user state-u.
- Bundle, RSC, image, font, query, call, memory, CPU i cost profili.
- Capacity model sa saturacijom, headroom-om, scaling-om i load shedding-om.
- Pre/posle dokaz za svaku performance promenu.

### Obavezni failure i acceptance testovi

- Pokreni kriticne tokove na low-end mobile, desktop, sporoj mrezi, visokom latency-ju i auth stanjima.
- Prekoraci svaki budget i dokazi da ga CI, alerting ili admission detektuje.
- Optereti cold cache-eve i instance dok je zavisnost degradirana.
- Proveri da load shedding stiti kriticne write operacije i recovery pre saturacije.

