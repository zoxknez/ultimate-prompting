## Phase AF - Test Strategy And Verification Matrix

- Use unit tests for pure domain rules and property tests for invariants, parsers, money, dates and state machines.
- Use request and integration tests for middleware, sessions, CSRF, authorization, database constraints and external contracts.
- Use system tests for critical browser and Hotwire flows, including JavaScript, accessibility and stale-page behavior.
- Use job tests with the real adapter or faithful integration environment for retry, duplicate, crash and mixed-version behavior.
- Run concurrency and failure tests against a real supported database, cache and queue backend, not only transactional fixtures.
- Verify production asset build, eager load, release boot, migration, health, smoke, shutdown and rollback.

