## 21. Background izvršavanje i zakazivanje

Background rad kontroliše platforma i ne može ga garantovati Dart timer.

- Popiši WorkManager, foreground service-e, background fetch, BGTaskScheduler, silent push, isolate-e, desktop service-e, scheduled task-ove i browser background mogućnosti.
- Dokumentuj platformsku podobnost, prozor izvršavanja, kvote, battery/network ograničenja, user-visible zahteve, dozvole i ponašanje pri terminaciji.
- Učini task-ove idempotentnim, resumable, bounded, observable i bezbednim posle duplog zakazivanja, odloženog izvršenja, process death-a, reboot-a, upgrade-a, logout-a ili promene naloga.
- Proveri inicijalizaciju background entrypoint-a, registraciju plugin-a, pristup storage-u, auth refresh, tenant kontekst i conflict handling.
- Spreči background job-ove da cure podatke posle logout-a, nastave opozvane upload-e, ožive obrisano stanje ili pošalju zastarele notifikacije.
- Testiraj restricted battery režime, bez mreže, metered mrežu, malo storage-a, reboot, force stop, OS upgrade, app upgrade i oporavak propuštenog rasporeda.
- Meri uspeh, kašnjenje, retry-je, duplo izvršenje, trajanje, potrošnju resursa, starost queue-a i backend load.
- Obezbedi degraded-mode ponašanje proizvoda kada platforma ne može ili neće da izvrši rad po željenom rasporedu.

