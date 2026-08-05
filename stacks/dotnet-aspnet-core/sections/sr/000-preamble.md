---
prompt_id: dotnet-aspnet-core-production-audit
version: 2.0.0
title: Production Audit Za .NET, C#, ASP.NET Core I Entity Framework Core
language: sr
status: production-candidate
default_mode: AUDIT_AND_SAFE_FIX
baseline_date: 2026-08-05
requires:
  - core/audit-operating-contract.md
  - core/severity-model.md
  - core/final-report-schema.md
  - core/production-readiness-dod.md
---
# MASTER PROMPT - Dubinski Production Audit, Popravka I Unapredjenje .NET / C# / ASP.NET Core / Entity Framework Core Projekta

Koristi ovaj prompt za pregled, bezbednu popravku, proveru i pripremu stvarnog .NET sistema za produkciju. Audit mora da obuhvati ceo put od repozitorijuma i razresavanja SDK-a do publish artefakta, obrade zahteva, izmena podataka, pozadinskog rada, telemetrije, deployment-a, rollback-a i oporavka.

Cilj moze biti ASP.NET Core API, Minimal API, MVC ili Razor Pages aplikacija, Blazor aplikacija, gRPC servis, SignalR hub, worker servis, Windows servis, systemd servis, Azure Functions workload, container, Kubernetes workload, backend desktop aplikacije, modularni monolit, mikroservis, biblioteka, CLI, legacy .NET Framework sistem ili mesoviti solution.

