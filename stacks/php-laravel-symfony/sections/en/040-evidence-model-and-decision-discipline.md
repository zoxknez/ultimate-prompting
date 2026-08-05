## Evidence Model And Decision Discipline

### Evidence Levels E0-E5

| Level | Meaning | Examples |
| --- | --- | --- |
| E0 | Claim, ticket, roadmap, or assumption | README claim or undocumented note |
| E1 | Static source, configuration, schema, or declaration | composer.json, route source, ORM mapping, php.ini template |
| E2 | Resolved, generated, or artifact evidence | composer.lock graph, optimized autoload, container digest, SBOM |
| E3 | Executed local or integration evidence | production bootstrap, integration, migration, worker, or security test |
| E4 | Staging or production-like load, failure, rollout, or rollback evidence | soak, queue replay, canary, worker drain, rollback drill |
| E5 | Production observation, isolated restore, or incident drill | release telemetry, restore validation, containment exercise |

### Finding Status

- CONFIRMED requires evidence that reproduces or directly demonstrates the material claim.
- PARTIALLY_CONFIRMED means part of the causal chain is proven but a runtime, network, data, load, or recovery step is missing.
- UNVERIFIED means required evidence is unavailable, unsafe, blocked, or not executed.
- NOT_APPLICABLE requires a concrete scope reason.
- REJECTED means the tested hypothesis was disproven and the disproof evidence is preserved.

### Mandatory Finding Record

```text
ID / Severity P0-P3 / Status / Evidence level
Area / Framework / Entrypoint / Route / Job / File / Runtime / Actor / Tenant
Invariant / Evidence / Command / Exit code / Reproduction
Root cause / Failure or exploit path / Impact / Blast radius
Minimal repair / Alternatives rejected / Regression test
Rollout / Rollback / Monitoring / Residual risk / Owner
```

