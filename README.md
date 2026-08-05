# Ultimate Production Audit Prompt Library

Bilingual English/Serbian library of evidence-first master prompts for deep technical audits, safe remediation, production readiness, incident response and recovery.

**Library content version:** 2.0.0 (every prompt file is byte-identical to the audited v2.0.0 release; see [CHANGELOG.md](CHANGELOG.md))  
**Maintenance architecture:** stack-local-sections composer (see Maintenance Architecture below)  
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

1. Select the closest stack prompt file directly - each `*.en.md` / `*.sr.md` is a complete, self-contained operating contract. No other file needs to be attached.
2. Provide the repository, artifacts, runtime/deployment context and business-critical flows.
3. Select `AUDIT_ONLY`, safe-fix, incident-response or equivalent mode defined by the prompt.
4. Require the agent to distinguish facts, observations, hypotheses and unknowns.
5. Do not approve destructive changes without evidence, impact and rollback.
6. Re-run the prescribed verification and failure scenarios after changes.
7. Keep the final report and evidence IDs with the release or incident record.

## Maintenance Architecture

The 32 root-level prompt files are the release artifact users read. They are also **compiled**: each one is
composed from smaller, version-controlled pieces so the library can be maintained without hand-editing
900-1600 line files, while staying byte-for-byte equivalent to the audited v2.0.0 content.

```text
stacks/<stack-id>/sections/<en|sr>/NNN-*.md   stack-local content, split at the original heading
                                               boundaries with zero rewording (scripts/decompose_master.py)
stacks/<stack-id>/sections.<locale>.json      ordered manifest: which section files (and, where proven
                                               safe, which shared contracts/ modules) compose the prompt
contracts/evidence/*.md                       genuinely shared modules - only introduced once proven
                                               byte-identical in BOTH locales across the stacks that use them
```

Run `python scripts/compose.py --check` to verify every root prompt file still matches what its sections
reconstruct, and `python scripts/check_section_loss.py` to verify zero controls were lost against the frozen
`archive/v2.0.0/SECTION_INVENTORY.json`. A shared module is only extracted from stack-local content when it
carries the same normative meaning, drops no stack-specific exception, holds in both EN and SR, and is
verified regression-free - most stacks were independently authored and genuinely differ (e.g. the
`wordpress-security-recovery-hardening` evidence/severity model is a forensics chain-of-custody scheme, not
the E0-E5 production-audit scale most other stacks use), so most content stays stack-local by design rather
than forced into a one-size-fits-all core.

## Baselines

The `baselines/` directory contains dated source manifests. They are snapshots, not permanent truth. Every time-sensitive version, security, support-policy or platform claim must be re-checked against its primary source during a real audit.

Never invent a future patch number. Never upgrade solely because a newer major exists. Verify compatibility, support, migration, rollout and rollback.

## Validation

Run the full release gate locally (also run in CI on every push/PR, see `.github/workflows/validate.yml`):

```bash
pip install -r requirements.txt
python scripts/validate_release.py --static
```

That single command runs, in order: `check_integrity.py` (EN/SR pair discovery, heading depth, line-shape
parity, YAML frontmatter, version metadata, JSON source manifests, balanced fenced blocks, Serbian
dash-style rules), `check_parity.py` (heading-count/depth parity), `check_baselines.py` (banned invented
patch-version hardcodes), `compose.py --check-lock` and `--check` (composition determinism and byte
equivalence), `check_section_loss.py` (zero controls lost vs. `archive/v2.0.0/`), `check_eval_coverage.py`,
and `run_evals.py` (the mock-provider regression suite). `check_source_links.py` makes live network calls
against third-party sites and runs separately on a daily schedule (`.github/workflows/source-links.yml`),
not on every push.

The regression suite above runs against `evals/providers/mock.py` (deterministic, zero-cost, no
credentials) — it verifies the harness plumbing, not real audit quality. `evals/providers/openai.py`
and `evals/providers/anthropic.py` call the real APIs for that (`--provider openai` / `--provider
anthropic`, each needs its SDK `pip install openai` / `pip install anthropic` plus `OPENAI_API_KEY` /
`ANTHROPIC_API_KEY` — neither is in `requirements.txt` since the rest of the tooling doesn't need them,
and neither has been run against a live key by the tooling in this repository).

Structural parity does not prove perfect semantic translation. Human or model-assisted bilingual review is still required for meaning-sensitive changes.

## Repository Layout

```text
.
├── *.en.md / *.sr.md        active prompt pairs (compiled release artifacts)
├── stacks/                  per-stack sections/, sections.<locale>.json manifests, stack.json, baselines
├── contracts/               shared modules extracted only after passing the 4-condition safety check
├── baselines/               dated primary-source manifests + schema.json + sources.json registry
├── evals/                   eval harness, provider adapters, fixtures, schemas, sandbox
├── reviews/                 Serbian revision reports
├── scripts/                 composer, validators, decomposition and migration tooling
├── .github/workflows/       CI (release gate on push/PR, source-link check nightly)
└── archive/v2.0.0/          frozen, tagged v2.0.0 snapshot + SECTION_INVENTORY.json used to prove zero loss
```

## Safety Notes

- Use only on systems you are authorized to inspect or change.
- Preserve evidence before destructive incident-response actions.
- Do not expose secrets, personal data, private keys or full database dumps in prompts or reports.
- A green build, passing checksum, successful deployment or absence of visible symptoms is not proof of production safety.
- Missing evidence must remain missing evidence, not be converted into a passing result.

## License And Contributions

See `LICENSE`, `CONTRIBUTING.md` and `SECURITY.md`.
