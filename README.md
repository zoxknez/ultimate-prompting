# Ultimate Prompting

**Production-grade master audit prompts** for AI coding agents (Grok, Claude, Cursor, Codex, and similar).

Each prompt turns a general-purpose agent into a **truth-first principal engineer**: inventory first, evidence before claims, minimal safe fixes, regression tests, and an honest production-readiness verdict.

Research baseline date for version tables: **4 August 2026**.  
Baselines are starting points — agents must re-check official sources at audit time.

---

## Why this exists

Most “audit my app” prompts produce generic best-practice lists.

These prompts require the agent to:

1. **Protect** the workspace (git, secrets, signing keys, uncommitted work)
2. **Map** real architecture, runtimes, and deployment units
3. **Verify** versions, lifecycle, and EOL from primary sources
4. **Run** real install/build/test/security commands (or mark `UNVERIFIED`)
5. **Separate** confirmed findings from suspicion
6. **Fix** only when the work mode allows — smallest defensible change
7. **Prove** repairs with regression tests
8. **Document** exact commands, exits, and residual risk
9. **Refuse** to invent command output, CVEs, or green tests

> Code that compiles is not production-ready.  
> Passing tests are not proof of security.  
> Local startup is not proof of deployability.

---

## Repository layout

```text
ultimate-prompting/
├── README.md
├── .gitignore
└── *-audit-prompt.{en,sr}.md    # 16 stacks × EN + SR = 32 prompts
```

| Suffix | Language |
| ------ | -------- |
| `.en.md` | English |
| `.sr.md` | Serbian (ASCII-friendly technical Serbian) |

Same structure and depth in both languages (1:1 section parity).

---

## Catalog (16 stacks)

| # | Domain | Files | Focus |
| - | ------ | ----- | ----- |
| 1 | **AI / RAG / LLM / Agents / MCP** | `ai-rag-llm-agent-audit-prompt.*` | Retrieval ACL, tools, injection, eval, cost, kill switch |
| 2 | **Android / Kotlin / Compose** | `android-master-audit-prompt.*` | Gradle/AGP, lifecycle, Compose, 16 KB pages, Play release |
| 3 | **DevOps / Docker / Kubernetes** | `devops-docker-kubernetes-audit-prompt.*` | Images, RBAC, probes, supply chain, backup/restore |
| 4 | **.NET / ASP.NET Core / EF Core** | `dotnet-aspnet-core-audit-prompt.*` | .NET 10 LTS, auth, Data Protection, EF, publish |
| 5 | **Electron / Tauri desktop** | `electron-tauri-desktop-audit-prompt.*` | Webview isolation, IPC/capabilities, signing, updater |
| 6 | **Flutter / Dart** | `flutter-dart-mobile-audit-prompt.*` | Channels/FFI, offline, 16 KB, stores, multi-platform |
| 7 | **Go / Rust backends** | `go-rust-backend-audit-prompt.*` | Race/Miri, modules/crates, concurrency, supply chain |
| 8 | **Java / Spring Boot** | `java-spring-boot-audit-prompt.*` | Boot 4.x, Security, JPA, Actuator, migrations |
| 9 | **Next.js / React** | `nextjs-master-audit-prompt.*` | RSC, Server Actions, cache privacy, Vercel/deploy |
| 10 | **Node.js / Express** | `node-express-api-audit-prompt.*` | Event loop, Express 5, authz, jobs, TypeScript 7 |
| 11 | **PHP / Laravel / Symfony** | `php-laravel-symfony-audit-prompt.*` | FPM vs Octane, Composer, Eloquent/Doctrine, queues |
| 12 | **Python / PySide6 desktop** | `python-pyside6-desktop-audit-prompt.*` | Qt threads, packaging, updater, subprocess safety |
| 13 | **React Native / Expo** | `react-native-expo-mobile-audit-prompt.*` | New Arch, Hermes, EAS/OTA `runtimeVersion`, stores |
| 14 | **Ruby / Rails** | `ruby-rails-audit-prompt.*` | Puma pools, Solid Queue/Sidekiq, AR, Kamal |
| 15 | **SQL / PostgreSQL / MySQL / SQLite** | `sql-database-audit-prompt.*` | Constraints, plans, PITR, restore-tested backups |
| 16 | **WordPress security & recovery** | `wordpress-security-recovery-hardening-prompt.*` | Forensics first, containment, rebuild, hardening |

---

## How to use

### 1. Pick the stack prompt

Example: full-stack Node API → `node-express-api-audit-prompt.en.md`  
Example: Rails monolith → `ruby-rails-audit-prompt.en.md`  
Example: compromised WP site → `wordpress-security-recovery-hardening-prompt.en.md`

### 2. Fill the context table

At the top of each prompt, replace placeholders:

```text
[NAME], [REPO], [WORKLOAD], [DEPLOYMENT], [REŽIM_RADA], …
```

### 3. Set the work mode

If omitted, agents default to **`AUDIT_AND_SAFE_FIX`**.

