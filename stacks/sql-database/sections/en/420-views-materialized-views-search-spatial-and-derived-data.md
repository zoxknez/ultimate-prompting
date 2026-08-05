## Views, Materialized Views, Search, Spatial, And Derived Data

Derived data must have explicit freshness, authority, refresh, invalidation and recovery contracts.

- Inventory views, materialized views, indexed views, search indexes, spatial indexes and summary tables.
- Verify ownership and authorization are not weakened by definer context or bypassed base-table policies.
- Define freshness SLO, refresh trigger, concurrency mode, failure behavior and catch-up procedure.
- Test schema changes and engine upgrades against stored definitions, parsers, tokenizers and spatial reference systems.
- Reconcile derived aggregates and search documents against authoritative tables.
- Include derived data rebuild time and storage in RTO and capacity plans.

