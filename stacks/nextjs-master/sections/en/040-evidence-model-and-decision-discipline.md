## Evidence Model And Decision Discipline

### Evidence Levels E0-E5

| Level | Meaning | Examples |
| --- | --- | --- |
| E0 | Claim, ticket, roadmap, or assumption | README claim or undocumented diagram |
| E1 | Static source, config, schema, or declaration | package.json, next.config, route source |
| E2 | Resolved or generated evidence and artifact metadata | lock graph, route manifest, digest, SBOM |
| E3 | Executed local or integration evidence | production build/start, browser or migration test |
| E4 | Staging or production-like load, failure, rollout, or rollback evidence | canary, load, cache-isolation, rollback drill |
| E5 | Production observation, isolated restore, or incident drill | release telemetry, real restore validation |

### Finding Status

- CONFIRMED requires sufficient evidence to reproduce or directly demonstrate the claim.
- PARTIALLY_CONFIRMED means part of the causal chain is proven but a runtime, browser, platform, or recovery step remains missing.
- UNVERIFIED means required evidence is unavailable, unsafe, blocked, or not executed.
- NOT_APPLICABLE requires a concrete scope reason.
- REJECTED means the tested hypothesis was disproven and the disproof evidence is preserved.

### Mandatory Finding Record

```text
ID / Severity P0-P3 / Status / Evidence level
Area / Route / File / Runtime / Actor or tenant
Invariant / Evidence / Command / Exit code / Reproduction
Root cause / Failure or exploit path / Impact / Blast radius
Minimal repair / Alternatives rejected / Regression test
Rollout / Rollback / Monitoring / Residual risk / Owner
```

