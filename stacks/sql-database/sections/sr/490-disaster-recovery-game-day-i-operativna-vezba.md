## Disaster-recovery game day i operativna vezba

Recovery procedure moraju biti izvrsive od strane on-call tima pod vremenskim pritiskom i sa delimicnim informacijama.

- Izaberi realne scenarije kao sto su gubitak regiona, slucajno brisanje, korumpirana migracija, kompromitovani kredencijali ili povratak stale primary-ja.
- Koristi izolovano okruzenje i odobreno rukovanje podacima uz ocuvanje production-like topologije.
- Izmeri vreme detekcije, odluke, pristupa, restore-a, validacije, cutover-a, reconciliation-a i komunikacije.
- Zabelezi svaku nedostajucu dozvolu, nedokumentovanu zavisnost, zastarelu komandu i nejasan ownership.
- Azuriraj runbook-ove, automatizaciju, monitoring, kontakte i obuku na osnovu dokaza.
- Ponavljaj dok izmereni RPO i RTO ne zadovolje deklarisane ciljeve.

