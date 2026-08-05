## 31. Lokalni storage, baze, migracije i cache

Lokalna persistencija je verzionisan data sistem, ne implementacioni detalj.

- Popiši SQLite/Drift/sqflite, Isar, Hive, ObjectBox, Realm, SharedPreferences, secure storage, fajlove, browser storage, desktop preference-e, cache i index-e.
- Klasifikuj autoritativne podatke, replicirane podatke, cache, izvedene podatke, secret materijal, draft stanje, queue stanje, telemetry stanje i disposable podatke.
- Proveri verzionisanje šeme, forward migraciju, rollback politiku, prekinutu migraciju, malo diska, korupciju, staru verziju aplikacije, vraćen backup i ponašanje parcijalnog upisa.
- Koristi transakcije za višekoračne invarijante; pregledaj isolation, konkurentne reader/writer-e, nested transakcije, WAL/journal ponašanje i pristup sa native thread-a.
- Particioniši podatke po nalogu i tenant-u; proveri logout, promenu naloga, promenu tenant-a, brisanje, backup, restore i cache invalidation.
- Audituj tvrdnje o enkripciji, lifecycle ključa, pretražive metapodatke, privremene fajlove, backup-e, screenshot-e, browser DevTools izloženost i desktop filesystem dozvole.
- Definiši cache key, freshness, stale-while-revalidate, invalidation, veličinu, eviction, korupciju, stampede zaštitu i offline semantiku.
- Zahtevaj migration fixture-e iz svake podržane istorijske verzije i testiraj upgrade, prekinut upgrade, oporavak, odbijanje downgrade-a i export podataka.

