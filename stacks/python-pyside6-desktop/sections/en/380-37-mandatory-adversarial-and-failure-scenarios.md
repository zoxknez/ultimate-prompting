## 37. Mandatory Adversarial And Failure Scenarios

### 37.1 S1 - Rapid repeated UI action starts duplicate non-idempotent work.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.2 S2 - Window, model, or account changes before a delayed worker result returns.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.3 S3 - QObject receiver is destroyed while signals, timers, network replies, or callbacks remain queued.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.4 S4 - GUI thread is blocked, reentered, or updated directly from a worker.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.5 S5 - Worker, asyncio task, subprocess, or helper crashes during a critical operation.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.6 S6 - Application closes, logs out, changes workspace, sleeps, or updates during in-flight work.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.7 S7 - Disk becomes full, read-only, locked, slow, or unavailable during write, migration, download, or update.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.8 S8 - Two application instances or stale locks modify the same local state.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.9 S9 - Network becomes slow, offline, redirected, proxied, certificate-rotated, or partially responsive.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.10 S10 - Authentication expires concurrently and refresh, logout, revocation, or account switching races.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.11 S11 - Unauthorized deep link, IPC, WebChannel, plugin, local file, or modified local state attempts a privileged action.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.12 S12 - Malformed, oversized, recursive, polyglot, or path-traversing file reaches an import or preview path.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.13 S13 - Writable current directory, PATH, plugin path, temp path, or user directory attempts module, DLL, helper, or resource hijacking.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.14 S14 - Queue, thread pool, event loop, memory, handles, disk, or GPU becomes saturated under burst and soak load.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.15 S15 - Native extension, Qt plugin, codec, driver, or graphics backend is missing, incompatible, or crashes.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.16 S16 - Installer or updater is interrupted, tampered, out of disk, blocked by antivirus, or cannot replace running files.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.17 S17 - Old and new binaries, helpers, plugins, schemas, or server APIs overlap during staged rollout and rollback.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.18 S18 - Signing certificate or update key expires, rotates, is revoked, or is suspected compromised.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.19 S19 - Backup restore occurs on a clean machine with missing keyring, changed paths, different user, or newer operating system.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.20 S20 - Malicious dependency, plugin, helper, package, or build runner requires containment and trusted rebuild.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

