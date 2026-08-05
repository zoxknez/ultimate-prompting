## 23. FFI, Native Assets, And Memory Safety

Native code can bypass Dart safety and must be audited as a separate security and reliability domain.

- Inventory `dart:ffi`, native assets, C/C++/Rust libraries, dynamic libraries, symbols, build scripts, download steps, licenses, and architecture variants.
- Verify provenance, hashes, signatures, reproducibility, compiler flags, hardening, ABI, minimum OS, symbol stripping, and debug-symbol retention.
- Audit pointer ownership, allocation/free symmetry, finalizers, lifetimes, callbacks, struct layout, alignment, encoding, integer width, nullability, and error propagation.
- Detect use-after-free, double free, leaks, buffer overflow, out-of-bounds access, race conditions, callback after unload, and blocking native calls.
- Validate all lengths, paths, file formats, network data, and handles before crossing the native boundary.
- Use sanitizers, fuzzing, static analysis, crash-symbolication, and architecture-specific tests where the toolchain allows.
- Verify graceful fallback or explicit unsupported behavior when a native library, symbol, architecture, entitlement, or device capability is unavailable.
- Include native library revocation, emergency replacement, backward compatibility, and rollback in the release plan.

