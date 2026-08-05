## Faza 4 - Build, bootstrap, konfiguracija, tajne i generisano stanje

### Cilj

Dokaži efektivnu konfiguraciju i generisano stanje koje koristi svaki artefakt i proces.

### Zahtevi audita

- Mapiraj environment promenljive, `.env` fajlove, secret manager-e, Symfony secrets, Laravel encrypted environment fajlove, mounted fajlove i platform-provided konfiguraciju.
- Utvrdi precedence i vreme učitavanja konfiguracije u CLI, HTTP, worker, scheduler, test, build, cache warmup i deployment hook-ovima.
- Audituj Laravel config, route, event i view cache i Symfony container compilation, cache warmup, env processor-e i dumped konfiguraciju.
- Proveri da su generisani proxy-ji, hydrator-i, serializer-i, API klijenti, ORM metadata, optimized autoload, frontend asset-i i code generation reproducibilni.
- Proveri izlaganje tajni u source-u, istoriji, logovima, stack trace-ovima, cache fajlovima, build layer-ima, Composer auth-u, CI artefaktima, debug alatima i backup-ima.
- Definiši rotaciju, opoziv, dual-key overlap, kontinuitet APP_KEY ili encryption ključa i oporavak za šifrovane podatke, cookie-je, sesije i signed URL-ove.

### Obavezni dokazi

- Mapa efektivne konfiguracije sa izvorom, precedence-om, vremenom učitavanja, vlasnikom, osetljivošću i reload ponašanjem.
- Fingerprint-i konfiguracije artefakta i runtime-a bez vrednosti tajni.
- Test rotacije i oporavka ključeva i tajni za svaku kritičnu kriptografsku zavisnost.

### Kriterijumi prihvatanja

- Konfiguracija je deterministična, environment-specific, bez tajni u artefaktima i vidljiva po reviziji.
- Rotacija ključa ili rollback ne čine tiho korisničke ili poslovne podatke nepovratnim.

