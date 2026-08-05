## Phase 10 - Symfony Application Path

### Objective

Audit effective Symfony behavior from kernel boot through HTTP, console, Messenger, Scheduler, Doctrine, cache, and deployment.

### Audit Requirements

- Verify exact Symfony patch, PHP range, Flex recipes, bundles, runtime component, environment selection, kernel configuration, and compiled container.
- Audit route loading, argument value resolvers, request mapping, validators, serializers, voters, access control, firewalls, authenticators, and exception listeners.
- Review service visibility, autowiring, autoconfiguration, aliases, decorators, compiler passes, lazy services, resettable services, and container optimization.
- Audit Doctrine ORM and DBAL integration, entity listeners, subscribers, filters, repositories, transaction middleware, migrations, and proxy generation.
- Verify Messenger transports, stamps, middleware, retries, failure transports, deduplication, worker limits, reset behavior, and graceful shutdown.
- Audit Scheduler, Lock, Cache, RateLimiter, Workflow, EventDispatcher, HttpClient, Mailer, Notifier, secrets vault, and debug component exposure.
- Verify cache warmup, environment-specific container compilation, asset handling, worker replacement, and zero-downtime release behavior.

### Required Evidence

- Effective container, route, firewall, service, transport, cache, and environment evidence from the production artifact.
- Negative authorization, serializer, validator, Messenger replay, and service reset tests.
- Cache warmup and worker replacement proof tied to one immutable release.

### Acceptance Criteria

- Compiled-container behavior matches reviewed source configuration and does not expose debug-only services or routes.
- Long-lived Symfony workers reset request-scoped state and process retries without violating business invariants.

