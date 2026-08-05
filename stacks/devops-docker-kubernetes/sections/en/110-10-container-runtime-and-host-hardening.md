## 10. Container Runtime And Host Hardening

**Objective:** Reduce runtime privilege and host escape blast radius.

### 10.1 Required Checks

1. Verify engine, containerd, runc, kernel, cgroups, storage driver, seccomp, AppArmor or SELinux, user namespaces, rootless mode, and support status.
2. Reject privileged mode, host PID, host IPC, host network, Docker socket mounts, broad device access, and arbitrary hostPath unless specifically justified and isolated.
3. Drop all capabilities and add only proven requirements. Enforce no-new-privileges, read-only root filesystem, bounded writable volumes, and controlled proc and sys access.
4. Set CPU, memory, PID, file-descriptor, ephemeral-storage, log, and process limits based on measured behavior and failure semantics.
5. Verify daemon API exposure, authorization plugins, socket ownership, TLS, remote access, auditability, and separation from untrusted users.
6. Test graceful stop, forced termination, restart policy, log rotation, disk pressure, OOM, and corrupted writable-state behavior.

### 10.2 Minimum Evidence

- Runtime security configuration and effective process privileges.
- Host exposure and mount inventory with justification.
- Controlled termination, pressure, and restart test results.

### 10.3 Exit Criteria

1. No unjustified privileged path or host-control socket is reachable.
2. Limits and restart behavior fail safely under measured pressure.
3. Runtime and host components are supported, patched through a defined process, and observable.

