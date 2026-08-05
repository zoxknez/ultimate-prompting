## 28. Backup, restore, disaster recovery i business continuity

**Cilj:** Dokazi da se kriticni servis i podaci mogu oporaviti unutar prihvacenih ciljeva.

### 28.1 Obavezne provere

1. Popisi podatke, konfiguraciju, state, tajne, kljuceve, sertifikate, registre, IaC state, GitOps repozitorijume, cluster state, spoljne zavisnosti i redosled oporavka.
2. Definisi poslovno odobren RPO, RTO, maksimalno tolerisano vreme prekida, granularnost oporavka, prihvatljiv gubitak podataka, pretpostavke zavisnosti i komunikacione obaveze.
3. Proveri backup opseg, konzistentnost, application quiescence, koordinaciju transakcija, ucestalost, retention, immutability, encryption, pristup, replikaciju, zastitu od brisanja, monitoring i trosak.
4. Proveri da su backup-system i recovery kredencijali odvojeni od primarnih putanja kompromitovanja i dostupni tokom identity, KMS, DNS, region ili control-plane otkaza.
5. Izvrsi izolovani restore reprezentativnih kriticnih podataka i platform state-a, potvrdi integritet, aplikacionu kompatibilnost, pristup, redosled, reconciliation i korisnicki tok.
6. Testiraj point-in-time recovery, obrisan objekat, ostecen backup, nedostajuci kljuc, partial backup, nedostupan region i kompromitovan primary scenario gde je primenljivo.
7. Izvedi failover i failback sa DNS-om, sertifikatima, data replikacijom, redovima, cache-evima, identitetom, tajnama, observability-jem, third-party sistemima i operativnim osobljem.
8. Izmeri stvarni RPO, RTO, ispravnost podataka, rucne korake, uska grla, trosak i rezidualne single point of failure tacke.

### 28.2 Minimalni dokazi

- Poslovno odobreni recovery ciljevi i redosled zavisnosti.
- Dokaz pokrivenosti backup-a, immutability-ja, pristupa, monitoringa i restore-a.
- Vremenski izmereni rezultati failover-a, failback-a, integriteta i korisnickog toka.

### 28.3 Kriterijumi izlaza

1. Oporavak kriticnih podataka i servisa je demonstriran unutar prihvacenog RPO i RTO ili je praznina blokirajuci nalaz.
2. Recovery ne zavisi od istog kompromitovanog ili otkazalog control plane-a bez alternative.
3. Runbook-ovi, kredencijali, ljudi, zavisnosti i artefakti potrebni za recovery su dostupni i testirani.

