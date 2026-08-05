## Phase O - Migrations, Multiple Databases, Shards And Replicas

- Inventory primary, replica, shard, queue, cache and cable databases and identify migration ownership for each.
- Use expand-and-contract for destructive changes and prove old and new application versions can coexist.
- Separate schema migration, data backfill, verification, cutover and cleanup into observable restartable steps.
- Verify lock duration, statement timeout, index creation method, table rewrite risk and replication lag.
- Test read-after-write behavior, role switching, replica lag, shard routing, tenant move and failover.
- Do not run migrations automatically from every web replica. Establish a single controlled migration owner.

