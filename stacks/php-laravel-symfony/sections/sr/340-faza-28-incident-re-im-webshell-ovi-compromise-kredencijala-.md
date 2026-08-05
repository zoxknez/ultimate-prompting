## Faza 28 - Incident režim, webshell-ovi, compromise kredencijala, korupcija i trusted rebuild

### Cilj

Obezbedi odvojen workflow koji čuva dokaze za aktivni compromise, gubitak integriteta, destruktivni kvar i nebezbednu neizvesnost.

### Zahtevi audita

- Uđi u INCIDENT režim za aktivni exploit, webshell ili nepoznati executable kod, krađu kredencijala, signing compromise, korupciju podataka, destruktivnu migraciju ili neizvestan produkcioni integritet.
- Sačuvaj logove, process stanje, filesystem metadata, artifact-e, database dokaze, queue stanje, cloud audit zapise, deployment istoriju i timestamped action log.
- Ograniči incident kroz traffic restriction, write freeze, pause worker-a, opoziv kredencijala, invalidaciju sesija, rotaciju ključeva, izolaciju i known-good failover po potrebi.
- Ne čisti nepoverljiv host in-place i ne proglašava ga oporavljenim; identifikuj persistence, initial access, lateral movement, pogođene identitete, data impact i scope.
- Rebuild-uj iz pregledanog source-a, trusted zavisnosti, čistih toolchain-a, sveže infrastrukture, rotiranih tajni, proverenih migracija i potpisanih immutable artifact-a.
- Validiraj podatke, object storage, backup-e, queue-ove, search index-e, cache-eve, sesije, spoljne provider-e i audit trail-ove pre vraćanja normalnog servisa.

### Obavezni dokazi

- Incident timeline, inventar dokaza, chain of custody, containment odluke, scope i zapis opoziva identiteta.
- Known-good source, dependency, toolchain, artifact, infrastructure i restore provenance.
- Post-rebuild dokaz integriteta, autorizacije, recovery-ja, reconciliation-a i monitoringa.

### Kriterijumi prihvatanja

- Servis se ne proglašava oporavljenim dok kod, kredencijali, podaci, hostovi ili artifact provenance ostaju nepoverljivi.
- Recovery uklanja persistence i root cause, vraća known-good stanje i dodaje testirane kontrole protiv ponavljanja.

