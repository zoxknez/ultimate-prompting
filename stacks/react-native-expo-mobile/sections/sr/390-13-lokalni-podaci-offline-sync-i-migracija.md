## 13. Lokalni podaci, offline, sync i migracija

### 13.1 Inventar storage-a i schema
- Popisi AsyncStorage, MMKV, SQLite, Realm, WatermelonDB, filesystem, SecureStore, Keychain, Keystore, native SDK storage i cache.
- Za svaki store zabelezi schema verziju, vlasnika, transaction model, thread model, enkripciju, backup, corruption recovery, kvotu i ponasanje brisanja.
- Koristi atomic write ili database transakciju za durable state i dokazi crash ponasanje na svakoj commit granici.
- Testiraj stare podatke sa novim binary-jem, stare podatke sa OTA update-om, delimicno migrirane podatke, prekinutu migraciju, malo prostora i read-only stanje.
- Nikada ne dozvoli da OTA update zahteva ireverzibilnu lokalnu schema promenu osim ako su dokazani runtime kompatibilnost, fallback i forward repair.
- Definisi backup, restore, export, brisanje, reinstall, promenu naloga i device-transfer semantiku.

### 13.2 Offline queue i resavanje konflikta
- Modeluj svaku queued komandu sa stabilnim ID-jem, actor-om, tenant-om, resursom, precondition-om, verzijom payload-a, idempotency key-em, brojem pokusaja i terminalnim stanjem.
- Definisi ordering, dependency, cancellation, replacement, compaction, expiration, prioritet i korisniku vidljivo pending stanje.
- Resavaj konflikte eksplicitnim domenskim pravilima umesto generickim last-write-wins pristupom osim kada poslovanje prihvata gubitak podataka.
- Testiraj duplu isporuku, promenjen redosled isporuke, delimican batch uspeh, stale precondition, odbijanje servera, istek tokena, upgrade aplikacije i promenu naloga.
- Obezbedi reconciliation i manuelni oporavak kada ni klijent ni server ne mogu bezbedno da utvrde konacno stanje.
- Meri starost queue-a, dubinu, retry, konflikt, dead letter, byte i vreme do konvergencije.

