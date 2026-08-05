## Sequences, Identity, Generated Keys, And Distributed ID Allocation

Prove uniqueness, exhaustion, ordering and recovery behavior for every identifier generator.

- Inventory sequences, identity columns, auto-increment, UUID or ULID generators, hi-lo allocation and external ID services.
- Review cache size, gaps, cycling, maximum value, signedness, failover and replica behavior.
- Verify restore, clone, shard split and environment copy cannot create overlapping ID ranges.
- Avoid business ordering assumptions based only on generated identifiers.
- Test concurrent allocation, rollback, retry and bulk import.
- Monitor exhaustion and define a migration plan before capacity becomes critical.

