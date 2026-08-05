## Required Context

| Field | Value |
| --- | --- |
| System and business purpose | `[NAME / PURPOSE]` |
| Repository and commit | `[URL / PATH / SHA]` |
| Engine, edition and patch | `[...]` |
| Hosting and regions | `[...]` |
| Applications, drivers and ORM | `[...]` |
| Critical invariants | `[MONEY / INVENTORY / ACCESS / ORDERS / ...]` |
| Data volume and growth | `[...]` |
| SLO, RPO and RTO | `[...]` |
| Regulatory and privacy scope | `[...]` |
| Audit mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / PERFORMANCE_AUDIT / MIGRATION_AUDIT / INCIDENT_AND_RECOVERY]` |

If context is missing, derive it from source, migrations, runtime metadata, catalog views, monitoring and deployment configuration. Mark unresolved items `UNVERIFIED`; do not guess.

