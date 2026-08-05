## 9. Expo Modules, Native Modules, JSI, And Native Memory

### 9.1 Native API Authorization And Validation
- Inventory every method, property, event, view, function, constant, callback, promise, and synchronous call exposed to JavaScript.
- Validate shape, size, range, path, URL, identifier, permission, tenant, ownership, and lifecycle state at the native boundary.
- Do not trust JavaScript-side checks for privileged native operations, filesystem access, device control, credentials, payments, or user data.
- Define main-thread, module-queue, background-thread, coroutine, dispatcher, and actor requirements explicitly.
- Specify cancellation, timeout, duplicate call, reentrancy, stale callback, error serialization, and shutdown behavior.
- Test direct calls with malformed and adversarial values even when normal JavaScript wrappers would reject them.

### 9.2 JSI, C++, JNI, Objective-C++, And ABI
- Inventory raw pointers, host objects, shared ownership, weak ownership, global references, JNI references, blocks, closures, and finalizers.
- Prove object lifetime across JavaScript garbage collection, React instance reload, surface destruction, activity recreation, app backgrounding, and process shutdown.
- Verify thread affinity, synchronization, memory ordering, callback validity, exception translation, and cross-language unwind behavior.
- Audit buffer length, offset, encoding, alignment, integer conversion, ownership transfer, allocator pairing, and use-after-free risk.
- Verify every native library for supported ABI, minimum OS, 16 KB page-size compatibility where applicable, symbol visibility, and packaging.
- Use sanitizer, native crash, symbolication, stress, repeated reload, and lifecycle tests where feasible.

