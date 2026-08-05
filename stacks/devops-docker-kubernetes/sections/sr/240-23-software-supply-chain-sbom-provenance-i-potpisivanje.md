## 23. Software supply chain, SBOM, provenance i potpisivanje

**Cilj:** Dokazi poreklo komponenti i blokiraj neovlascene ili ranjive artefakte prema riziku.

### 23.1 Obavezne provere

1. Popisi package manager-e, lockfile-ove, module, base image-e, action-e, plugin-e, chart-ove, operator-e, binarne fajlove, firmware, vendored kod i download skripte.
2. Proveri autenticnost izvora, immutable reference, checksum-e, potpise, maintainer-e, licence, podrsku, release kanale, mirror-e i otpornost na dependency confusion.
3. Generisi potpune SBOM-ove za izvor i finalne artefakte, ukljuci tranzitivne i OS zavisnosti, identifikuj alat i format i potvrdi pokrivenost prema build-ovanom artefaktu.
4. Generisi provenance koji identifikuje izvor, builder, parametre, zavisnosti, okruzenje, izlaze i izolaciju. Proceni primenljive SLSA zahteve bez preuvelicavanja nivoa.
5. Potpisi artefakte i atestacije zasticenim kljucevima ili keyless identitetom, pa proveri issuer, subject, audience, identitet sertifikata, transparency dokaz, vezu sa digest-om i policy.
6. Koreliraj ranjivosti sa reachability-jem, execution context-om, izlozenoscu, eksploatabilnoscu, compensating kontrolama, dostupnoscu popravke i deployment inventarom umesto samo sa severity oznakom skenera.
7. Definisi vremenski ogranicene procedure izuzetka, karantina, opoziva, ponovnog potpisivanja, rebuild-a i hitne zamene.
8. Testiraj admission ili promotion odbijanje nepotpisanih, pogresno potpisanih, neproverljivih, ranjivih, zastarelih, pogresnog izvora ili pogresnog okruzenja artefakata.

### 23.2 Minimalni dokazi

- Inventar provenance-a zavisnosti i komponenti.
- SBOM, provenance, potpis i verification izvestaji vezani za artefakt.
- Vezba policy odbijanja i reakcije na kompromitovanu komponentu.

### 23.3 Kriterijumi izlaza

1. Kriticni produkcioni artefakti mogu se pripisati odobrenom izvoru i zasticenim builder-ima.
2. SBOM, provenance, potpis i vulnerability odluke su vezani za tacan deploy-ovani digest.
3. Putanje opoziva i rebuild-a mogu ukloniti kompromitovanu komponentu iz produkcije unutar prihvacenog roka.

