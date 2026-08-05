## Deployment, CI/CD, Release, Rollback, And Incident Response

### Packaging And Runtime Environment

- Verify the exact JAR, layered JAR, WAR, native image, container, server package, or platform artifact promoted to each environment by immutable digest.
- Inspect container base image, JRE contents, trust store, locale, timezone data, user, filesystem permissions, capabilities, resource limits, read-only paths, temp space, and signal handling.
- Verify reverse proxy, servlet container, JVM flags, environment, mounted configuration, secrets, agents, sidecars, service mesh, DNS, certificates, and startup command in the deployed revision.
- Do not rebuild between environments; promote the same reviewed artifact and change only controlled environment configuration.
- Test installation, startup, readiness, traffic, shutdown, restart, node replacement, image pull, registry outage, configuration error, and secret rotation.

### CI/CD And Artifact Trust

- Map repository protections, approvals, runner trust, fork behavior, tokens, OIDC, environment gates, secrets, caches, artifacts, reusable workflows, plugins, and deployment identities.
- Pin third-party actions, images, plugins, wrappers, and downloaded tools by immutable version or digest with an update and revocation process.
- Separate untrusted pull-request execution from release credentials, signing keys, production networks, package publication, and mutable caches.
- Generate and retain test evidence, dependency graph, SBOM, provenance, signatures where used, artifact digest, migration plan, release notes, and approval trail.
- Verify deployment consumes only the reviewed artifact and that provenance or signatures are actually checked where policy claims enforcement.

### Rollout, Compatibility, And Rollback

- Define preconditions, canary cohort, traffic progression, observation windows, SLO and invariant guardrails, abort thresholds, owner, and rollback authority.
- Test old/new application versions with old/new schema, events, cache values, sessions, tokens, clients, jobs, and background workers during overlap.
- Separate application rollback, configuration rollback, feature disablement, traffic shift, schema forward repair, data reconciliation, and infrastructure rollback.
- Prove rollback does not corrupt data, replay irreversible effects, lose messages, invalidate sessions unexpectedly, or start incompatible old code against a changed schema.
- Rehearse rollback from partial rollout, failed migration, dependency incident, security revocation, performance regression, and corrupted configuration.

### Incident And Trusted-Recovery Mode

- Define triggers for security, data-integrity, availability, privacy, supply-chain, signing-key, certificate, dependency, and migration incidents.
- Preserve timelines, release identities, digests, configuration, logs, traces, database evidence, broker offsets, audit records, and relevant volatile evidence with controlled access.
- Provide kill switches, credential and key revocation, traffic isolation, consumer pause, job pause, write freeze, feature disablement, and safe degraded modes.
- Rebuild from trusted source and toolchain after supply-chain compromise; do not treat redeployment of an untrusted artifact as remediation.
- Require post-recovery verification of business invariants, tenant isolation, balances, queues, indexes, files, callbacks, alerts, and monitoring before closure.


