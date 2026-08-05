## Phase 1 - System Topology, Entrypoints, And Trust Boundaries

### Objective

Map the real application, process, data, identity, and network topology before evaluating controls.

### Audit Requirements

- Enumerate HTTP front controllers, CLI commands, queue consumers, scheduler tasks, migrations, realtime servers, and webhook receivers.
- Map CDN, WAF, load balancer, ingress, reverse proxy, web server, FPM socket, application process, database, broker, cache, and storage hops.
- Identify actors, service identities, tenants, administrators, support users, providers, and machine-to-machine callers.
- Classify authoritative stores, replicas, caches, indexes, derived projections, files, and external systems of record.
- Mark trust transitions for headers, cookies, tokens, message metadata, tenant identifiers, file names, URLs, serialized payloads, and environment variables.
- Assign ownership and escalation paths for each executable, data store, integration, secret, and recovery procedure.

### Required Evidence

- Architecture and trust-boundary diagram tied to real configuration and deployment evidence.
- Entrypoint and owner inventory with runtime, identity, data access, and side effects.
- Critical journey and dependency map including degraded and failure paths.

### Acceptance Criteria

- No externally reachable or privileged entrypoint remains unmapped.
- Every critical invariant has an authoritative owner and enforcement layer.

