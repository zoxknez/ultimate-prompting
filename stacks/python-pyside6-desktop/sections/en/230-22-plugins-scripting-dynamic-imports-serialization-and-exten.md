## 22. Plugins, Scripting, Dynamic Imports, Serialization, And Extension Points

### 22.1 Audit Scope

1. Inventory Python plugin systems, entry points, dynamic imports, user scripts, macros, templates, QML modules, native plugins, codecs, and third-party extensions.
2. Document discovery paths, trust source, signature or hash verification, compatibility contract, permissions, API surface, process isolation, update, disable, and removal.
3. Review `pickle`, `marshal`, `shelve`, unsafe YAML, object hooks, dynamic class loading, `eval`, `exec`, template execution, and expression engines.
4. Assess plugin access to filesystem, network, credentials, UI, clipboard, devices, database, updater, and privileged helpers.
5. Detect import shadowing, writable plugin paths, namespace collisions, dependency conflicts, ABI mismatch, crash propagation, and startup denial of service.
6. Define behavior for incompatible, corrupted, malicious, revoked, slow, crashing, or abandoned plugins.

### 22.2 Required Verification

1. Attempt plugin loading from user-writable, current-directory, removable-media, network-share, and tampered package locations.
2. Feed untrusted serialized objects, templates, expressions, scripts, and configuration; confirm strict formats and safe failure.
3. Test plugin timeout, crash, infinite loop, excessive memory, dependency conflict, API mismatch, update, revocation, and disable/recovery.
4. Use process isolation or a deliberately constrained capability model for untrusted extension code; document residual risk when true sandboxing is unavailable.
5. Reject arbitrary-code extension features presented as safe without explicit trust, distribution, permission, and incident controls.

