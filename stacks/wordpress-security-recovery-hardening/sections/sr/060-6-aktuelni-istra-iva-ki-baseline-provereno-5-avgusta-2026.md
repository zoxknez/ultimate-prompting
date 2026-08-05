## 6. Aktuelni Istraživački Baseline - Provereno 5. Avgusta 2026.

Tretiraj ovo kao datirani snapshot, a ne kao trajnu istinu. Pre saveta vezanih za verzije ponovo proveri zvanične izvore.

| Komponenta | Provereni baseline | Obavezno tumačenje |
| --- | --- | --- |
| WordPress | Najnovija stabilna verzija: 7.0.2, objavljena 17. jula 2026. | Pre remediation-a ponovo proveri release arhivu. Koristi najnovije održavano bezbednosno izdanje kompatibilno sa sajtom. |
| Budući WordPress | Verzija 7.1 planirana je za 19. avgust 2026. | Nikada ne preporučuj budući ili pre-release build za production recovery, osim ako je izričito tražen za testiranje. |
| PHP preporuka | WordPress preporučuje PHP 8.3 ili noviji | Prednost daj trenutno podržanoj PHP grani kompatibilnoj sa svim obaveznim pluginovima/temama i potvrđenoj u staging-u. |
| PHP minimum | WordPress 7.0 podržava najmanje PHP 7.4 | PHP 7.4 je EOL i nije prihvatljiv dugoročni production cilj. Tretiraj ga kao P1 tehnički dug ili više kada je javno izložen. |
| PHP upstream podrška | Na datum provere podržane su PHP 8.2, 8.3, 8.4 i 8.5 grane, sa različitim rokovima podrške | Ponovo proveri php.net. Prednost daj granama sa aktivnom podrškom kada kompatibilnost to dozvoljava. |
| Database preporuka | MySQL 8.0+ ili MariaDB 10.11+ | Pre migracije potvrdi kompatibilnost hosta i pluginova. Legacy podrška nije isto što i bezbedan baseline. |
| Web transport | HTTPS podrška je obavezna/preporučena | Potvrdi end-to-end HTTPS, validaciju origin-a i secure cookies, a ne samo HTTPS ispred CDN-a. |
| Incident response | NIST SP 800-61 Rev. 3 final, april 2025. | Uključi pripremu, detekciju, odgovor, oporavak i lessons learned u upravljanje rizikom. |
| Checksum | WP-CLI može proveriti WordPress core i checksum pluginova iz zvaničnog repozitorijuma | Uspešan checksum je samo jedan signal i ne pokriva database, uploads, MU pluginove, custom/premium kod, host ili edge persistence. |

Obavezni zvanični izvori za ponovnu proveru:

- https://wordpress.org/download/releases/
- https://wordpress.org/about/requirements/
- https://developer.wordpress.org/advanced-administration/security/hardening/
- https://developer.wordpress.org/cli/commands/core/verify-checksums/
- https://developer.wordpress.org/cli/commands/plugin/verify-checksums/
- https://www.php.net/supported-versions.php
- https://csrc.nist.gov/pubs/sp/800/61/r3/final

Za svaku eksternu tvrdnju u finalnom izveštaju zabeleži URL izvora, naslov stranice, datum pristupa i činjenicu koju izvor podržava.

