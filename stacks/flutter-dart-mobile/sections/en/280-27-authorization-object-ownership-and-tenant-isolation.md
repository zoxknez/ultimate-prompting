## 27. Authorization, Object Ownership, And Tenant Isolation

The client can improve UX but cannot be the authoritative security boundary.

- Map every privileged action, object lookup, mutation, export, share, upload, download, admin flow, support flow, and tenant-scoped query.
- Verify server-side authentication, permission, role, resource ownership, tenant membership, status, quota, and business-invariant checks.
- Treat route guards, hidden buttons, local roles, cached entitlements, feature flags, and disabled controls as presentation only.
- Prevent BOLA/IDOR by testing changed identifiers, stale links, another user, another tenant, deleted membership, downgraded role, and revoked share.
- Verify local cache keys, database partitions, file paths, search indexes, notification payloads, analytics, and background tasks include correct account and tenant identity.
- Test account switch and tenant switch during in-flight reads, writes, uploads, downloads, realtime events, migration, and restoration.
- Audit impersonation and delegated access with explicit actor, subject, purpose, duration, scope, logging, user visibility, and revocation.
- Require negative authorization tests at API, repository, state, route, storage, notification, and UI integration layers.

