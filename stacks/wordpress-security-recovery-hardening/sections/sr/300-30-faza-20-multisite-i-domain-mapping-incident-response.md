## 30. Faza 20 - Multisite I Domain-Mapping Incident Response

Za WordPress Multisite obuhvati mrežu, a ne samo vidljivo pogođen sajt.

### Multisite inventar

- tip mreže: poddomen, poddirektorijum ili mapirani domeni
- glavni sajt, svi sajtovi, archived/spam/deleted sajtovi i orphaned tabele
- super administratore i network-level service naloge
- network-active pluginove, MU pluginove i network-enabled teme
- `sunrise.php`, domain-mapping kod i povezane tabele/options
- network podešavanja, registration politiku i dozvoljene email domene
- upload putanje i per-site granice medija
- globalne korisnike i per-site capability metadata
- `wp_blogs`, `wp_site`, `wp_sitemeta`, registration i sign-up zapise kada su primenljivi
- per-site options, postove, metadata i cron unose
- network cache, CDN i certificate pokrivenost

### Multisite-specifične provere

- potvrdi da kompromitacija jednog sajta ne može izvršavati kod kroz deljene pluginove/teme na celoj mreži
- pregledaj dodelu super-admin prava i capability izmene
- razdvoji site-specific od network-wide injektovanog sadržaja
- proveri vlasništvo mapiranih domena, redirect-e i TLS
- testiraj direktan pristup kroz originalne i mapirane hostname-ove
- pregledaj obrisane ili arhivirane sajtove radi persistence-a
- proceni da li deljene tabele ili globalni korisnici izlažu druge tenant-e
- rebuild ili restore izvrši network-aware redosledom i sa mapom table prefix-a

Čist glavni sajt ne dokazuje da je mreža čista.

