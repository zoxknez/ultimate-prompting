## Phase M - Active Record Models, Schema And Query Correctness

- Compare model validations with database `NOT NULL`, unique, foreign-key, check, exclusion and enum constraints.
- Audit association ownership, dependent behavior, counter caches, touch chains, nested attributes, STI, polymorphism and delegated types.
- Verify equality, identity, serialization, encrypted attributes, dirty tracking and callback ordering.
- Use logs, query traces and realistic data to confirm N+1, Cartesian joins, missing indexes, sequential scans and excessive object materialization.
- Review bulk insert/update/delete methods because many bypass validations, callbacks, timestamps or encryption behavior.

