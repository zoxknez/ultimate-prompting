## Faza I - RUST STAZA: Unsafe, FFI, Async

### Unsafe inventar

Pronadji: `unsafe` blok/fn/trait/impl, raw pointer, transmute, MaybeUninit, ManuallyDrop, union, unchecked indexing/UTF-8, custom allocator, FFI, SIMD, inline asm, `static mut`.

Tabela: `Lokacija | Unsafe operacija | Safety invariant | Ko ga obezbedjuje | Test/provera | Rizik`.

Za javni `unsafe fn` zahtevaj `# Safety` dokumentaciju: preuslovi, lifetime, alignment, aliasing, initialization, ownership, thread safety, drop, FFI/ABI. Komentar `// SAFETY:` mora objasniti konkretan invariant, ne samo "ovo je bezbedno".

### FFI

Proveri: ABI, `repr(C)`, layout/alignment, string encoding, null, ownership/allocator par, callback, unwinding preko FFI, bindgen, build.rs, platform target. Ne dozvoli unwind preko FFI granice osim kada je eksplicitno podrzano.

### Miri i sanitizeri

Kada podrzano:

```text
cargo +nightly miri test
```

Pinuj nightly. Miri nije dokaz odsustva svih UB, narocito u neizvrsenim putanjama, platformskom kodu i nepodrzanom FFI-ju. Dokumentuj Address/Leak/Memory/ThreadSanitizer zahteve i ogranicenja.

### Async runtime i task lifecycle

Prvo utvrdi runtime (Tokio, async-std, smol, Embassy, custom, vise runtime-ova, ili bez). Ne primenjuj Tokio pravila na drugi runtime bez provere.

Proveri: multi-thread/current-thread, worker threads, blocking pool, task spawn ownership, cancellation/`Drop` future, `JoinHandle` await, `select!` cancel safety, bounded channels/backpressure, `spawn_blocking` za blocking rad, timeout, graceful shutdown. Nekontrolisan `tokio::spawn` bez nadzora je rizik za leak i orphan taskove.

