# Upgrade Progress

Baseline start: 2026-08-05

| # | Paket | EN | SR | Paritet | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | AI / RAG / LLM / Agents / Tools / MCP | done | done | passed | completed |
| 2 | Android / Kotlin / Jetpack Compose | done | done | passed | completed |
| 3 | DevOps / Docker / Kubernetes | done | done | passed | completed |
| 4 | .NET / ASP.NET Core / EF Core | done | done | passed | completed |
| 5 | Electron / Tauri Desktop | done | done | passed | completed |
| 6 | Flutter / Dart Mobile / Web / Desktop | done | done | passed | completed |
| 7 | Go / Rust Backend | done | done | passed | completed |
| 8 | Java / Spring Boot | done | done | passed | completed |
| 9 | Next.js / React / TypeScript | done | done | passed | completed |
| 10 | Node.js / Express / Fastify API | done | done | passed | completed |
| 11 | PHP / Laravel / Symfony | done | done | passed | completed |
| 12 | Python / PySide6 / Qt Desktop | done | done | passed | completed |
| 13 | React Native / Expo | done | done | passed | completed |
| 14 | Ruby / Rails | done | done | passed | completed |
| 15 | SQL / PostgreSQL / MySQL / MariaDB / SQLite | done | done | passed | completed |
| 16 | WordPress Security Recovery / Hardening | done | done | passed | completed |

## Current Repository-Level Findings

- Structural EN/SR parity is automatically tested for all 16 current prompt pairs.
- Semantic translation equivalence still requires human or model-assisted review.
- Full fixture-based eval repositories remain future repository-level work.

## Korak 4 - Zavrseno

- .NET / C# / ASP.NET Core / EF Core EN/SR paket unapredjen na verziju 2.0.0.
- Revizija: `reviews/04-dotnet-aspnet-core-audit-review.sr.md`.

## Korak 5 - Zavrseno

- Electron / Tauri / Chromium / WebView / Node.js / Rust desktop EN/SR paket unapredjen na verziju 2.0.0.
- Revizija: `reviews/05-electron-tauri-desktop-audit-review.sr.md`.

## Korak 6 - Zavrseno

- Flutter / Dart / Android / iOS / Web / Windows / macOS / Linux EN/SR paket unapredjen na verziju 2.0.0.
- Revizija: `reviews/06-flutter-dart-audit-review.sr.md`.

## Korak 7 - Zavrseno

- Go / Rust backend / systems EN/SR paket unapredjen na verziju 2.0.0.
- Revizija: `reviews/07-go-rust-backend-audit-review.sr.md`.

## Korak 8 - Zavrseno

- Java / Spring Boot / JVM EN/SR paket unapredjen na verziju 2.0.0.
- Uklonjen je prethodni heading i line-shape raskorak izmedju jezika.
- Revizija: `reviews/08-java-spring-boot-audit-review.sr.md`.


## Korak 9 - Zavrseno

- Next.js / React / TypeScript / Node.js / Vercel / self-hosting EN/SR paket unapredjen na verziju 2.0.0.
- Uveden source-to-runtime evidence model, RSC i Server Actions hardening, Cache Components privacy matrica, platform/version-skew audit i recovery ugovor.
- TypeScript baseline ispravljen prema stabilnom izdanju 7.0 od 8. jula 2026.
- Revizija: `reviews/09-nextjs-react-typescript-audit-review.sr.md`.

## Korak 10 - Zavrseno

- Node.js / Express / Fastify / TypeScript API EN/SR paket unapredjen na verziju 2.0.0.
- Uveden source-to-runtime evidence model, odvojeni Express i Fastify audit, HTTP/proxy hardening, auth i tenant matrice, transaction/idempotency/reconciliation ugovor, event-loop i memory dokaz, immutable promotion, rollback, restore i incident kontrole.
- Revizija: `reviews/10-node-express-fastify-api-audit-review.sr.md`.

