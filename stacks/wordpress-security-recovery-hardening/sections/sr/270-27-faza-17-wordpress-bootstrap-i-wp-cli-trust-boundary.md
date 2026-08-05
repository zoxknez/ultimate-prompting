## 27. Faza 17 - WordPress Bootstrap I WP-CLI Trust Boundary

WordPress bootstrap tretiraj kao potencijalno neprijateljski dok se ne pregledaju core, konfiguracija, MU pluginovi, drop-in fajlovi i kod koji se rano učitava.

### Mapa bootstrap izvršavanja

Prati i proveri:

- web-server rewrite i front-controller putanju
- `index.php`, `wp-blog-header.php`, `wp-load.php`, `wp-config.php` i `wp-settings.php`
- fajlove uključene pre ili iz `wp-config.php`
- `auto_prepend_file` i `auto_append_file` iz PHP, pool, vhost i per-directory konfiguracije
- `advanced-cache.php`, `object-cache.php`, `db.php`, `sunrise.php`, `maintenance.php` i druge drop-in fajlove
- MU pluginove i njihove loader fajlove
- Composer autoloader-e, custom bootstrap fajlove i vendor kod
- environment loader-e tajni i bootstrap kod hosting provajdera
- OPcache i preload konfiguraciju koja može da zadrži stari izvršivi kod

### WP-CLI bezbednosna pravila

- utvrdi da li komanda radi pre učitavanja WordPress-a ili izvršava pun kompromitovani bootstrap
- `wp core verify-checksums` je koristan jer dokumentovana komanda radi pre učitavanja WordPress-a, ali i dalje dokazuje samo integritet core fajlova
- ne pretpostavljaj da `--skip-plugins --skip-themes` neutrališe MU pluginove, drop-in fajlove, `wp-config.php`, PHP auto-prepend kod ili host-level persistence
- za komande koje učitavaju WordPress prednost daj kopiji dokaza ili izolovanom forenzičkom klonu
- koristi najmanje privilegovan OS i database nalog koji je dostupan
- nikada ne pokreći WP-CLI kao root samo da bi zaobišao permissions
- zabeleži komandu, radni direktorijum, efektivnog korisnika, WP-CLI verziju, exit code i hash output-a
- neočekivan output, mrežni poziv, kreiranje procesa ili izmenu fajla tokom read-only komande tretiraj kao indikator za istragu

### Direktna inspekcija kao fallback

Kada se WordPress bootstrap-u ne može verovati:

- pregledaj fajlove direktno OS alatima
- koristi read-only database pristup i eksplicitne SQL upite
- izvuci inventar iz package manifest-a, metadata fajl sistema i čistih vendor paketa
- uporedi sa izolovanom poznato dobrom WordPress instalacijom
- odloži application-level komande dok se bootstrap trust boundary ne obnovi

