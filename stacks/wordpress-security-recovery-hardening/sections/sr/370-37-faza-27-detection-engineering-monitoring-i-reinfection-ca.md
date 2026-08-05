## 37. Faza 27 - Detection Engineering, Monitoring I Reinfection Canary

Monitoring mora biti projektovan prema zapaženoj attack putanji i preostaloj neizvesnosti.

### Minimalna detection pokrivenost

- privileged login, reset lozinke, izmene uloga i capability-ja
- novi application password-i, API ključevi i session-i
- instalacija, update, aktivacija, deaktivacija i file edit core-a, pluginova i tema
- izmene MU pluginova, drop-in fajlova, `wp-config.php`, `.htaccess`, `.user.ini` i executable upload-a
- izmene cron-a, Action Scheduler-a, system cron-a i panel zadataka
- izmene DNS-a, nameserver-a, CDN worker-a/rule-a i certificate-a
- neobični outbound HTTP, mail volume i webhook destinacije
- skokovi 404, 403, 5xx, login, XML-RPC, REST i admin-ajax saobraćaja
- sumnjive PHP greške, kreiranje procesa i upisi u fajl sistem
- database admin, trigger, event, grant i schema izmene
- novi Search Console/Bing vlasnici i sitemap submission-i
- drift checkout skripti, DOM-a i mrežnih zahteva kada postoji commerce

### Canary i integrity kontrole

- uspostavi potpisan ili hash-ovan poznato dobar inventar kritičnih izvršivih fajlova
- koristi canary fajlove ili direktorijume samo kada ne izlažu tajne niti stvaraju šum
- alarmiraj na kreiranje PHP-a u uploads/cache/language/backup putanjama
- prati neočekivane izmene update konfiguracije i security kontrola
- baseline-uj normalne outbound domene i privileged akcije
- potvrdi da alert-i stižu na kanal nezavisan od kompromitovanog okruženja
- testiraj alert-e bezbednim sintetičkim događajima i zabeleži latenciju dostave

### Kriterijumi izlaska iz monitoringa

Ne zatvaraj pojačan monitoring samo na osnovu proteklog vremena. Zahtevaj:

- da nema ponavljanja indikatora incidenta
- stabilan inventar fajlova i konfiguracije
- samo očekivanu privileged aktivnost
- čisto stanje scheduled task-ova i queue-a
- čistu search/index i checkout verifikaciju kada su primenljivi
- funkcionalne alert-e i sačuvane logove
- prihvatanje preostalih blind spot-ova od strane vlasnika

