## Phase G - Constraints And Business Invariants

Place each invariant at the strongest atomic layer that can enforce it.

- Inventory primary, unique, foreign-key, check, exclusion, generated and partial constraints.
- Test uniqueness with NULL, collation, soft deletion, tenant scope and concurrent inserts.
- Verify foreign-key action, deferrability, indexing, delete behavior and orphan repair.
- Treat application check-then-write as unsafe when a database constraint or atomic statement is required.
- Verify trigger and stored-program invariants under bulk load, replication, disabled constraints and restore.
- Create reconciliation queries for every critical invariant.

