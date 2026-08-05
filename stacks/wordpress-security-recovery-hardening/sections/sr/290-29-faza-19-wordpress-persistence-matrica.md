## 29. Faza 19 - WordPress Persistence Matrica

Koristi persistence matricu i svaki red označi kao `EXAMINED`, `NOT PRESENT`, `CONFIRMED`, `UNVERIFIED` ili `OUT OF SCOPE`.

### Persistence u fajl sistemu i bootstrap-u

- izmenjeni root/core fajlovi
- MU pluginovi i skriveni loader fajlovi
- drop-in i cache loader-i
- fajlovi aktivnih i neaktivnih pluginova/tema
- izvršivi upload-i i polyglot media
- `.htaccess`, Nginx/LiteSpeed pravila i custom error dokumenti
- `.user.ini`, `php.ini`, PHP-FPM pool direktive i auto-prepend fajlovi
- backup, cache, language, upgrade i privremeni direktorijumi
- parent direktorijumi, susedni sajtovi i startup fajlovi korisničkog home-a
- OPcache preload fajlovi i zastareli bytecode

### WordPress i database persistence

- administrator, editor i service nalozi
- izmene uloga/capability-ja u user metadata
- application password-i i session tokeni
- `active_plugins`, network-active pluginovi i podešavanja tema
- cron option unosi i plugin-specific tabele zakazanih akcija
- zlonamerni options, transients, widgets, meniji, block sadržaj i reusable patterns
- injektovani postovi, stranice, revizije, komentari i metadata
- site URL, home URL, upload putanja, admin email i redirect podešavanja
- database trigger-i, events, routine, neočekivani korisnici i grant-ovi
- object-cache vrednosti sposobne da vrate zastarelo ili zlonamerno application stanje

### Host i eksterni persistence

- user/system cron, systemd timer-i i startup hook-ovi
- SSH ključevi, shell profili i authorized-command ograničenja
- korisnici kontrolnog panela, tokeni i one-click installer poslovi
- DNS zapisi, nameserver-i, registrar delegate-i i domain forwarding
- CDN worker-i, pravila, redirect-i, origin override-i i cache ključevi
- Git deploy ključevi, CI tajne, webhook-ovi i build artefakti
- email forwarding, mailbox pravila, SMTP kredencijali i API tokeni
- Search Console/Bing ownership tokeni i neovlašćeni verifikovani vlasnici

Ne proglašavaj persistence iskorenjenim dok svaki primenljivi red nema dokaz i metod verifikacije.

