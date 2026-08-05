## 21. Faza 11 - Strategija Eradication-a

Izaberi i obrazloži jednu strategiju:

### Strategija A - Čist rebuild, preporučena kod potvrđene kompromitacije

- pripremi čisto okruženje ili čist document root
- instaliraj svež WordPress core iz zvaničnog izvora
- instaliraj known-good pluginove/teme iz proverenih izvora
- migriraj samo provereni content i obaveznu konfiguraciju
- ponovo kreiraj pouzdane administratore
- regeneriši salts i tajne
- validiraj pre prebacivanja saobraćaja

### Strategija B - Restore proverenog backup-a

Koristi samo kada:

- backup prethodi najranijoj verovatnoj kompromitaciji
- poreklo i integritet backup-a su poznati
- backup je skeniran i upoređen pre restore-a
- initial-access vektor je zatvoren pre javnog izlaganja
- posle restore-a kredencijali se rotiraju

### Strategija C - In-place remediation

Koristi samo kada rebuild/restore nije izvodljiv i dokumentuj povećani preostali rizik. Kompromitovane komponente zameni pouzdanim paketima umesto da njihovo ručno krpljenje bude finalno stanje.

### Obavezni eradication koraci

- stavi dokaz u karantin, ne preimenuj ga samo unutar javnog direktorijuma
- ukloni neovlašćene korisnike, ključeve, cron zadatke, triggers, workers i pravila
- ukloni persistence iz WordPress-a, hosta, database-a i edge-a
- zakrpi ili ukloni initial-access vektor
- posle čuvanja dokaza i zamene koda očisti OPcache, object cache, page cache i CDN cache
- potvrdi da nema kompromitovanih susednih sajtova koji mogu ponovo inficirati cilj

