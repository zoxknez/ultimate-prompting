## Phase J - Transaction Boundaries And Atomicity

Reconstruct each critical transaction from application entry to durable commit.

- List reads, writes, constraints, locks, remote calls, messages, files, cache and user waits inside each transaction.
- Verify auto-commit, implicit commit, nested transaction and savepoint behavior.
- Verify ORM unit-of-work boundaries match business atomicity and actual connection ownership.
- Do not hold database locks during slow remote calls or human interaction without an explicit design.
- Define commit uncertainty behavior after timeout, network loss or process crash.
- Use outbox, inbox, saga or reconciliation when atomicity spans database and external systems.

