# Revizija 16 - WordPress Security Recovery / Malware Cleanup / Hardening

Datum verifikacije: 2026-08-05

## Početno stanje

Postojeći WordPress paket je bio najdublji od originalnih promptova: 1.004 linije i 83 naslova po jeziku. Imao je dobro incident-response jezgro, evidence-first pristup, čuvanje dokaza, containment, filesystem/database analizu, credential rotation, clean rebuild, hardening, release gate-ove i kontrolisan finalni izveštaj.

Ipak, za maksimalni production incident-response nivo nedostajali su formalizovani slojevi za:

- incident command i decision authority
- shared-hosting i neighbor-site lateralno kretanje
- WordPress bootstrap i WP-CLI trust boundary
- supply-chain provenance pluginova, tema i eksternih integracija
- potpuna persistence matrica
- Multisite i domain mapping
- WooCommerce, checkout i payment skimmer incidente
- SEO spam i Search Console recovery
- Redis/page cache/CDN/OPcache stale-state rizike
- WP-Cron, Action Scheduler i background queue persistence
- serialized database podatke i content reconciliation
- formalni backup trust score i clean-rebuild tok
- detection engineering i reinfection canary kontrole
- obavezne evidence matrice i adversarial scenarije

## Rezultat rekonstrukcije

- prompt verzija: 2.0.0
- EN linije: 1.608
- SR linije: 1.608
- EN naslovi: 143
- SR naslovi: 143
- EN/SR heading odstupanja: 0
- EN/SR line-shape odstupanja: 0
- YAML frontmatter: validan
- Markdown fence blokovi: balansirani
- nedozvoljene vrste crte u SR promptu: 0
- dedicated baseline manifest: validan JSON

Originalni v1.0.0 par je sačuvan pod:

`archive/wordpress-security-recovery-hardening/v1.0.0/`

## Najvažnija tehnička unapređenja

### 1. Source-to-runtime i bootstrap poverenje

Prompt sada eksplicitno proverava:

- rewrite i front-controller putanju
- `index.php`, `wp-blog-header.php`, `wp-load.php`, `wp-config.php` i `wp-settings.php`
- PHP `auto_prepend_file` i `auto_append_file`
- MU pluginove i sve WordPress drop-in fajlove
- Composer autoloadere i custom bootstrap kod
- OPcache/preload i stare PHP-FPM procese
- hosting-provider bootstrap i environment loader-e

WP-CLI se više ne tretira kao automatski bezbedan samo zato što je CLI alat. Prompt razlikuje dokumentovane komande koje rade pre učitavanja WordPress-a od komandi koje mogu izvršiti kompromitovani bootstrap.

### 2. Account-wide incident scope

Uveden je audit svih domena, staging instalacija, sibling sajtova, shared upload/cache/tmp direktorijuma, panel korisnika, FTP/SFTP/SSH naloga, crona, database korisnika, Redis/Memcached instance i control-plane događaja.

Kod kredibilne account-wide kompromitacije preferira se novi hosting nalog ili novo okruženje, umesto parcijalnog čišćenja jednog document root-a.

### 3. Supply-chain provenance

Svaki plugin, theme, MU plugin, drop-in i code-snippet paket sada mora imati:

- poznat izvor
- verziju i putanju
- commit/tag ili package URL
- hash/potpis kada postoji
- maintenance owner-a
- support status
- vulnerability/abandonment procenu
- capability i impact inventar

Posebno se obrađuju premium/custom paketi, uklonjeni pluginovi, ownership transfer, nulled distribucije, update serveri, Composer/npm zavisnosti i remote third-party skripte.

### 4. Persistence matrica

Persistence je proširena na tri kompletna sloja:

- filesystem/bootstrap
- WordPress/database
- host/external control plane

Uključeni su application passwords, session tokeni, roles/capabilities, cron, Action Scheduler, options/transients, database triggers/events, object cache, SSH, panel tokeni, DNS/CDN, CI, mailbox pravila i Search Console vlasništvo.

### 5. Multisite

Dodat je network-aware audit za:

- super administratore
- network-active pluginove
- globalne i per-site tabele
- `sunrise.php` i domain mapping
- mapped domains i TLS
- deleted/archived sajtove
- cross-site capability i cache granice
- network-aware restore i table-prefix mapu

### 6. WooCommerce i payment skimmer

Novi prompt zahteva:

