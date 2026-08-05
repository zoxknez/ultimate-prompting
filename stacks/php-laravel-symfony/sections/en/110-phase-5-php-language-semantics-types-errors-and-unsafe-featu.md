## Phase 5 - PHP Language Semantics, Types, Errors, And Unsafe Features

### Objective

Identify language-level correctness and compatibility risks that static syntax success cannot prove.

### Audit Requirements

- Audit strict types boundaries, scalar coercion, union and intersection types, nullable values, enums, readonly state, property hooks, magic methods, and dynamic properties.
- Inspect equality, array-key coercion, numeric strings, integer overflow, floating-point money, decimals, timezone, DST, locale, Unicode, and serialization semantics.
- Trace exceptions, `Throwable`, error handlers, shutdown handlers, warnings converted to exceptions, fatal errors, deprecations, and partial-response behavior.
- Review `eval`, dynamic include, variable variables, reflection, attributes, closures, generators, fibers, weak references, FFI, and extension APIs.
- Audit `serialize` and `unserialize`, object injection, allowed classes, magic methods, Phar metadata, and format compatibility.
- Use PHPStan or Psalm, coding standards, mutation or property testing where justified, treating tool output as evidence rather than truth.

### Required Evidence

- Compatibility matrix for target PHP lines and critical extensions.
- Static-analysis baseline with suppressions, owners, expiry, and reachability review.
- Regression tests for every material coercion, error, serialization, time, money, or compatibility risk.

### Acceptance Criteria

- No critical invariant depends on undocumented coercion, magic behavior, or version-specific undefined behavior.
- Deprecations and compatibility blockers have owners, tests, and migration dates.

