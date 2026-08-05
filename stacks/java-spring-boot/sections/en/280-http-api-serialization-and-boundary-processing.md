## HTTP, API, Serialization, And Boundary Processing

### Endpoint And Contract Inventory

- Generate an inventory of MVC, WebFlux, functional, GraphQL, WebSocket, SSE, RSocket, gRPC, Actuator, management, callback, webhook, and internal endpoints.
- Record path, method, media type, version, audience, authentication, authorization, tenant rule, request limit, timeout, idempotency, transaction boundary, response contract, and owner.
- Compare runtime mappings with source, OpenAPI/AsyncAPI/GraphQL schemas, API gateway configuration, generated clients, tests, and documentation.
- Detect ambiguous mappings, shadowed routes, accidental Actuator exposure, test-only endpoints, deprecated versions, and management ports reachable from untrusted networks.
- Test direct access that bypasses UI, gateway, client-side checks, service mesh, or expected call order.

### HTTP And Proxy Semantics

- Verify trusted proxy boundaries, forwarded headers, scheme, host, port, client IP, path prefix, TLS termination, mutual TLS, and redirect construction.
- Test request smuggling variants, duplicate headers, conflicting content lengths, transfer encoding, oversized headers, malformed cookies, encoded paths, and normalization differences across hops.
- Define and verify timeout budgets for accept, headers, body, handler, downstream calls, response write, keep-alive, idle connections, streaming, and graceful shutdown.
- Review compression, decompression limits, range requests, conditional requests, caching headers, ETag semantics, redirects, retries, and safe/idempotent method treatment.
- Verify error mapping uses stable status codes and Problem Details without stack traces, secrets, internal identifiers, tenant data, or contradictory retry guidance.

### Serialization And Schema Evolution

- Inventory every `ObjectMapper`, codec, module, naming strategy, polymorphic configuration, date/time rule, numeric rule, unknown-field policy, and custom serializer/deserializer.
- Treat Jackson 2 and Jackson 3 as distinct compatibility surfaces; verify package changes, module availability, coercion defaults, polymorphism, and generated clients during migration.
- Audit JSON, XML, YAML, CSV, protobuf, Avro, Java serialization, Kryo, MessagePack, and custom binary formats for type confusion, gadget paths, entity expansion, depth, size, and allocation limits.
- Test old producer/new consumer, new producer/old consumer, absent fields, unknown fields, renamed enums, reordered fields, nullability, precision, large numbers, and duplicate keys.
- Version external contracts explicitly and prove database, event, cache, file, and API schema changes can coexist during rolling deployment and rollback.

### Validation, Files, Archives, And Webhooks

- Validate syntactic form, semantic meaning, authorization, ownership, state, quota, freshness, and cross-field invariants at the authoritative boundary.
- Apply explicit limits to request size, multipart parts, filenames, paths, dimensions, rows, cells, archive entries, decompressed bytes, recursion, parser time, and temporary storage.
- Prevent traversal, symlink escape, overwrite, polyglot content, content-type spoofing, formula injection, decompression bombs, malicious document/media parsing, and unsafe external converters.
- For webhooks, verify signature scheme, raw-body handling, timestamp window, key rotation, replay protection, event identity, ordering, idempotency, and acknowledgement strategy.
- Quarantine untrusted files and events until validation and scanning complete; define deletion, retention, privacy, retry, and forensic evidence behavior.


