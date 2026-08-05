## Phase E - Schema Authority And Drift

Compare every representation of the schema and migration history.

- Compare declarative schema, migration files, checksums, production catalogs, ORM models, generated clients and documentation.
- Detect objects created manually, missing migrations, edited historical migrations and divergent environment order.
- Compare types, nullability, defaults, generated expressions, collations, identity behavior and timezone semantics.
- Compare constraints, indexes, partitions, triggers, procedures, grants and row-level policies.
- Prove test schema creation matches production migration order and engine.
- Define the source of truth and a drift-detection control for each object class.

