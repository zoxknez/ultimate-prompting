# Changelog

## [2.0.0] - 2026-08-05

### Added

- Completed all 16 synchronized English/Serbian production audit packages.
- Added repository-wide integrity validation, prompt catalog, SHA-256 manifest, final validation report and final Serbian library review.
- Added the WordPress 2.0 incident-response, trusted-recovery and hardening package.

### Changed

- All active prompt pairs now declare version 2.0.0.
- All active pairs now pass equal line count, line-shape and heading-depth validation.
- Baseline claims are tied to dated primary-source manifests and mandatory re-verification.

### Known limitations

- Structural parity does not prove perfect semantic translation.
- Fixture-based end-to-end eval repositories remain future work.

## [0.9.0] - 2026-08-04

### Fixed

- Baseline wording: no invented Node/Docker/Kubernetes/Helm/MySQL patch numbers; force re-check of official sources.
- Android SR typo: `SIDELLOAD` → `SIDELOAD`.
- Added MIT `LICENSE` (README claimed MIT without a license file).

### Added

- `core/` shared operating contract modules.
- `baselines/sources.json` source manifest for version claims.
- `scripts/check_parity.py` EN/SR structural parity checker.
- `scripts/check_baselines.py` banned invented-version patterns.
- `SECURITY.md`, `CONTRIBUTING.md`, this `CHANGELOG.md`.
- Reconstructed depth for **Python/PySide6**, **DevOps**, **WordPress** prompts.
- `stacks/go-audit-overlay.md` and `stacks/rust-audit-overlay.md` (split path for Go/Rust).

### Changed

- README: honest status — strong **v0.9** library, not fully proven “production-grade” without eval harness.

## [0.1.0] - 2026-08-04

- Initial public package: 16 stacks × EN/SR master audit prompts.

## 2026-08-05 - DevOps production audit prompt 2.0.0

- Rebuilt the English and Serbian DevOps, Docker, Kubernetes and cloud-platform prompt as a synchronized production audit contract.
- Added source-to-production integrity, CI/CD trust boundaries, supply-chain attestations, cluster security, reliability, restore, DR, incident response, and FinOps coverage.
- Added current primary-source baseline entries and a detailed Serbian revision report.
## 2026-08-05 - .NET production audit prompt 2.0.0

- Rebuilt the English and Serbian .NET, C#, ASP.NET Core and EF Core prompt as a synchronized production audit contract.
- Added source-to-runtime identity, MSBuild and NuGet trust, business invariants, authorization matrices, Blazor security, EF provider correctness, outbox, zero-downtime migrations, CLR capacity, artifact promotion, DR, incident response, and migration overlays.
- Added current Microsoft primary-source baseline entries, mandatory evidence matrices, acceptance scenarios, and a detailed Serbian revision report.

## 2026-08-05 - Go / Rust backend and systems production audit prompt 2.0.0

- Rebuilt the English and Serbian Go/Rust prompt as a synchronized source-to-runtime production audit contract.
- Added E0-E5 evidence levels, Go toolchain and build-tag matrices, Rust MSRV/feature/profile matrices, unsafe and ABI contracts, distributed correctness, overload control, mandatory evidence matrices, adversarial scenarios, immutable artifact promotion, rollback, restore, and incident response.
- Added current Go and Rust primary-source baseline entries and a detailed Serbian revision report.
## 2026-08-05 - Node.js / Express / Fastify API production audit prompt 2.0.0

- Rebuilt the English and Serbian Node.js API prompt as a synchronized source-to-runtime production audit contract.
- Added separate Express 4/5 and Fastify 5 lifecycle audits, HTTP/proxy framing controls, runtime validation, authentication and tenant isolation, transaction/idempotency/reconciliation, queue and webhook reliability, event-loop and memory evidence, supply-chain provenance, immutable promotion, rollback, restore, and incident response.
- Added current primary-source baseline entries, 12 evidence matrices, 20 adversarial and failure scenarios, and a detailed Serbian revision report.


## 2026-08-05 - Ruby / Ruby on Rails production audit prompt 2.0.0

- Rebuilt the English and Serbian Ruby/Rails prompt as a synchronized source-to-runtime production audit contract.
- Added separate CRuby, JRuby and TruffleRuby analysis, Rack and HTTP controls, authorization and tenant matrices, Active Record transactions and migrations, Solid Queue and Sidekiq delivery semantics, Puma and concurrency capacity, GC/YJIT evidence, Hotwire/Action Cable/Active Storage hardening, immutable promotion, rollback, restore and incident trusted rebuild.
- Added current official baseline entries, 12 evidence matrices, 20 adversarial and failure scenarios, and a detailed Serbian revision report.

## 2026-08-05 - SQL database production audit prompt 2.0.0

- Rebuilt the English and Serbian SQL, PostgreSQL, MySQL, MariaDB and SQLite prompt as a synchronized source-to-data production audit contract.
- Corrected the release baseline: MySQL 8.4 is LTS, while MySQL 9.7 is the Innovation track rather than LTS.
- Added schema and invariant proof, SQL semantics, transaction/isolation/locking/idempotency analysis, query plans and capacity, engine-specific paths, migrations and backfills, backup/PITR/HA/DR, 12 evidence matrices, 20 failure scenarios and a detailed Serbian review.


## 2026-08-05 - WordPress security incident response prompt 2.0.0

- Rebuilt the English and Serbian WordPress security recovery prompt as a synchronized evidence-first incident-response, trusted-recovery and hardening contract.
- Added incident command, account-wide/shared-hosting scope, WordPress bootstrap and WP-CLI trust boundaries, component provenance, complete persistence matrices, Multisite, WooCommerce/payment-skimmer response, SEO recovery, cache/CDN/OPcache consistency, Action Scheduler, serialized database analysis, trusted backup selection, detection engineering, 12 evidence matrices and 20 adversarial scenarios.
- Added a verified WordPress/PHP/NIST baseline manifest and archived the original v1.0.0 pair.
