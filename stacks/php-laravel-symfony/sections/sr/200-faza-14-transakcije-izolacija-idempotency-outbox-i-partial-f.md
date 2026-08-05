## Faza 14 - Transakcije, izolacija, idempotency, outbox i partial failure

### Cilj

Dokaži atomicity, replay safety, consistency i recovery kroz granice baze i spoljnih side effect-a.

### Zahtevi audita

- Mapiraj svaku kritičnu mutation operaciju na transaction manager, konekciju, isolation level, timeout, retry policy, lock redosled i commit granicu.
- Proveri framework transaction helper-e, nested transakcije, savepoint-e, više konekcija, callback timing, exception conversion i rollback semantiku.
- Testiraj lost update, write skew, phantom, uniqueness race, duplicate request, deadlock, timeout, process crash i client disconnect.
- Dizajniraj idempotency sa autentikovanim scope-om, request fingerprint-om, atomskim ownership-om, in-progress stanjem, durable rezultatom, expiry-jem, retry-jem i conflict ponašanjem.
- Koristi transactional outbox, inbox, CDC ili ekvivalentan dokazani dizajn kada database stanje i poruke ili spoljni efekti moraju da se slažu.
- Definiši reconciliation i compensating akcije za payment-e, email, object storage, search indexing, webhook-ove i druge netransakcione efekte.

### Obavezni dokazi

- Matrica transakcija i side effect-a kritičnih tokova sa identifikovanom svakom crash tačkom.
- Dokaz konkurentnih i replay testova oko pre-commit, commit i post-commit granica.
- Dokaz outbox-a, inbox-a, reconciliation-a i manuelnog recovery-ja za partial failure.

### Kriterijumi prihvatanja

- Retry, duplicate delivery, timeout ili process crash ne može tiho da duplira ili izgubi kritični poslovni efekat.
- Svaki ne-atomski cross-system tok ima detektabilno odstupanje i testiranu recovery proceduru.

