## Phase 7 - Fastify 5, Plugins, Encapsulation, And Schemas

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Identify exact Fastify core and plugin versions and verify LTS and Node support compatibility.
- Map the plugin DAG, registration order, prefixes, decorators, hooks, schemas, and encapsulation boundaries.
- Detect accidental global exposure, missing decorator dependencies, duplicate registration, and scope-dependent behavior.
- Treat JSON Schema definitions as application code because validators and serializers may compile them dynamically.
- Never compile user-provided schemas; review Ajv options, formats, keywords, shared IDs, and serializer behavior.
- Keep database or external calls out of initial schema validation and use appropriate hooks for async checks.

### Required Evidence

- Produce and preserve the plugin and encapsulation graph.
- Produce and preserve the schema, serializer, and hook inventory.
- Produce and preserve core and plugin support evidence.

### Mandatory Failure And Acceptance Tests

- Prove that a sibling plugin cannot access an unintended decorator.
- Prove that untrusted schema input is rejected before compilation.
- Prove that response serialization prevents private-field leakage.

