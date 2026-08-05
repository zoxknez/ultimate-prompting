## 25. Pakovanje, bundling, installer-i, potpisivanje, update i rollback

### 25.1 Obim audita

1. Identifikuj packaging alate, verzije, spec/config fajlove, hook-ove, hidden import-e, exclusion-e, data fajlove, Qt module, collection plugin-a, native biblioteke i runtime opcije.
2. Uporedi one-file, one-folder, app bundle, portable, installer, store, system-package i enterprise deployment ponašanje gde je primenljivo.
3. Pregledaj poverenje bootloader-a/runtime-a, extraction direktorijume, privremeno izvršavanje, DLL/library pretragu, integritet resursa, antivirus interakciju i writable code putanje.
4. Mapiraj code-signing identitete, sertifikate, timestamp servise, notarizaciju, entitlement-e, potpisivanje paketa, custody ključeva, odobrenje, rotaciju, revocation i recovery gubitka.
5. Dokumentuj update metadata, transport, verifikaciju potpisa, kanal, cohort, mapiranje arhitekture/platforme, redosled verzija, downgrade politiku, delta/full pakete, vreme instalacije i restart.
6. Definiši fresh install, upgrade, repair, prekinutu instalaciju, prekinut update, rollback, forward repair, uninstall, retention podataka i side-by-side channel ponašanje.

### 25.2 Obavezna verifikacija

1. Izgradi iz čistog okruženja, pregledaj package manifest-e i binary-je i uporedi isporučene fajlove sa allowlisted bill of materials.
2. Instaliraj na čistim mašinama kao standardni korisnik i administrator; verifikuj first run, dozvole, shortcut-e, association-e, servise, prerequisite-e i uninstall.
3. Verifikuj potpise i notarizaciju nakon finalnog pakovanja; dokaži da se post-sign mutacija ili tampered update sadržaj odbacuje.
4. Testiraj update sa svake podržane verzije/kanala/arhitekture, offline prekid, pun disk, process lock, antivirus kašnjenje, gubitak napajanja, signature kvar i server rollback.
5. Dokaži recovery kada update počne ali ne može da se završi, data schema napreduje, stari binary se ponovo pokrene, signing ključevi budu opozvani ili update servis bude kompromitovan.

