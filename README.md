# Ultimate Production Audit Prompt Library

Bilingual English/Serbian library of evidence-first master prompts for deep technical audits, safe remediation, production readiness, incident response and recovery.

**Library version:** 2.0.0  
**Baseline date:** 2026-08-05  
**Active packages:** 16  
**Active prompt files:** 32  
**Languages:** English and Serbian

## What This Library Is

Each prompt is a structured operating contract for an AI coding or audit agent. The prompts are designed to prevent shallow checklist reviews and require evidence across source code, dependencies, generated artifacts, runtime configuration, data, deployment, security controls, failure modes, rollback and recovery.

The library is not a guarantee that a system is secure or production-ready. Results depend on scope, access, evidence quality, tool capability, environment fidelity and correct execution.

## Packages

| # | Package | English | Serbian |
| --- | --- | --- | --- |
| 1 | AI / RAG / LLM / Agents / Tools / MCP | `ai-rag-llm-agent-audit-prompt.en.md` | `ai-rag-llm-agent-audit-prompt.sr.md` |
| 2 | Android / Kotlin / Jetpack Compose / TV | `android-master-audit-prompt.en.md` | `android-master-audit-prompt.sr.md` |
| 3 | DevOps / Docker / Kubernetes / Cloud | `devops-docker-kubernetes-audit-prompt.en.md` | `devops-docker-kubernetes-audit-prompt.sr.md` |
| 4 | .NET / C# / ASP.NET Core / EF Core | `dotnet-aspnet-core-audit-prompt.en.md` | `dotnet-aspnet-core-audit-prompt.sr.md` |
| 5 | Electron / Tauri Desktop | `electron-tauri-desktop-audit-prompt.en.md` | `electron-tauri-desktop-audit-prompt.sr.md` |
| 6 | Flutter / Dart / Mobile / Web / Desktop | `flutter-dart-mobile-audit-prompt.en.md` | `flutter-dart-mobile-audit-prompt.sr.md` |
| 7 | Go / Rust Backend And Systems | `go-rust-backend-audit-prompt.en.md` | `go-rust-backend-audit-prompt.sr.md` |
| 8 | Java / Spring Boot / JVM | `java-spring-boot-audit-prompt.en.md` | `java-spring-boot-audit-prompt.sr.md` |
| 9 | Next.js / React / TypeScript | `nextjs-master-audit-prompt.en.md` | `nextjs-master-audit-prompt.sr.md` |
| 10 | Node.js / Express / Fastify API | `node-express-api-audit-prompt.en.md` | `node-express-api-audit-prompt.sr.md` |
| 11 | PHP / Laravel / Symfony | `php-laravel-symfony-audit-prompt.en.md` | `php-laravel-symfony-audit-prompt.sr.md` |
| 12 | Python / PySide6 / Qt Desktop | `python-pyside6-desktop-audit-prompt.en.md` | `python-pyside6-desktop-audit-prompt.sr.md` |
| 13 | React Native / Expo / Android / iOS | `react-native-expo-mobile-audit-prompt.en.md` | `react-native-expo-mobile-audit-prompt.sr.md` |
| 14 | Ruby / Ruby on Rails | `ruby-rails-audit-prompt.en.md` | `ruby-rails-audit-prompt.sr.md` |
| 15 | SQL / PostgreSQL / MySQL / MariaDB / SQLite | `sql-database-audit-prompt.en.md` | `sql-database-audit-prompt.sr.md` |
| 16 | WordPress Security Recovery / Forensics / Hardening | `wordpress-security-recovery-hardening-prompt.en.md` | `wordpress-security-recovery-hardening-prompt.sr.md` |

## Recommended Use

1. Select the closest stack prompt.
2. Provide the repository, artifacts, runtime/deployment context and business-critical flows.
3. Include the shared files from `core/` when the target model supports multiple files.
4. Select `AUDIT_ONLY`, safe-fix, incident-response or equivalent mode defined by the prompt.
5. Require the agent to distinguish facts, observations, hypotheses and unknowns.
6. Do not approve destructive changes without evidence, impact and rollback.
7. Re-run the prescribed verification and failure scenarios after changes.
8. Keep the final report and evidence IDs with the release or incident record.

## Shared Contracts

- `core/audit-operating-contract.md` - evidence-first operating rules
- `core/severity-model.md` - common P0-P3 severity model
- `core/final-report-schema.md` - final report structure
- `core/production-readiness-dod.md` - shared production readiness Definition of Done

## Baselines

The `baselines/` directory contains dated source manifests. They are snapshots, not permanent truth. Every time-sensitive version, security, support-policy or platform claim must be re-checked against its primary source during a real audit.

Never invent a future patch number. Never upgrade solely because a newer major exists. Verify compatibility, support, migration, rollout and rollback.

## Validation

Run:

```bash
python scripts/check_parity.py
python scripts/check_integrity.py
python scripts/check_baselines.py
```

The checks validate active EN/SR pair discovery, heading depth, line-shape parity, YAML frontmatter, version metadata, JSON source manifests, balanced fenced blocks, banned baseline hardcodes and Serbian dash-style rules.

Structural parity does not prove perfect semantic translation. Human or model-assisted bilingual review is still required for meaning-sensitive changes.

## Repository Layout

```text
.
├── *.en.md / *.sr.md        active prompt pairs
├── core/                    shared operating contracts
├── baselines/               dated primary-source manifests
├── reviews/                 Serbian revision reports
├── scripts/                 repository validation tools
├── stacks/                  reusable stack overlays
└── archive/                 superseded prompt versions
```

## Safety Notes

- Use only on systems you are authorized to inspect or change.
- Preserve evidence before destructive incident-response actions.
- Do not expose secrets, personal data, private keys or full database dumps in prompts or reports.
- A green build, passing checksum, successful deployment or absence of visible symptoms is not proof of production safety.
- Missing evidence must remain missing evidence, not be converted into a passing result.

## License And Contributions

See `LICENSE`, `CONTRIBUTING.md` and `SECURITY.md`.
