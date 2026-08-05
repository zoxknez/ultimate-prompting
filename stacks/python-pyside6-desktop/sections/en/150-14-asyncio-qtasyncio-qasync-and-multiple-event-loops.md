## 14. Asyncio, QtAsyncio, Qasync, And Multiple Event Loops

### 14.1 Audit Scope

1. Identify asyncio usage, QtAsyncio or qasync integration, loop policy, task groups, executors, async generators, network clients, and library-owned loops.
2. Document which loop owns each coroutine, how Qt and asyncio callbacks interleave, and where thread or process handoff occurs.
3. Review task creation, structured concurrency, cancellation propagation, timeout composition, shielded tasks, exception groups, and task retention.
4. Detect nested `asyncio.run`, loop creation in worker threads, blocking code on the loop, unobserved tasks, cross-loop futures, and shutdown warnings.
5. Assess compatibility of libraries that assume the main thread, a specific event-loop implementation, or Unix-only signal behavior.
6. Define offline, reconnect, retry, backpressure, application-close, logout, and update-restart behavior for asynchronous work.

### 14.2 Required Verification

1. Instrument task creation, completion, cancellation, exceptions, queue depth, loop lag, and shutdown across representative flows.
2. Test delayed and reordered responses, disconnect during await, cancellation during write, window destruction, account switch, and application exit.
3. Ensure cancellation reaches sockets, streams, files, database operations, child processes, and business workflows or is explicitly compensated.
4. Verify one clear integration strategy rather than accidental coexistence of independent GUI and asyncio loops.
5. Fail readiness when critical background tasks can become orphaned, silently fail, update stale UI, or prevent clean shutdown.

