## Resource Governance, Timeouts, Cancellation, And Workload Isolation

Prevent one query, tenant, report, migration or maintenance task from exhausting shared resources.

- Define statement, lock, transaction, idle, connection-acquisition and administrative timeouts.
- Verify client cancellation reaches the server and releases transactions, locks, memory and temporary files.
- Separate OLTP, reporting, migration, backup, CDC and administrative workloads where needed.
- Use quotas, resource groups, admission control, concurrency caps or replicas with measured tradeoffs.
- Test maliciously expensive filters, sorts, joins, regex, JSON, full-text and export requests.
- Alert on cancellation failure, runaway sessions, repeated timeout and workload starvation.

