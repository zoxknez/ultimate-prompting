## Faza 10 - Data fetching, streaming i server rad

Mapiraj svako server citanje, identity ulaze, consistency, lifecycle, timeout budget, cache i rendering posledicu.

### Zahtevi audita

- Inventarisi fetch, ORM/database pozive, GraphQL, SDK-ove, filesystem citanja, interni HTTP i service pristup.
- Za svako citanje zabelezi actor-a, tenant-a, parametre, autorizaciju, consistency, cache, timeout, retry, cancellation i fallback.
- Detektuj waterfall-e, duple fetch-eve, skrivene layout zavisnosti, metadata dupliranje, unbounded fan-out i per-row pozive.
- Koristi paralelizam samo sa eksplicitnim downstream kapacitetom, cancellation-om, ordering-om i partial-failure semantikom.
- Pregledaj Suspense i streaming za koristan napredak, stabilan layout, privatnost, error izolaciju i crawler ponasanje.
- Izbegavaj server-to-self javni HTTP osim ako su trust, latency, auth i deployment implikacije dokazane.

### Obavezni dokazi

- Read-path inventar sa consistency, timeout, cache i owner kolonama.
- Trace timeline za reprezentativne kriticne stranice.
- Query-plan i downstream-call dokaz za skupe putanje.
- Cancellation i timeout propagation dokaz.

### Obavezni failure i acceptance testovi

- Ubrizgaj sporu zavisnost i dokazi deadline-e, fallback i partial rendering.
- Prekini konekciju tokom streaming-a i proveri cancellation ili namerno zavrsavanje.
- Obori jednu granu paralelnog citanja i proveri izolaciju i consistency.
- Koristi production-like obim podataka i proveri bounded query-je, fan-out, latency i memoriju.

