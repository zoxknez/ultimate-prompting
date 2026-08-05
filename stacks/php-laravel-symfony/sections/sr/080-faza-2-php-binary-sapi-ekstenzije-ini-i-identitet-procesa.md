## Faza 2 - PHP binary, SAPI, ekstenzije, INI i identitet procesa

### Cilj

Dokaži koji PHP build i konfiguraciju svaki proces zaista koristi.

### Zahtevi audita

- Zabeleži tačnu PHP verziju, datum build-a, arhitekturu, thread-safety režim, compiler, debug flagove, Zend Engine i relevantne build opcije.
- Uporedi CLI, FPM, Apache module, queue worker, scheduler, migration job, test runner i container runtime binary-je.
- Uporedi učitane INI fajlove, scan direktorijume, setove ekstenzija, timezone, locale, memory, execution, upload, session, OPcache, JIT, realpath i error podešavanja.
- Popiši PDO drivere, Redis ili Memcached klijente, intl, mbstring, sodium, OpenSSL, curl, XML, image, zip, pcntl, posix, sockets i FFI zavisnosti.
- Proveri OS pakete, CA trust, ICU, timezone bazu, graphics biblioteke i native client biblioteke koje koriste ekstenzije.
- Potvrdi runtime identitet iz deployment procesa ili bezbednog diagnostic endpoint-a, ne samo iz lokalnog `php -v`.

### Obavezni dokazi

- Matrica PHP identiteta po procesu sa binary putanjom, SAPI-jem, verzijom, patch-em, ekstenzijama, INI-jem, image digest-om i vlasnikom.
- Diff CLI, web, worker, scheduler, migration i test runtime podešavanja.
- Odluka o podršci i upgrade-u povezana sa zvaničnim lifecycle-om i podrškom provajdera.

### Kriterijumi prihvatanja

- Svi kritični procesi koriste eksplicitno podržan i patch-ovan runtime ili imaju ograničen migration plan.
- Nijedna odluka se ne oslanja na nedokazanu pretpostavku da svi PHP SAPI-ji dele isti binary ili konfiguraciju.

