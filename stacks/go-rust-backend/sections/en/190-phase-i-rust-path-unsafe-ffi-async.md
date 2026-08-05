## Phase I - RUST PATH: Unsafe, FFI, Async

### Unsafe inventory

Find: `unsafe` block/fn/trait/impl, raw pointers, transmute, MaybeUninit, ManuallyDrop, unions, unchecked indexing/UTF-8, custom allocators, FFI, SIMD, inline asm, `static mut`.

Table: `Location | Unsafe operation | Safety invariant | Who upholds it | Test/check | Risk`.

For public `unsafe fn` require `# Safety` documentation: preconditions, lifetime, alignment, aliasing, initialization, ownership, thread safety, drop, FFI/ABI. A `// SAFETY:` comment must explain a concrete invariant, not merely say “this is safe”.

### FFI

Check: ABI, `repr(C)`, layout/alignment, string encoding, null, ownership/allocator pairing, callbacks, unwinding across FFI, bindgen, build.rs, platform target. Do not allow unwind across FFI unless explicitly supported.

### Miri and sanitizers

When supported:

```text
cargo +nightly miri test
```

Pin nightly. Miri is not proof of absence of all UB, especially on unexecuted paths, platform code, and unsupported FFI. Document Address/Leak/Memory/ThreadSanitizer requirements and limits.

### Async runtime and task lifecycle

First determine the runtime (Tokio, async-std, smol, Embassy, custom, multiple runtimes, or none). Do not apply Tokio rules to another runtime without checking.

Check: multi-thread/current-thread, worker threads, blocking pool, task spawn ownership, cancellation/`Drop` of futures, `JoinHandle` await, `select!` cancel safety, bounded channels/backpressure, `spawn_blocking` for blocking work, timeout, graceful shutdown. Uncontrolled `tokio::spawn` without supervision risks leaks and orphan tasks.

