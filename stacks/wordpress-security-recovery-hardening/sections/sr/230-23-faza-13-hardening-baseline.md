## 23. Faza 13 - Hardening Baseline

Primeni prema okruženju i poslovnim zahtevima. Izbegavaj cargo-cult podešavanja.

### WordPress

- ažuriraj core, pluginove i teme na održavane kompatibilne verzije
- ukloni nekorišćene pluginove/teme i nepoznat kod
- ograniči broj administratora i koristi imenovane naloge
- uključi MFA za privilegovane naloge
- isključi dashboard file editing preko `DISALLOW_FILE_EDIT`
- razmotri `DISALLOW_FILE_MODS` samo kada se deployment i update upravljaju eksterno
- ograniči application passwords i ukloni nekorišćene kredencijale
- ograniči registraciju i dodelu uloga
- pregledaj REST/XML-RPC izloženost prema legitimnoj upotrebi
- zaštiti WP-Cron ili ga zameni kontrolisanim system scheduler-om kada je prikladno
- smanji broj pluginova i zahtevaj poreklo/odgovorno lice za održavanje
- uključi security/audit logging sa zaštićenim remote retention-om gde je moguće

### Fajl sistem i PHP

- least-privilege ownership i permissions
- bez world-writable izvršivih putanja
- zabrani izvršavanje skripti u uploads i cache direktorijumima kada arhitektura dozvoljava
- zaštiti `wp-config.php`, backup, log i environment fajlove
- potvrdi da temporary i session direktorijumi nisu web-accessible
- isključi izlaganje PHP verzije
- isključi prikaz PHP grešaka u production-u i uključi bezbedno logovanje
- pregledaj dangerous functions prema potrebama aplikacije, ne kao zamenu za patching
- koristi `open_basedir` samo kada pruža stvarnu izolaciju i kompatibilnost je testirana
- postavi bezbedna upload ograničenja i MIME obradu
- koristi podržanu PHP verziju i ekstenzije

### Web server i transport

- forsiraj HTTPS i uključi HSTS tek kada je HTTPS ispravan na svim potrebnim poddomenima
- postavi odgovarajuće security header-e uz compatibility test
- zabrani pristup hidden/config/backup fajlovima
- isključi directory listing
- ograniči admin putanje preko rate limiting-a, WAF-a, VPN-a ili IP pravila gde je praktično
- pravilno podesi real client IP iza CDN/proxy-ja
- bezbedno podesi request/body limite i timeout-e

### Database

- jedinstven least-privilege WordPress database korisnik
- bez javnog remote database pristupa osim kada je izričito potreban i ograničen
- podržana database verzija
- bezbedni backup-i i encrypted transport gde je primenljivo
- monitoring privilegovanih korisnika, grants, triggers i events

### Host i operacije

- podržan OS i paketi
- SSH ključevi, MFA/provider kontrole i bez deljenih admin naloga
- odvojeni site/account-i gde je moguće radi ograničenja lateral movement-a
- patch management sa staging-om i rollback-om
- offsite, immutable ili versioned backup-i
- dokumentovani restore testovi
- centralizovani logovi i alerting
- file-integrity monitoring sa poznatim baseline-om
- inventar ranjivosti i odgovornost za održavanje
- incident runbook i kontakt lista

### CDN, DNS i third-party servisi

- MFA i least privilege
- registrar lock i provera recovery podataka
- upozorenja za DNS izmene
- origin lock-down i autentifikovani origin gde je podržan
- pregled workers, page rules, redirect-a i transform pravila
- ograniči payment/API/webhook kredencijale
- popiši third-party skripte i tag-manager privilegije