| Mode | Behavior |
| ---- | -------- |
| `AUDIT_ONLY` | Analyze and run safe checks; no source/lock/schema changes |
| `AUDIT_AND_SAFE_FIX` | Confirmed low-risk fixes + regression tests; plan large changes |
| `FULL_IMPLEMENTATION` | Justified fixes in small steps; backup before destructive work |
| `FIX_CONFIRMED_ISSUES` | Only previously registered confirmed issues |
| Stack-specific | e.g. `SECURITY_AUDIT`, `MIGRATION_AUDIT`, `PERFORMANCE_AUDIT`, `RELEASE_AND_OTA_AUDIT`, `INCIDENT_AND_RECOVERY` |

### 4. Paste into the agent

Use as:

- system / project instruction,
- first message in a coding session,
- or `.cursor` / agent skill body.

### 5. Demand the mandatory deliverables

Every prompt ends with a **final report** contract, typically:

- verdict: `ready` / `ready-with-conditions` / `not-ready`
- version / lifecycle table
- architecture map
- P0–P3 findings with evidence
- command log (real exits only)
- residual risk and blockers
- external sources consulted (URL + date)

---

## Anatomy of a master prompt

```text
Research baseline (dated version table)
  → Role & mission
  → Technology paths (framework / runtime / platform)
  → Project context table
  → Work modes
  → Operating contract (truth-first)
  → Finding register schema
  → Phases A…R (inventory → fix → release)
  → Severity P0–P3
  → Production checklist
  → Definition of Done
  → Forbidden behaviors
  → Final report template
  → Work order & priorities
```

### Evidence statuses

| Status | Meaning |
| ------ | ------- |
| `CONFIRMED` / `POTVRĐENO` | Hard evidence (code, config, command, test, runtime) |
| `PARTIALLY_CONFIRMED` | Strong signal, missing environment/runtime piece |
| `UNVERIFIED` / `NEPROVERENO` | Could not run or incomplete access |
| `NOT_APPLICABLE` | Outside project scope |
| `REJECTED` / `ODBAČENO` | Checked and not a real issue |

### Severity (shared philosophy)

| Priority | Typical meaning |
| -------- | --------------- |
| **P0** | Unauthorized access, RCE, secret exposure, data loss, unrecoverable deploy |
| **P1** | Critical authz/race/idempotency/outage patterns, unsafe migrations |
| **P2** | Localized defects, measured perf, weak observability |
| **P3** | Docs, naming, hygiene |

---

## Design principles

1. **Truth-first** — no invented command output, CVEs, or test results  
2. **Protect first** — secrets, signing keys, production DBs, user data  
3. **Read-only first** — especially databases, migrations, destructive DDL  
4. **Engine-specific** — PostgreSQL ≠ MySQL ≠ SQLite; Electron ≠ Tauri; FPM ≠ Octane  
5. **Measure performance** — no “it’s slow” / “YJIT helps” without data  
6. **Restore-tested backups** — a backup that was never restored is not proven  
7. **Minimal diffs** — no framework rewrites for fashion  
8. **Honest verdicts** — if DoD fails: *not fully production-ready* + blockers  

---

## Baseline snapshot (4 August 2026)

High-level pins used in prompt tables (always re-verify):

| Ecosystem | Snapshot highlights |
| --------- | ------------------- |
| .NET | .NET **10** LTS (e.g. 10.0.10), C# 14, EF Core 10 |
| Java | Java **25** LTS, Spring Boot **4.1.x** |
| Go / Rust | Go **1.26.x**, Rust **1.97.x**, Edition 2024 |
| Node / Next | Node **24** LTS, Express **5.x**, Next **16.3.x**, TS **7.x** |
| PHP | PHP **8.4/8.5** preferred, Laravel **13**, Symfony **7.4** LTS |
| Ruby | Ruby **4.0.x**, Rails **8.1.x**, Solid Queue default |
| SQL | PostgreSQL **18**, MySQL **9.7/8.4** LTS, SQLite **3.53.x** |
| Desktop | Electron **43.x**, Tauri **2.11.x** |
| Mobile | Flutter **3.44.x**, Expo SDK **57** / RN **0.86**, New Arch only |
| WordPress | WP **7.0.x**, PHP **8.3+** recommended |

---

## Contributing

- Keep **EN and SR pairs in sync** (same sections, same depth).  
- Prefer **ASCII-friendly Serbian** in `.sr.md` for tooling portability.  
- Update research baselines with **primary sources** + access date.  
- Do not add secrets, real credentials, or production dumps.  
- Prefer small, reviewable edits over drive-by rewrites of every prompt.

Suggested commit style:

```text
docs: refresh .NET baseline for 2026-08
feat: add Electron/Tauri master audit prompt
fix: align Flutter EN/SR section parity
```

---

## License

MIT — free to use, modify, and embed in internal agent workflows.

If you publish derivatives, a link back to this repository is appreciated but not required.

---

## Maintainer

- GitHub: [zoxknez/ultimate-prompting](https://github.com/zoxknez/ultimate-prompting)

---

## Quick start (agent session)

```text
You are executing the master audit prompt below.

Work mode: AUDIT_AND_SAFE_FIX
Repository: <path or URL>
Stack prompt: node-express-api-audit-prompt.en.md

Rules:
- Never invent command output.
- Mark unrun checks as UNVERIFIED with reason.
- Deliver the mandatory final report and DoD checklist.
```

Then paste the full contents of the chosen `*.md` file.
