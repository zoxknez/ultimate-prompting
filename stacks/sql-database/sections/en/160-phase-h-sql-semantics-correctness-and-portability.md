## Phase H - SQL Semantics, Correctness, And Portability

Review generated and handwritten SQL for semantic correctness, not only syntax.

- Check three-valued logic, `NULL`, `NOT IN`, `IS DISTINCT FROM` alternatives and aggregate behavior.
- Check join cardinality, accidental Cartesian products, outer-join filters and duplicate multiplication.
- Require deterministic ordering and a stable unique tie-breaker for pagination and batch processing.
- Review implicit casts, type precedence, timezone conversion, collation coercion and numeric narrowing.
- Review upsert, merge, replace, returning, generated-key and affected-row semantics per engine.
- Test every production engine when shared SQL claims portability.

