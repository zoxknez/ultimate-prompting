## Faza D - Ruby Runtime I Implementacija

### CRuby / MRI

- Proveri tacan patch, configure flag-ove, YJIT podrsku, allocator, OpenSSL, libc, arhitekturu i container bazu.
- Pravilno modeluj Global VM Lock: on ne cini application state, database upise, native extension-e ili multi-process ponasanje bez race-a.
- Pregledaj native gemove i C extension-e za ABI, compiler, libc, OpenSSL i arhitekturnu kompatibilnost.
- Benchmarkuj YJIT na production-like workload-u i uzmi u obzir memoriju, warmup, code GC i deployment model.

### JRuby I TruffleRuby

- Proveri JVM ili GraalVM verziju, flag-ove, garbage collector, native integraciju, gem podrsku i container limite.
- Ponovo proceni thread safety jer JRuby moze paralelno izvrsavati Ruby thread-ove.
- Testiraj database adapter-e, native gemove, signal handling, pretpostavke o forking-u procesa i server kompatibilnost.
- Ne tvrdi prenosivost dok tacan runtime i sve uloge procesa ne prodju isti critical-flow test suite.

