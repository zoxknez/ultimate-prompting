## 1. Current Research Baseline - Re-Check Before Every Audit

This baseline is a starting point, not a substitute for verification at execution time. Re-check current Microsoft first-party sources and the actual project before recommending or changing anything.

| Component | Baseline on 5 August 2026 | Mandatory audit-time verification |
| --- | --- | --- |
| .NET 10 | Current production LTS line; latest patch listed on the support page is 10.0.10 (released 14 July 2026); supported until 14 November 2028. | `dotnet --info`, `global.json`, TFM, production runtime/image, and patch policy. |
| Older lines | .NET 8 LTS and .NET 9 STS are in maintenance; both reach EOL on 10 November 2026. They are not a new long-term baseline without a clear reason. | Actual lifecycle, OS support, and upgrade plan. |
| C# | C# 14 is the stable language release tied to .NET 10. A language version newer than the one associated with the target framework is not supported. | `LangVersion`, SDK, CI/IDE/generator/analyzer, and TFM compatibility. |
| Preview | .NET 11 and C# 15 are preview technologies at the baseline date. | `allowPrerelease`, preview SDK/packages, and explicit production approval. |
| EF Core | EF Core 10 is LTS, requires .NET 10 SDK/runtime, and is supported until 10 November 2028. (Note: .NET 10 runtime support lasts until 14 November 2028 — the dates are not identical.) EF Core 9 → 10 migrations require review of behavioral and source-breaking changes. | EF runtime/tools/provider versions, breaking-change catalog, and provider compatibility. |
| Breaking changes | An upgrade is not only a `TargetFramework` change; there is a catalog of binary, source, and behavior incompatibilities. | Compatibility catalog, release notes, and tests for affected flows. |
| NuGet audit | For `net10.0`, NuGet Audit defaults to direct and transitive packages (`NuGetAuditMode=all`). Repository-level audit, package source mapping, lock files, and locked restore are supported. | Effective NuGet/MSBuild configuration, audit sources, suppressions, and resolved graph. |
| Migrations | Microsoft recommends reviewed SQL scripts, migration bundles, or a controlled migration job; automatic startup `Database.Migrate()` carries operational risk. | Provider, SQL, lock/duration, rollout, backup/PITR, and recovery. |
| Data Protection | The key ring must be persisted, protected, and available to all replicas; it is used for cookies, antiforgery, and protected payloads. | Storage, encryption-at-rest, application discriminator, permissions, rotation, backup, and DR. |
| Resilience | Use `Microsoft.Extensions.Resilience` and `Microsoft.Extensions.Http.Resilience`; `Microsoft.Extensions.Http.Polly` is deprecated. | Pipeline, timeout/retry bounds, telemetry, idempotency, and upgrade path. |

Note: a claim that a patch was released on 10 November 2026 is not temporally possible on this baseline date; do not treat it as fact. At real audit time always use the current release/support record.

