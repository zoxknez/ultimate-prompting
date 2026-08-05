## 6. Konfiguracija, Actuator, Supply Chain I Kontrole Zloupotrebe

Validiraj tipiziranu konfiguraciju pri startupu. Kriticna konfiguracija ili tajne moraju bezbedno srusiti startup, ne prvi produkcioni zahtev. Pregledaj property-source prioritet, profile, environment imenovanje, config-server/secrets integraciju, keystore-ove, enkripcijske kljuceve, DataSource URL-ove, `.env` fajlove, istoriju izvora gde je dozvoljeno, CI logove/artefakte, container layere, fixtures i konfiguracione endpointe.

Inventarisi Actuator endpoint access i exposure odvojeno za HTTP i JMX. Koristi restriktivnu allow listu, zastiti osetljive management endpointe, sanitizuj vrednosti i izbegni javni `env`, `configprops`, `beans`, `mappings`, heap dump, thread dump, log fajl, shutdown ili dynamic logger pristup. Javno HTTP izlaganje mora biti eksplicitna odluka sa mreznim i Spring Security kontrolama, ne samo dependency default.

Definisi rate limite po pouzdanom client IP-u, korisniku, API kljucu, tenant-u, ruti, neuspelom pokusaju, operativnoj ceni i broju aktivnih poslova. Validiraj partition key, proxy/IP ponasanje, distribuiranu naspram per-instance semantike, burst algoritam, queue limite, headere, `Retry-After`, fail-open/fail-closed politiku i memorijske granice. Login, reset, skup search/export/upload, AI i kreiranje jobova zahtevaju odvojene kontrole.

Pronadji injection, SpEL/template injection, nebezbednu Java deserijalizaciju, command/file/path injection, open redirect, SSRF, XML entity rizike, log injection, upload abuse, curenje tajni, nebezbedne headere, ranjive zavisnosti, kompromitovane repozitorijume/pluginove i debug curenje. Pinuj i pregledaj build-plugin i dependency izvore; generisi/pregledaj SBOM gde je podrzan.

