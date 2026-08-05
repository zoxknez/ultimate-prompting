## Change Governance, Review, And Production Access

Database changes require stronger controls because effects can be durable, global and hard to reverse.

- Require peer review for DDL, destructive DML, role changes, backup policy, failover automation and retention changes.
- Use immutable reviewed scripts or migration artifacts with checksums and environment guards.
- Separate request, approval, execution and audit identities for high-risk actions.
- Use just-in-time privileged access, session recording and automatic expiry where supported.
- Prohibit shared administrative accounts and undocumented production console changes.
- Review emergency changes after the incident and convert them into managed source-controlled state.

