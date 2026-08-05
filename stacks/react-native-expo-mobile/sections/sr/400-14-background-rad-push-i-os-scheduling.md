## 14. Background rad, push i OS scheduling

### 14.1 Background izvrsavanje
- Popisi TaskManager task, background fetch, lokaciju, geofencing, upload, download, media, headless JavaScript, native servis, BGTaskScheduler i Android job.
- Proveri vreme registracije, jedinstven identitet task-a, duplu registraciju, versioning, persistirane opcije, zavisnost od dozvola i unregister ponasanje.
- Dizajniraj za best-effort scheduling, OS throttling, ogranicenja baterije, mrezne uslove, gasenje procesa, reboot i vendor-specific ponasanje.
- Ogranici vreme izvrsavanja, memoriju, obim podataka, retry, wakeup i konkurentnost; checkpoint-uj durable napredak.
- Testiraj stari background kod sa novim backend-om, novi JavaScript sa starim native scheduler stanjem i queued rad kroz upgrade aplikacije.
- Izlozi uspeh, gresku, timeout, cancellation, sledeci raspored, poslednji zavrsetak i korisniku vidljivo stale-data stanje.

### 14.2 Push notification i akcije
- Popisi APNs, FCM, Expo Push Service, direktnu provider integraciju, notification service extension, kategorije, kanale i background handler-e.
- Tretiraj payload kao nepoverljiv input i validiraj tip, verziju, velicinu, sender context, deep link, resource ownership i expiration.
- Ne stavljaj tajne ili nepotrebne licne podatke u payload, notification tekst, analytics ili device log.
- Testiraj duple, odlozene, promenjenog redosleda, istekle, malformed, tenant-mismatched, logged-out, account-switched i revoked-resource notification-e.
- Posebno proveri tap, dismiss, quick action, text input, foreground, background, terminated i restored ponasanje.
- Definisi registraciju tokena, rotaciju, invalidaciju, logout cleanup, brisanje naloga, razdvajanje okruzenja i delivery observability.

