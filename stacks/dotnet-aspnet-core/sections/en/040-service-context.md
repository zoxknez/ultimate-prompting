## Service Context

| Field | Value |
| --- | --- |
| Service | `[NAME]` |
| Purpose | `[DESCRIPTION]` |
| Clients | `[WEB / MOBILE / DESKTOP / PARTNERS / PUBLIC]` |
| Architecture | `[MONOLITH / MODULAR MONOLITH / MICROSERVICE / WORKER / OTHER]` |
| Deployment | `[DOCKER / KUBERNETES / IIS / AZURE / VPS / SERVERLESS / OTHER]` |
| Runtime | `[TARGET FRAMEWORK / SDK / HOST OS]` |
| Data | `[SQL SERVER / POSTGRESQL / MYSQL / SQLITE / COSMOS / OTHER]` |
| Authentication | `[COOKIE / OIDC / JWT / API KEY / MTLS / OTHER]` |
| Critical operations | `[PAYMENTS / INVENTORY / FILES / LICENSES / OTHER]` |
| Repository/archive | `[REPOSITORY]` |
| Solution root | `[SOLUTION_ROOT]` |
| Expected behavior | `[EXPECTED_BEHAVIOR]` |
| Known problems | `[KNOWN_PROBLEMS]` |
| Workload | `[WORKLOAD]` |
| Hosting/OS | `[HOSTING / OS]` |
| Messaging/cache/storage | `[MESSAGING / CACHE / STORAGE]` |
| Identity/deployment/CI | `[IDENTITY_PROVIDER / DEPLOYMENT / CI_CD]` |
| Baseline/compatibility | `[REQUIRED_BASELINE / COMPATIBILITY]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |
| Regulatory and extra constraints | `[REGULATORY / CONSTRAINTS]` |

Code, project files, lock files, runtime configuration, executed commands, deployed artifact behavior, and database constraints are evidence. Documentation and roadmap files are context only.

When an input is absent, try to establish it from the solution, configuration, CI, and deployment artifacts; otherwise mark it `UNVERIFIED`. Do not assume Azure, SQL Server, Windows hosting, a stateless architecture, or an ASP.NET Core app merely because C#/.NET is present.

