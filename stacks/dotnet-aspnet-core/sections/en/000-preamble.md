---
prompt_id: dotnet-aspnet-core-production-audit
version: 2.0.0
title: .NET, C#, ASP.NET Core and Entity Framework Core Production Audit
language: en
status: production-candidate
default_mode: AUDIT_AND_SAFE_FIX
baseline_date: 2026-08-05
requires:
  - core/audit-operating-contract.md
  - core/severity-model.md
  - core/final-report-schema.md
  - core/production-readiness-dod.md
---
# MASTER PROMPT - Deep Production Audit, Repair, And Improvement Of A .NET / C# / ASP.NET Core / Entity Framework Core Project

Use this prompt to inspect, safely repair, verify, and prepare a real .NET system for production. Audit the complete path from repository and SDK resolution to published artifact, request processing, data changes, background execution, telemetry, deployment, rollback, and recovery.

The target may be an ASP.NET Core API, Minimal API, MVC or Razor Pages application, Blazor application, gRPC service, SignalR hub, worker service, Windows service, systemd service, Azure Functions workload, container, Kubernetes workload, desktop backend, modular monolith, microservice, library, CLI, legacy .NET Framework system, or a mixed solution.

