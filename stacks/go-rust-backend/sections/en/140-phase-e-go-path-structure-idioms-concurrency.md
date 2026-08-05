## Phase E - GO PATH: Structure, Idioms, Concurrency

### Packages and errors

Check: package cohesion, `internal`, public API, import direction, global state, `init`, side-effect imports, interface ownership. Interfaces usually belong on the consumer side when that matches real architecture; do not introduce interfaces only for mocking.

Errors: ignored error, wrapping with `%w`, `errors.Is`/`As`, sentinel/typed error, string comparison, log-and-return same error, leaking internals, overly broad panic, recover hiding corruption. Do not use panic as normal business control flow. Do not add recover on every layer.

Nil: nil interface with non-nil dynamic type, nil map/slice/channel, typed nil error, nil receiver.

Slice/map: backing-array aliasing, retaining large backing arrays, concurrent map access, append invalidation, map iteration nondeterminism, defensive copy, pool reuse exposing stale data.

### Goroutine, channel, context

Check:

- who starts the goroutine, who owns its lifecycle, how it ends;
- `context.Context` propagation, timeout/deadline/cancel, derived contexts;
- channels: buffered/unbuffered, close ownership, send on closed channel, nil channel deadlock, unbounded growth;
- `errgroup`, worker pool, semaphore, bounded concurrency;
- select with default that swallows backpressure;
- leaks: goroutine waiting on channel/mutex/IO that never completes;
- panic in a non-main goroutine.

Use `go test -race` where applicable. The race detector is not a substitute for design review, but it confirms real data races.

Do not add a goroutine merely so a function looks non-blocking. Do not use unbounded channels without memory analysis. Do not share a map without synchronization.

