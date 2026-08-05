## 54. Obavezni adversarial i failure scenariji

1. Promeni identifikator resursa, route parametar, tenant, nalog, notification payload ili deep-link cilj i proveri serversku i lokalnu izolaciju.
2. Tapni mutaciju više puta pod sporom mrežom i proveri jedan logički side effect, istinito UI stanje, idempotentnost i telemetriju.
3. Promeni rutu, nalog, tenant, locale ili filter dok su zahtevi i stream-ovi aktivni i proveri da zastareo rad ne može mutirati novo stanje.
4. Ubij proces tokom startup-a, migracije baze, upisa, upload-a, plaćanja, sinhronizacije i update-a; proveri oporavak i očuvanje invarijanti.
5. Isporuči duple, odložene, promenjenog redosleda, malformirane, istekle, wrong-account i revoked-session push ili realtime događaje.
6. Odbij, ograniči, limitiraj, opozovi ili promeni svaku materijalnu dozvolu dok su funkcija i aplikacija aktivne.
7. Radi offline duži period, promeni sat/vremensku zonu, queue-uj konfliktne operacije sa više uređaja, zatim se poveži i uskladi.
8. Vrati 401, 403, 409, 412, 429, 5xx, malformirane, prekinute, ogromne, spore, redirectovane i timed-out mrežne odgovore tokom kritičnih tokova.
9. Prosledi zlonamerne URL-ove, fajlove, arhive, medije, JavaScript poruke, platform-channel payload-e, FFI ulaze, putanje i filename-ove.
10. Testiraj minimalne, tipične, najnovije, low-memory, low-storage, battery-restricted, accessibility, multi-window i architecture varijante.
11. Instaliraj svaku podržanu staru verziju, kreiraj realne podatke, uradi upgrade preko preskočenih verzija, prekini upgrade, vrati stari backup i pokušaj downgrade.
12. Serviraj stari web shell sa novim asset-ima i novi shell sa starim asset-ima; testiraj zastarele service worker-e, mešane CDN cache-eve i rollback.
13. Koristi old client/new server i new client/old server kombinacije sa preklapanjem šeme, feature flag-a, notifikacija i background job-a.
14. Simuliraj nedostajući plugin, native biblioteku, simbol, hardver, entitlement, sistemski servis, keychain/keyring, browser capability i distributivni servis.
15. Pusti da isteknu ili opozovi signing, push, TLS, identity, store, update i telemetry kredencijale; proveri alert-e, containment, rotaciju i kontinuitet.
16. Izazovi crash loop, rast memorije, retry storm, reconnect storm, notification storm, velike queue-eve, velike liste i backend overload.
17. Vrati sistem iz backup-a ili trusted artefakata u izolovanom okruženju i dokaži identitet, konzistentnost podataka, autorizaciju, observability i izmereni RPO/RTO.
18. Ponovo build-uj posle simulirane kompromitovane zavisnosti ili build runner-a i dokaži čist provenance, nove potpise gde su potrebni, poređenje artefakata i opoziv.

