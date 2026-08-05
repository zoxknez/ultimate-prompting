## Phase P - Test Strategy And Fixes

Inventory: unit, integration, race, fuzz, Miri/sanitizer, contract, security, concurrency, migration, E2E, load, recovery, publish smoke.

Every P0–P2 fix requires a test that demonstrates the old incorrect and new correct behavior.

Before changing: finding, hypothesis, minimal change, preserved contract, risk, test that could disprove, rollback. Change the smallest file set. Do not modify `go.mod`/`go.sum`/`Cargo.lock` without review.

