## 8. Python Runtime, ABI, GIL, Free-Threaded Mode, And JIT

### 8.1 Audit Scope

1. Record exact CPython version, vendor, build flags, architecture, debug/release status, ABI tag, `SOABI`, Unicode configuration, OpenSSL, and platform runtime.
2. Identify whether the build uses the traditional GIL, free-threaded mode, experimental JIT, debug allocator, sanitizers, or custom interpreter patches.
3. Map every C/C++/Rust extension, limited-API/abi3 wheel, ctypes/cffi binding, Shiboken wrapper, and native library to supported Python and platform ABIs.
4. Review reference ownership, finalizers, weak references, cyclic GC, shutdown order, exception hooks, import hooks, and signal handling.
5. Assess subinterpreters, embedded Python, isolated mode, virtual environments, zip imports, frozen modules, and user-site behavior if applicable.
6. Distinguish language-level thread safety from extension-level, Qt-level, database-level, file-level, and business-level concurrency safety.

### 8.2 Required Verification

1. Run the packaged application under the exact supported interpreter mode and exercise native extensions, shutdown, exceptions, and concurrency.
2. For free-threaded mode, require explicit compatibility evidence for PySide6, every native dependency, global state, callbacks, reference lifetimes, and third-party libraries.
3. For JIT or non-default builds, compare correctness, startup, memory, diagnostics, packaging, crash behavior, and rollback against the supported baseline.
4. Use debug builds, faulthandler, tracemalloc, sanitizers, or platform debuggers where appropriate to investigate native crashes and lifetime defects.
5. Reject an interpreter upgrade when required wheels, Qt bindings, packaging tools, native libraries, or operating-system targets are unsupported.

