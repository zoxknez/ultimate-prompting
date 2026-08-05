## Phase 8 - Routing, Controllers, Input Mapping, Validation, Serialization, And API Contracts

### Objective

Prove every request is mapped, validated, authorized, executed, and serialized according to an explicit contract.

### Audit Requirements

- Inventory routes, hosts, methods, domains, prefixes, middleware, defaults, requirements, model binding, parameter conversion, fallback routes, and priorities.
- Detect route shadowing, ambiguous methods, unsafe wildcard routes, accidental public endpoints, debug routes, and environment-only routes in production.
- Validate path, query, header, cookie, body, multipart, file, JSON, XML, form, CLI, message, and webhook input at runtime.
- Separate structural validation, semantic validation, authorization, ownership checks, state checks, and external lookups.
- Prevent mass assignment with explicit DTOs, request objects, allowlists, serializer groups, writable-field policies, and domain commands.
- Verify response schemas, errors, Problem Details, pagination, filtering, sorting, expansion, includes, field masks, versioning, and generated clients.

### Required Evidence

- Route and command matrix with authentication, authorization, tenant, validation, transaction, idempotency, limits, and tests.
- OpenAPI or equivalent contract diff against actual runtime behavior.
- Negative tests for malformed, oversized, ambiguous, unauthorized, and cross-tenant input.

### Acceptance Criteria

- No critical endpoint relies on PHP types, UI restrictions, or ORM fillable defaults as its only runtime validation.
- Public and machine contracts are versioned, bounded, tested, and compatible or explicitly migrated.

