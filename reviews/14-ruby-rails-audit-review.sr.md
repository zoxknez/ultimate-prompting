# Revizija 14 - Ruby / Ruby on Rails production audit prompt

Datum: 2026-08-05

## Polazno stanje

- Stari EN prompt: 253 linija i 31 naslova.
- Stari SR prompt: 253 linija i 31 naslova.
- Pocetni paritet je prolazio, ali je prompt bio prekratak za dokaziv source-to-runtime production audit.

## Rezultat

- Novi EN prompt: 863 linija i 96 naslova.
- Novi SR prompt: 863 linija i 96 naslova.
- Oba jezika generisana su iz jedne sinhronizovane strukture.
- Uvedeni su E0-E5 nivoi dokaza, P0-P3 severity, 12 evidence matrica i 20 adversarial/failure scenarija.

## Najvaznija unapredjenja

- Potpun lanac od commit-a, Ruby runtime-a i Bundler grafa do image/artifact digest-a, procesa, schema-e, telemetry-ja i recovery-ja.
- Odvojeni CRuby, JRuby i TruffleRuby audit.
- Dubinski Rack, middleware, auth, session, CSRF, tenant i admin audit.
- Active Record constraint, transaction, concurrency, idempotency, multi-database, shard i migration audit.
- Odvojeni Active Job, Solid Queue, Sidekiq i scheduler ugovori.
- Puma i drugi serveri, GVL/thread/fiber/Ractor, GC/YJIT, memory i capacity dokaz.
- Action Cable, Hotwire, Active Storage, parser, webhook i external integration hardening.
- Immutable artifact promotion, mixed-version rollout, rollback, forward repair, isolated restore i trusted rebuild.

## Validacije

- Heading paritet: prosao.
- Line-shape paritet: prosao.
- YAML frontmatter: validan.
- JSON baseline: validan.
- Markdown code fence blokovi: balansirani.
- En dash, em dash i non-breaking hyphen u SR promptu: 0.
