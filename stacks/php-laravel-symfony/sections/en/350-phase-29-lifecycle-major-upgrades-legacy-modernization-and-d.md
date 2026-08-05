## Phase 29 - Lifecycle, Major Upgrades, Legacy Modernization, and Decommissioning

### Objective

Plan supported-version operation, framework and runtime migration, compatibility, rollback, and retirement without hidden risk.

### Audit Requirements

- Track PHP, framework, Composer, extensions, database drivers, operating systems, web servers, libraries, and services against official support windows.
- Inventory deprecated PHP features, framework APIs, recipes, bundles, packages, annotations, configuration formats, and behavioral changes.
- For Laravel major upgrades, verify PHP requirements, first-party package support, skeleton changes, auth, queue, cache, database, test, and deployment compatibility.
- For Symfony major or LTS migrations, verify recipes, Flex, bundle support, deprecations, container, security, serializer, Messenger, Doctrine, and Runtime changes.
- Run dual-line compatibility tests, representative data migrations, mixed-version deployment, performance comparison, canary, rollback, and forward repair.
- Remove abandoned packages, insecure plugins, dead routes, debug tools, unused credentials, obsolete infrastructure, and unsupported runtime paths with evidence.

### Required Evidence

- Support and upgrade matrix with owner, deadline, blockers, compatibility evidence, and rollback.
- Dual-version build, test, data, load, deployment, and recovery evidence.
- Decommission evidence for code, routes, packages, secrets, data, workers, infrastructure, and observability.

### Acceptance Criteria

- No unsupported or abandoned component remains on a critical production path without an approved, time-bound mitigation.
- Upgrade and retirement plans preserve data, contracts, authority, operations, and a tested recovery path.

