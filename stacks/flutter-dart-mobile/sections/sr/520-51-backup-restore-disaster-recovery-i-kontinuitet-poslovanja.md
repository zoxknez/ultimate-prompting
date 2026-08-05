## 51. Backup, restore, disaster recovery i kontinuitet poslovanja

Tvrdnja o backup-u je nepotpuna dok restore i kompatibilnost aplikacije nisu demonstrirani.

- Popiši serverske backup-e, lokalne export-e, user-created backup-e, cloud backup ponašanje, secure-storage backup ponašanje, backup signing materijala, retention artefakata, simbole, source map-e i oporavak store pristupa.
- Definiši vlasnika, scope, učestalost, enkripciju, immutable stanje, retention, pristup, region, pravna ograničenja, redosled zavisnosti, RPO, RTO i restore okruženje.
- Testiraj restore sa tačnim verzijama aplikacije, verzijama šeme, encryption ključevima, kredencijalima, backend ugovorima, feature konfiguracijom i simbolima potrebnim za rad i dijagnostiku.
- Proveri da obnovljeni klijenti i servisi ne dupliraju queued operacije, ne koriste opozvane kredencijale, ne oživljavaju obrisane podatke, ne prelaze tenant granice ili krše retention.
- Uključi scenarije gubitka signing ključa, store naloga, push sertifikata, kompromitacije update feed-a, gubitka backend regiona, telemetry outage-a i prekida kritičnog vendor-a.
- Testiraj failover i failback gde je primenljivo, uključujući DNS, sertifikat, origin, app-link association, remote config, cache i ponašanje starog klijenta.
- Zabeleži izmereni RPO/RTO, nedostajuće zavisnosti, ručne korake, gubitak podataka, uticaj na korisnike i remedijaciju iz svake probe.
- Ne proglašavaj recovery-ready stanje samo na osnovu uspešnih backup job-ova, zadržanih artefakata ili dokumentovanih procedura.

