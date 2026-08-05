## 13. Local Data, Databases, Files, And Recovery

### 13.1 Data Inventory And Classification

1. Inventory every persistent location: app data, user data, config, cache, logs, crash dumps, temp, downloads, databases, browser profiles, cookies, secure storage, OS credentials, keychain, registry/plist, shared containers, and removable/network storage.
2. Classify data by owner, account/tenant, sensitivity, retention, backup, synchronization, portability, deletion, and legal requirements.
3. Separate secrets from preferences, cache from durable state, derived data from source-of-truth data, and account-specific data from device-wide data.
4. Document paths per platform, package type, portable mode, store sandbox, enterprise redirection, roaming profile, and multiple installed channels.
5. Verify directory and file permissions after fresh install, upgrade, repair, downgrade, account switch, and migration.
6. Prevent one local OS user, app channel, account, tenant, or previous installation from reading another's data unless explicitly designed.
7. Define what survives uninstall, what is removed, what requires user confirmation, and how enterprise-managed data is handled.
8. Test low disk, read-only media, quota, path length, Unicode, case differences, antivirus lock, concurrent access, and abrupt power loss.

### 13.2 Databases, Migrations, Concurrency, And Integrity

1. Identify every embedded or local database engine, exact version, extensions, encryption layer, journal mode, locking model, busy timeout, schema version, and backup method.
2. Review schema constraints, foreign keys, uniqueness, checks, indexes, transaction boundaries, isolation, conflict handling, and recovery.
3. Never rely only on application validation for durable invariants. Add database constraints where supported and compatible.
4. Design migrations for crash safety, idempotency, forward compatibility, rollback or forward repair, disk-space requirements, and old/new application overlap.
5. Back up or snapshot before destructive migrations. Verify backup readability and restore into an isolated environment.
6. Test two windows/processes, background jobs, sidecars, sync engines, and old/new versions accessing the same data where that can occur.
7. Prevent duplicate external side effects around local transactions with idempotency keys, outbox/inbox patterns, durable state machines, or compensating actions.
8. Handle corruption explicitly: detection, read-only safe mode, export, repair limits, restore, telemetry, user communication, and no silent reset.
9. Verify encrypted database key storage, rotation, recovery, account switch, device migration, and behavior when secure storage is unavailable.
10. Test migration interruption at each durable step, downgrade after migration, concurrent startup, lock contention, full disk, and corrupted journal/WAL.

### 13.3 Files, Imports, Exports, Archives, And User Content

1. Treat every imported, opened, dragged, pasted, synchronized, or downloaded file as untrusted regardless of extension.
2. Validate format by parser and content, not extension or MIME alone. Bound size, dimensions, entry count, compression ratio, nesting, parse time, memory, and output.
3. Use robust parsers in a constrained process when possible. Audit native codecs and document libraries for memory-safety and command-execution risk.
4. Prevent path traversal, absolute paths, symlink extraction, hard-link abuse, device files, alternate streams, overwrite, permission inheritance, and archive bombs.
5. Create exports atomically with safe permissions and explicit overwrite behavior. Avoid leaking secrets, hidden columns, deleted records, internal IDs, or unrelated account data.
6. Sanitize filenames for each platform without creating collisions or losing the ability to map back to the source.
7. Mark or quarantine downloaded/generated files where platform expectations require it, and do not auto-open executable or active content.
8. Test malformed, truncated, oversized, polyglot, password-protected, nested, malicious-name, and concurrently modified files.

