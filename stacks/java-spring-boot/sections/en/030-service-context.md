## Service Context

| Field | Value |
| --- | --- |
| Service | `[NAME]` |
| Purpose | `[DESCRIPTION]` |
| Clients | `[WEB / MOBILE / DESKTOP / PARTNERS / PUBLIC]` |
| Architecture | `[MONOLITH / MODULAR MONOLITH / MICROSERVICE / WORKER / OTHER]` |
| Deployment | `[DOCKER / KUBERNETES / VM / SERVERLESS / OTHER]` |
| Runtime | `[JAVA / JDK DISTRIBUTION / SPRING BOOT VERSION]` |
| Data | `[POSTGRESQL / MYSQL / ORACLE / SQL SERVER / MONGODB / OTHER]` |
| Persistence | `[JPA / HIBERNATE / JDBC / R2DBC / OTHER]` |
| Authentication | `[SESSION / OIDC / JWT / MTLS / API KEY / OTHER]` |
| Critical operations | `[PAYMENTS / INVENTORY / FILES / LICENSES / OTHER]` |
| Repository | `[REPOSITORY]` |
| Expected behavior | `[EXPECTED_BEHAVIOR]` |
| Known problems | `[KNOWN_PROBLEMS]` |
| Messaging/cache/CI | `[MESSAGING / CACHE / CI_CD]` |
| Required baseline and constraints | `[REQUIRED_BASELINE / CONSTRAINTS]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES]` |
| Additional requirements | `[ADDITIONAL_REQUIREMENTS]` |

Code, build files, dependency locks, runtime configuration, executed commands, deployed artifact behavior, and database constraints are evidence. Documentation and roadmap files are context only.

When an input is absent, try to establish it from the project; mark it `UNVERIFIED` when that is impossible; use only the smallest clearly marked assumption when necessary. Never present an assumption as a fact.

