## 11. Registry, Artifact Promotion And Retention

**Objective:** Protect artifact identity, availability, confidentiality, and lifecycle.

### 11.1 Required Checks

1. Inventory registries, repositories, replication, geo placement, access paths, public visibility, retention, immutability, deletion protection, and owners.
2. Use immutable digests for deployment and treat tags only as human-friendly references unless immutability is enforced.
3. Verify push, pull, delete, replication, quarantine, promotion, and emergency access permissions separately.
4. Require verified signatures, provenance, policy results, and approved promotion evidence before production eligibility.
5. Test registry outage, rate limits, unavailable digest, deleted rollback artifact, replication lag, and compromised artifact response.
6. Align retention with rollback horizon, investigation needs, legal requirements, storage cost, and vulnerability response.

### 11.2 Minimum Evidence

- Registry permission and visibility matrix.
- Promotion evidence for a representative production artifact.
- Rollback-artifact availability and compromised-artifact drill result.

### 11.3 Exit Criteria

1. Production deploys resolve to approved immutable digests.
2. Rollback artifacts remain available for the defined recovery horizon.
3. Artifact quarantine, revocation, and replacement procedures are tested.

