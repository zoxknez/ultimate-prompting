## 13. Faza 3 - Inventar Okruženja

Napravi kompletnu mapu asset-a pre donošenja zaključaka.

### WordPress inventar

- WordPress verzija, locale i update kanal
- single-site ili multisite
- aktivni i neaktivni pluginovi sa verzijama i poreklom
- aktivne i neaktivne teme sa verzijama i poreklom
- MU pluginovi
- drop-in fajlovi: `advanced-cache.php`, `db.php`, `db-error.php`, `install.php`, `maintenance.php`, `object-cache.php`, `sunrise.php`
- custom kod, code snippets, child teme i vendor paketi
- administratori, editori i privilegovani servisni nalozi
- application passwords
- WP-Cron događaji i rasporedi
- REST rute, XML-RPC upotreba i javno izloženi endpoint-i
- aktivni pluginovi sačuvani u database options
- uploads struktura i prisustvo izvršivih fajlova
- object cache, page cache i CDN integracija
- security, backup i migration pluginovi
- payment, SMTP, analytics, tag manager i SSO integracije

### Host inventar

- OS, kernel, hosting nalog i model izolacije
- web server i virtual-host konfiguracija
- PHP verzija, SAPI, pool konfiguracija i ekstenzije
- document root putanje, aliases, symlink-ovi i dodatni domeni/poddomeni
- filesystem ownership, permissions, ACL i immutable flags
- SSH korisnici, ključevi, dostupnost shell history-ja i SFTP/FTP nalozi
- cPanel/Plesk korisnici, API tokeni i delegirani korisnici
- user i system crontab, `/etc/cron*`, systemd timeri i startup skripte
- `/tmp`, `/var/tmp`, home direktorijumi i susedni web root-ovi
- lokacije logova, rotacija i retention
- backup, snapshot i restore tačke
- outbound mail konfiguracija
- Redis/Memcached/object-cache servisi
- container-i, deployment pipeline-i i mounted volume-i gde postoje

### Edge i eksterni inventar

- registrar nalog i nameserver-i
- DNS zapisi i nedavne izmene
- CDN/WAF zone, workers, pravila, redirect-i i origin podešavanja
- TLS sertifikati i origin sertifikati
- Search Console/Bing Webmaster Tools
- payment provider webhook-ovi i API kredencijali
- Git repozitorijumi, CI/CD sistemi i deployment ključevi
- transactional email provajder
- monitoring i uptime servisi