- checkout suspension decision
- browser DOM i network evidence
- payment architecture mapu
- provider/acquirer eskalaciju
- gateway, webhook i fraud logove
- WooCommerce REST ključeve, Store API i custom template-e
- Action Scheduler i failed jobs
- third-party checkout JavaScript i tag manager
- conditional skimmer testove
- provider-coordinated credential rotation

### 7. SEO spam i search recovery

Audit sada obuhvata:

- server/CDN/WordPress redirect-e
- sitemap, robots, feed, canonical i structured data
- hidden/doorway sadržaj
- cloaking po user agent-u, referrer-u, IP-u, geografiji i auth statusu
- service worker-e i browser cache
- Search Console/Bing vlasnike i istoriju promena
- ispravan redosled remediation -> cache purge -> sitemap regeneration -> review/removal

### 8. Cache, OPcache i stale release

Uvedena je kontrolisana sekvenca za:

- WordPress object cache
- page cache
- Redis/Memcached
- reverse proxy
- CDN i edge workers
- host cache
- OPcache/preload
- PHP-FPM child procese
- browser cache i service worker-e

Prompt zabranjuje purge pre deploy-a pouzdanog koda kada bi se cache ponovo napunio kompromitovanim sadržajem.

### 9. WP-Cron i Action Scheduler

Dodati su:

- kompletan scheduler inventar
- owner/callback mapiranje
- encoded argument i recurrence analiza
- evidence preservation pre otkazivanja
- old worker i duplicate execution kontrola
- business idempotency
- restore/timezone/DST scenariji
- reinfection detection kroz ponovno kreiranje event-a

### 10. Database i serialized data

Prompt sada zahteva:

- stvarni table prefix i schema discovery
- user/session/application-password analizu
- options/site options/transients/autoload/cron audit
- posts/revisions/templates/patterns/navigation audit
- plugin-specific, WooCommerce i Multisite tabele
- triggers/events/routines/definer proveru
- serialization-aware mutacije
- before/after hash i row evidence
- poslovni reconciliation posle restore-a

### 11. Backup i trusted rebuild

Svaki backup dobija provenance, integrity, isolation scan, restore test, timeline poziciju i data-gap procenu.

Clean rebuild sada uključuje novo trusted okruženje, fresh official WordPress, verified komponente, controlled data migration, upload sanitization, nove tajne, security/functional/recovery testove i cutover sa rollback planom.

### 12. Detection engineering

Dodati su alert zahtevi za:

- privileged identity promene
- core/plugin/theme i critical-file izmene
- executable upload
- cron/Action Scheduler/panel task
- DNS/CDN/certificate promene
- outbound HTTP/mail/webhook anomalije
- PHP proces/file-write ponašanje
- database grants/triggers/schema
- Search Console ownership
- checkout DOM/network drift

## Obavezni dokazi

Dodato je 12 matrica:

1. asset i control-plane
2. source-to-runtime integrity
3. persistence
4. identity i secret
5. database integrity
6. scheduled execution
7. edge i cache
8. backup i restore
9. vulnerability i patch
10. critical functional flow
11. notification i stakeholder
12. production return

Dodato je i 20 adversarial/failure scenarija, uključujući cloaking, direct-origin bypass, executable uploads, application-password revocation, cron recurrence, stale OPcache, sibling-site rewrite, isolated restore, update interruption, checkout script integrity, duplicate job delivery i credential revocation recovery.

## Aktuelni baseline

Verifikovani primary-source baseline nalazi se u:

`baselines/wordpress-security-baseline-2026-08-05.json`

Ključne potvrđene činjenice:

- WordPress 7.0.2 je aktuelni release od 17. jula 2026.
- Release rešava critical i high security problem, uz forced auto-update za pogođene sajtove.
- WordPress preporučuje PHP 8.3+, MariaDB 10.11+ ili MySQL 8.0+ i HTTPS.
- PHP 8.2 i 8.3 su u security-only podršci; PHP 8.4 i 8.5 su u aktivnoj podršci.
- `wp core verify-checksums` radi pre WordPress bootstrap-a, ali proverava samo core fajlove.
- plugin checksum pokriva samo pakete za koje WordPress.org checksum postoji.
- NIST SP 800-61 Rev. 3 je aktuelni finalni incident-response okvir.

## Konačna ocena

WordPress paket je sada najdublji incident-response prompt u biblioteci i pokriva tehnički, operativni, forenzički, identity, data, supply-chain, commerce, search, recovery i monitoring životni ciklus.
