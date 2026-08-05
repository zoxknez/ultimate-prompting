## SQLite Path

### Loaded Library, Compile Options, And Filesystem

- Verify `sqlite_version()`, `sqlite_source_id()` and `PRAGMA compile_options` from the actual application process.
- Identify system library, bundled amalgamation, static link, dynamic link, language binding and extension loading.
- Verify page size, reserved bytes, encoding, auto-vacuum, maximum limits and compatibility with existing files.
- Review local filesystem locking guarantees; do not place a writable SQLite database on unsupported network or sync storage.
- Protect database, `-wal`, `-shm`, journal, backup and temporary files with correct ownership and permissions.

### Transactions, WAL, Locking, And Concurrency

- Verify journal mode, synchronous level, locking mode, busy timeout and connection-per-thread behavior.
- Test deferred, immediate and exclusive transaction behavior under concurrent readers and writers.
- Measure WAL growth, checkpoint behavior, long readers, write starvation and crash recovery.
- Use bounded retry for `SQLITE_BUSY` or `SQLITE_LOCKED`; never hide indefinite contention.
- Test process crash, power loss, disk full, read-only storage and two-instance application behavior.

### SQLite Schema, Integrity, Migration, And Backup

- Verify `foreign_keys` on every connection, `trusted_schema`, defensive settings and STRICT table use where appropriate.
- Review affinity, dynamic typing, numeric conversion, collation and generated-column behavior.
- Use `PRAGMA integrity_check` or `quick_check` with understood cost and limitations; add application invariants.
- Test table-rebuild migrations with triggers, indexes, foreign keys, data volume, crash and rollback.
- Use the online Backup API, `VACUUM INTO` or another supported coordinated method; do not blindly copy only the main file in WAL mode.
- Restore into isolation, verify source ID and compile options, run integrity checks and execute application smoke tests.

