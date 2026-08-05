## Research Baseline - 5 August 2026

This is a dated starting point. Re-check official sources, the lockfile, installed packages, container image, OS distribution, architecture, libc, extensions, SAPI, web server, process manager, and the running process before every lifecycle, migration, security, or compatibility decision.

| Component | Baseline | Mandatory audit-time verification |
| --- | --- | --- |
| PHP | 8.5 active; 8.4 active until 31 Dec 2026; 8.3 and 8.2 security-only at the baseline date. | Exact patch, support phase, build options, SAPI, architecture, extensions, INI, image, and provider support. |
| PHP patches | 8.5.9 is listed in the official PHP 8 changelog on 30 Jul 2026. | Re-check the latest patch for every deployed minor line; never infer from a local CLI only. |
| Laravel | 13.x stable; requires PHP 8.3-8.5; Laravel 12 remains supported within its published window. | Exact framework patch, PHP matrix, first-party packages, upgrade guide, deployment model, and advisories. |
| Symfony | 8.1 is the current stable line; 7.4 is the current LTS; 6.4 remains an older supported LTS. | Exact component patches, PHP requirement, Flex recipes, bundle support, deprecations, and selected LTS strategy. |
| Composer | 2.10.2 latest stable at the baseline date; 2.2 LTS exists for constrained legacy environments. | Actual binary, installer verification, plugins, repositories, audit behavior, platform config, and lock reproducibility. |
| Runtime model | FPM and mod_php are request-scoped; Octane, FrankenPHP worker mode, RoadRunner, Swoole, ReactPHP, and Amp retain process state. | Actual SAPI and worker mode, reset semantics, process lifetime, reload, drain, memory growth, and mixed-version behavior. |

### Primary Source Policy

- Use official PHP, Laravel, Symfony, Composer, framework package, database, web-server, process-manager, hosting-platform, OpenTelemetry, OWASP, and standards documentation.
- Record source title, URL, access date, exact claim, selected version, and repository or runtime evidence that confirms or contradicts it.
- Do not replace lifecycle, security, migration, transaction, or protocol guidance with snippets, popularity, summaries, or AI-generated claims.
- When official sources and runtime evidence conflict, show the conflict and keep the decision conditional until the exact artifact and process are verified.

