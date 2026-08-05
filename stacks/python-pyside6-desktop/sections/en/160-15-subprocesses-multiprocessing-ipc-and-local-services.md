## 15. Subprocesses, Multiprocessing, IPC, And Local Services

### 15.1 Audit Scope

1. Inventory subprocesses, `multiprocessing`, helper executables, local agents, services, named pipes, Unix sockets, loopback HTTP, shared memory, and file-based IPC.
2. Record executable resolution, arguments, environment, working directory, privileges, ownership, authentication, framing, versioning, timeout, and shutdown.
3. Review shell usage, quoting, command injection, PATH hijacking, current-directory search, inherited handles, environment leakage, and writable executable locations.
4. Assess multiprocessing start methods, frozen-application bootstrap, recursive spawn, resource tracker behavior, shared-state consistency, and crash recovery.
5. Treat localhost and same-user IPC as attacker-reachable unless authentication, authorization, permissions, and peer identity are proven.
6. Define compatibility for old/new GUI, helper, service, protocol, schema, and update versions.

### 15.2 Required Verification

1. Launch from installed paths and adversarial working directories to prove trusted executable and library resolution.
2. Test malformed, oversized, reordered, replayed, unauthenticated, cross-user, stale-version, and partial IPC messages.
3. Force helper crash, GUI crash, timeout, pipe break, duplicate request, upgrade overlap, and shutdown during critical work.
4. Verify privilege separation, least-privilege service accounts, OS ACLs, peer credentials, request authorization, and signed/versioned helpers.
5. Confirm no orphan process, shared-memory segment, lock file, port listener, temporary secret, or half-applied side effect remains after failure.

