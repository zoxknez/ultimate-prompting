## 12. Dart Language And Runtime Correctness

Review language semantics and runtime behavior that can invalidate business logic.

- Audit null safety, unsafe casts, `dynamic`, late initialization, non-null assertions, covariance, generic constraints, extension collisions, and exhaustiveness.
- Review equality, hashCode, identity, immutable models, copy semantics, collection mutation, ordering, deduplication, and cache-key correctness.
- Verify integer, double, decimal-money, date/time, timezone, locale, Unicode, normalization, regex, parsing, rounding, overflow, and precision behavior.
- Inspect exception taxonomy, `Error` versus `Exception`, zone behavior, unhandled async errors, stack preservation, retries, cancellation, and user-safe mapping.
- Audit JSON, protobuf, GraphQL, binary, XML, platform-channel, database, and cache serialization for versioning, unknown fields, defaults, malformed input, and backward compatibility.
- Search for hidden global state, static singletons, mutable service locators, test-order dependence, environment leakage, and isolate-unsafe assumptions.
- Verify tree-shaking and release-mode differences for assertions, reflection-like code generation, runtime type names, stack traces, and conditional imports.
- Require tests at boundaries, invalid inputs, minimum/maximum values, malformed payloads, clock changes, locale changes, and old persisted data.

