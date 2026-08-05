## 20. Isolate-i, worker-i i teška obrada

Koristi izolaciju namerno i proveri trošak poruka, memorije i lifecycle-a.

- Popiši `Isolate.spawn`, `Isolate.run`, `compute`, background plugin entrypoint-e, native worker thread-ove i web worker-e.
- Proveri dostupnost entrypoint-a, tree-shaking anotacije gde su potrebne, inicijalizaciju, registraciju plugin-a, dostupnost zavisnosti i platformska ograničenja.
- Audituj serializaciju poruka, TransferableTypedData, trošak kopiranja, vlasništvo objekata, verzionisanje protokola, malformirane poruke i gašenje.
- Spreči isolate-e da koriste nepodržane UI binding-e, zastarele kredencijale, pogrešan tenant kontekst, neinicijalizovano skladište ili native resurse koji nisu isolate-safe.
- Definiši cancellation, timeout, progress, propagaciju crash-a, restart, queue limite i cleanup za dugotrajni rad.
- Profiluj da li izolacija poboljšava odzivnost nakon startup, copy, scheduling i memory overhead-a.
- Na web-u proveri dostupnost worker-a, CSP, putanje asset-a, browser podršku, fallback i cross-origin isolation zahteve.
- Zahtevaj load, cancellation, termination, malformed-message i ponovljene start/stop testove.

