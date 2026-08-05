## Phase I - Input Safety, Injection, And Dynamic SQL

Prove that data and identifiers cannot cross into executable SQL unsafely.

- Use parameters for values and strict allowlists plus correct quoting for identifiers and sort expressions.
- Inspect ORM raw SQL, query fragments, stored procedures, migration generators and administrative scripts.
- Review multi-statement settings, client-side emulation, prepared-statement modes and encoding boundaries.
- Bound JSON paths, full-text syntax, regular expressions, spatial input and user-defined expressions.
- Prevent second-order injection through stored data later reused in DDL, export, shell or template contexts.
- Test malformed encodings, comments, separators, duplicate parameters and driver-specific edge cases.

