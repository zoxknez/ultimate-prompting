## Phase D - Ruby Runtime And Implementation

### CRuby / MRI

- Verify exact patch, configure flags, YJIT support, allocator, OpenSSL, libc, architecture and container base.
- Model the Global VM Lock correctly: it does not make application state, database writes, native extensions or multi-process behavior race-free.
- Inspect native gems and C extensions for ABI, compiler, libc, OpenSSL and architecture compatibility.
- Benchmark YJIT on production-like workloads and account for memory, warmup, code GC and deployment model.

### JRuby And TruffleRuby

- Verify JVM or GraalVM version, flags, garbage collector, native integration, gem support and container limits.
- Re-evaluate thread safety because JRuby can execute Ruby threads in parallel.
- Test database adapters, native gems, signal handling, process forking assumptions and server compatibility.
- Do not claim portability until the exact runtime and all process roles pass the same critical-flow suite.

