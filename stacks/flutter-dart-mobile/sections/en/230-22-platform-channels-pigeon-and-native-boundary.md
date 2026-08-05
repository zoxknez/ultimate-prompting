## 22. Platform Channels, Pigeon, And Native Boundary

Treat every Dart/native bridge as an IPC and authorization boundary.

- Inventory MethodChannel, EventChannel, BasicMessageChannel, Pigeon APIs, FFI, callbacks, codecs, channel names, handlers, and platform implementations.
- Verify schema, type, nullability, range, enum, path, URI, origin, resource ownership, and business authorization on both sides of every call.
- Audit call ordering, reentrancy, concurrent calls, duplicate callbacks, timeout, cancellation, process recreation, engine detach, and late result delivery.
- Do not expose generic file, shell, URL, reflection, database, keychain, clipboard, intent, process, or device operations without narrow allowlists and resource checks.
- Verify errors preserve enough diagnostics without leaking secrets, paths, tokens, native stack data, or internal identifiers to users.
- Version channel contracts and test old/new Dart and native combinations during rolling application or add-to-app upgrades.
- Review thread requirements, main-thread blocking, dispatch queues, coroutine/task ownership, memory ownership, and callback lifetime in native code.
- Require negative, malformed-input, authorization, concurrency, detach/reattach, process-death, and platform-version tests.

