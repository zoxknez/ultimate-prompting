## Faza 10 - Symfony application putanja

### Cilj

Audituj efektivno Symfony ponašanje od kernel boot-a kroz HTTP, console, Messenger, Scheduler, Doctrine, cache i deployment.

### Zahtevi audita

- Proveri tačan Symfony patch, PHP opseg, Flex recipes, bundle-ove, Runtime komponentu, izbor okruženja, kernel konfiguraciju i kompajlirani container.
- Audituj učitavanje ruta, argument value resolver-e, request mapping, validator-e, serializer-e, voter-e, access control, firewall-e, authenticator-e i exception listener-e.
- Pregledaj service visibility, autowiring, autoconfiguration, alias-e, decorator-e, compiler pass-ove, lazy service-e, resettable service-e i optimizaciju container-a.
- Audituj Doctrine ORM i DBAL integraciju, entity listener-e, subscriber-e, filtere, repository-je, transaction middleware, migracije i generisanje proxy-ja.
- Proveri Messenger transport-e, stamp-ove, middleware, retry, failure transport-e, deduplikaciju, worker limite, reset ponašanje i graceful shutdown.
- Audituj Scheduler, Lock, Cache, RateLimiter, Workflow, EventDispatcher, HttpClient, Mailer, Notifier, secrets vault i izlaganje debug komponenti.
- Proveri cache warmup, environment-specific kompilaciju container-a, asset handling, zamenu worker-a i zero-downtime release ponašanje.

### Obavezni dokazi

- Dokaz efektivnog container-a, ruta, firewall-a, service-a, transporta, cache-a i okruženja iz produkcionog artifact-a.
- Negativni authorization, serializer, validator, Messenger replay i service reset testovi.
- Dokaz cache warmup-a i zamene worker-a povezan sa jednim immutable release-om.

### Kriterijumi prihvatanja

- Ponašanje kompajliranog container-a odgovara pregledanoj source konfiguraciji i ne izlaže debug-only service-e ili rute.
- Dugovečni Symfony worker-i resetuju request-scoped stanje i obrađuju retry bez kršenja poslovnih invarijanti.