## Korak 11 - Zavrseno

- PHP / Laravel / Symfony / Composer / FPM / long-lived runtime EN/SR paket unapredjen na verziju 2.0.0.
- Uveden source-to-runtime evidence model, odvojeni Laravel i Symfony lifecycle audit, auth i tenant matrice, Eloquent/Doctrine data integrity, transaction/idempotency/outbox ugovor, queue i long-lived worker recovery, FPM/OPcache capacity, immutable promotion, migracije, rollback, restore i incident trusted rebuild.
- Revizija: `reviews/11-php-laravel-symfony-audit-review.sr.md`.
## Korak 12 - Zavrseno

- Python / PySide6 / Qt Widgets / QML / WebEngine desktop EN/SR paket unapredjen na verziju 2.0.0.
- Uklonjen je poslednji postojeci EN/SR heading i line-shape raskorak u biblioteci.
- Uveden source-to-installed-runtime evidence model, Python ABI i GIL/free-threaded/JIT audit, QObject i signal/thread lifecycle, QtAsyncio, model/view, QML, WebEngine, native/IPC granice, platformsko pakovanje, signing, update, rollback, restore i incident trusted rebuild.
- Revizija: `reviews/12-python-pyside6-qt-desktop-audit-review.sr.md`.


## Korak 13 - Zavrseno

- React Native / Expo / Android / iOS EN/SR paket unapredjen na verziju 2.0.0.
- 879 linija i 130 naslova po jeziku, bez strukturnih odstupanja.
- Revizija: `reviews/13-react-native-expo-audit-review.sr.md`.


## Korak 14 - Zavrseno

- Ruby / Ruby on Rails / Active Record / Active Job / Puma EN/SR paket unapredjen na verziju 2.0.0.
- Uveden source-to-runtime evidence model, odvojeni CRuby/JRuby/TruffleRuby audit, auth i tenant matrice, transaction/idempotency/migration ugovor, Solid Queue i Sidekiq delivery dokaz, Puma/concurrency/GC/YJIT capacity, realtime/storage hardening, immutable promotion, rollback, restore i incident trusted rebuild.
- Revizija: `reviews/14-ruby-rails-audit-review.sr.md`.

## Korak 15 - Zavrseno

- SQL / PostgreSQL / MySQL / MariaDB / SQLite / managed database EN/SR paket unapredjen na verziju 2.0.0.
- Ispravljen je baseline: MySQL 8.4 je LTS, dok je MySQL 9.7 Innovation linija, a ne LTS.
- Uveden source-to-data evidence model, schema i invariant audit, transaction/isolation/locking/idempotency ugovor, query-plan i capacity dokaz, engine-specific putanje, migration/backfill, backup/PITR/HA/DR, 12 evidence matrica i 20 adversarial scenarija.
- 803 linije i 74 naslova po jeziku, bez strukturnih odstupanja.
- Revizija: `reviews/15-sql-database-audit-review.sr.md`.



## Korak 16 - Zavrseno

- WordPress Security Incident Response / Forensics / Trusted Recovery / Hardening EN/SR paket unapredjen na verziju 2.0.0.
- Uvedeni incident command, account-wide/shared-hosting scope, bootstrap i WP-CLI trust boundary, supply-chain provenance, persistence matrice, Multisite, WooCommerce/payment skimmer, SEO recovery, cache/CDN/OPcache, Action Scheduler, dubinski database i serialized-data audit, trusted rebuild, detection engineering, 12 evidence matrica i 20 failure scenarija.
- 1.608 linija i 143 naslova po jeziku, bez strukturnih odstupanja.
- Revizija: `reviews/16-wordpress-security-recovery-hardening-review.sr.md`.

## Biblioteka - Zavrseno

- Svih 16 EN/SR paketa je unapredjeno.
- Svih 16 aktivnih parova prolazi structural parity proveru.
- Ukupno: 32 aktivna prompt fajla i 31.606 linije.
