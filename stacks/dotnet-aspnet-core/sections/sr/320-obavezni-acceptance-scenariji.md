## Obavezni Acceptance Scenariji

Pokreni ili eksplicitno oznaci kao blokirano i `NEPROVERENO` za svaki primenljiv scenario:

1. neautorizovan, pogresna role, pogresan tenant, pogresan owner, nevalidno stanje, istekao/opozvan credential i cross-resource pristup;
2. dupli i konkurentni kriticni write, retry posle timeout-a, parcijalni spoljni kvar, crash oko commit-a i stale client update;
3. nedostajuca ili rotirana tajna, kontinuitet Data Protection kljuca, certificate/signing-key rollover i identity-provider metadata rollover;
4. nedostupna ili spora baza, pool exhaustion, deadlock ili concurrency konflikt, migration lock i restore proba;
5. downstream timeout, throttle, neispravan odgovor, DNS promena, certificate promena, sprecavanje retry storm-a i recovery;
6. broker duplikat, promena redosleda, kasnjenje, disconnect, poison message, dead-letter replay i overlap consumer deployment-a;
7. prevelika, spora, neispravna, kompresovana, arhivirana, path-traversal i neautorizovana file operacija;
8. spor klijent, disconnected klijent, stream cancellation, backpressure, reconnect, revocation i deployment drain;
9. cold start, warm load, burst, soak, overload, degradirana zavisnost, memory pressure, thread-pool pressure i recovery;
10. SIGTERM ili service stop tokom read-a, write-a, upload-a, stream-a, job-a, migracije i telemetry flush-a;
11. rolling ili canary deployment sa old/new koegzistencijom, abort-om, application rollback-om, forward repair-om i data recovery-jem;
12. clean checkout restore/build/test/publish i izvrsavanje tacnog finalnog artefakta u nameravanom hosting modelu.

