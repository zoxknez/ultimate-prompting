## Multi-Database And Cross-System Consistency

When a business flow spans databases or services, document the absence of a single atomic boundary.

- Map the authoritative system for each field, object and state transition.
- Review distributed transaction use, two-phase commit, prepared transaction retention and coordinator failure.
- Prefer explicit saga, outbox, inbox and reconciliation contracts when global atomicity is unavailable.
- Test duplicate, missing, reordered and delayed cross-system events.
- Define conflict authority and manual repair for divergent systems.
- Include external-system state in rollback, restore and disaster-recovery planning.

