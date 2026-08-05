## Phase 2 - PHP Binary, SAPI, Extensions, INI, And Process Identity

### Objective

Prove which PHP build and configuration each process actually uses.

### Audit Requirements

- Record exact PHP version, build date, architecture, thread-safety mode, compiler, debug flags, Zend Engine, and relevant build options.
- Compare CLI, FPM, Apache module, queue worker, scheduler, migration job, test runner, and container runtime binaries.
- Compare loaded INI files, scan directories, extension sets, timezone, locale, memory, execution, upload, session, OPcache, JIT, realpath, and error settings.
- Inventory PDO drivers, Redis or Memcached clients, intl, mbstring, sodium, OpenSSL, curl, XML, image, zip, pcntl, posix, sockets, and FFI dependencies.
- Verify OS packages, CA trust, ICU, timezone database, graphics libraries, and native client libraries used by extensions.
- Confirm runtime identity from the deployed process or a safe diagnostic endpoint, not only from local `php -v`.

### Required Evidence

- Per-process PHP identity matrix with binary path, SAPI, version, patch, extensions, INI, image digest, and owner.
- Diff of CLI, web, worker, scheduler, migration, and test runtime settings.
- Support and upgrade decision tied to official lifecycle and provider support.

### Acceptance Criteria

- All critical processes use an explicitly supported and patched runtime or have a contained migration plan.
- No decision relies on an unproven assumption that all PHP SAPIs share the same binary or configuration.

