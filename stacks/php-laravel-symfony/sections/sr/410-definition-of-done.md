## Definition of Done

1. Scope, pretpostavke, izuzeci, okruženja, runtime režimi, owner-i i ograničenja dokaza su eksplicitni.
2. Namenjeni source, build input-i, zavisnosti, generated code, artifact, deployment, schema i pokrenuti procesi su kriptografski ili operativno povezani.
3. Sve kritične HTTP, console, queue, scheduler, webhook, file, admin, support i recovery površine su inventarisane i autorizovane.
4. Poslovne invarijante preživljavaju konkurentnost, retry, duplicate delivery, partial failure, crash, timeout, cancellation i mixed-version izvršavanje.
5. Autoritet i recovery ponašanje baze, cache-a, sesije, queue-a, storage-a, search-a i spoljnog provider-a su dokazani.
6. Framework-specific lifecycle, proxy, container, policy, voter, middleware, worker i cache semantika je testirana iz produkcionog artifact-a.
7. Security granice izdržavaju exploit-oriented negativne testove i abusive resource obrasce.
8. Kapacitet i pouzdanost su izmereni pod reprezentativnim cold, burst, sustained, soak, slowdown, failover i overload uslovima.
9. Observability detektuje i objašnjava correctness, security, availability, latency, queue, data, release i recovery kvarove.
10. Produkcioni artifact je reproducibilan, minimalan, immutable, potpisan ili verifikovan, promovisan bez rebuild-a i bezbedno zamenljiv.
11. Rollout, rollback, forward repair, opoziv kredencijala, izolovani restore, incident containment i trusted rebuild su izvršivi i testirani.
12. Finalna odluka, residual risk-ovi, izuzeci, owner-i, rokovi, dokazi i datum sledeće verifikacije su zabeleženi.

Ako bilo koja stavka nije dokazana, audit nije završen. Označi je kao `UNVERIFIED`, objasni rizik i odrazi ga u finalnoj readiness odluci.

