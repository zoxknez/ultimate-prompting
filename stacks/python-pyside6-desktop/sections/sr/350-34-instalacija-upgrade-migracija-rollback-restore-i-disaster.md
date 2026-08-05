## 34. Instalacija, upgrade, migracija, rollback, restore i disaster recovery

### 34.1 Obim audita

1. Inventariši sve podržane početne verzije, kanale, arhitekture, installation scope-ove, data schema-e, konfiguracione verzije, plugin-e, helper-e i OS stanja.
2. Definiši fresh install, first run, upgrade, repair, side-by-side install, promenu kanala, migraciju arhitekture, downgrade, uninstall, reinstall i prenos profila.
3. Mapiraj svaku migraciju podataka i konfiguracije sa precondition-om, transakcijom ili atomicity-jem, backup-om, compatibility prozorom, failure stanjem, retry-jem, forward repair-om i rollback limitima.
4. Razlikuj application rollback, configuration rollback, feature rollback, updater rollback, helper rollback, data rollback i server-side kompatibilnost.
5. Dokumentuj pokrivenost backup-a, enkripciju, off-device kopije, retention, detekciju korupcije, restore tooling, operator proceduru, RPO i RTO.
6. Definiši ponašanje kada se preklapaju stari i novi binary-ji, helper-i, plugin-i, schema-e, update metadata i serverski API-ji.

### 34.2 Obavezna verifikacija

1. Izvrši podržanu upgrade matricu sa reprezentativnim podacima, plugin-ima, nalozima, podešavanjima, prekinutim operacijama i low-resource uslovima.
2. Injektuj kvar pre, tokom i posle zamene paketa, migracije, update-a helper-a, restart-a servisa, promene metadata i first launch-a.
3. Dokaži da rollback tiho ne korumpira novije podatke i da su forward repair ili data reconciliation dostupni kada je reverse migracija nebezbedna.
4. Izvrši izolovan restore iz stvarnih backup-a na čistim mašinama i izmeri postignuti RPO i RTO, uključujući keyring i certificate zavisnosti.
5. Dokumentuj tačan manual recovery za boot failure, crash loop, pokvaren updater, korumpiran profil, revoked sertifikat, izgubljen signing ključ i nedostupan backend.

