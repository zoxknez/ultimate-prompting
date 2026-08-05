## Phase 10 - Parsing, Runtime Validation, Serialization, And Output Safety

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Treat path, query, headers, cookies, body, multipart fields, files, metadata, and upstream responses as untrusted.
- Define body, field, depth, array, string, number, file-count, header, decompression, and total request limits.
- Apply structural schemas, semantic validation, cross-field rules, authorization-aware constraints, and field allowlists.
- Prevent mass assignment, prototype pollution, unsafe merge, coercion ambiguity, duplicate-key ambiguity, and precision loss.
- Validate dates, time zones, durations, money, identifiers, Unicode normalization, and regex complexity.
- Define output schemas or serializers for sensitive APIs and verify error and alternate response paths use them.

### Required Evidence

- Produce and preserve the input and output schema inventory.
- Produce and preserve the limit, coercion, and field-allowlist matrix.
- Produce and preserve serialization and content-type evidence.

### Mandatory Failure And Acceptance Tests

- Prove that oversized and deeply nested input is rejected cheaply.
- Prove that prototype keys cannot modify application objects.
- Prove that private fields never appear through alternate response paths.

