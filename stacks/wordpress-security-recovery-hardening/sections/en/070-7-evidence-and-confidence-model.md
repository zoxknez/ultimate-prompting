## 7. Evidence And Confidence Model

### Evidence status

Use exactly one:

- `CONFIRMED` - directly supported by collected evidence.
- `LIKELY` - multiple consistent indicators, but no definitive proof.
- `POSSIBLE` - plausible and partially supported.
- `UNVERIFIED` - not tested or insufficient evidence.
- `REFUTED` - evidence contradicts the hypothesis.

### Evidence quality

Rate each important item:

- `E1` - direct artifact, trusted log, verified hash or reproducible observation.
- `E2` - strong corroborating evidence from two or more independent sources.
- `E3` - single indirect indicator or incomplete artifact.
- `E4` - unsupported report, assumption or anecdote.

### Chain-of-custody record

```text
Evidence ID:
Collected at (ISO-8601 and timezone):
Collected by:
Source host/account:
Original path/object ID:
Collection method/command:
Original size:
SHA-256:
Ownership and permissions:
Original timestamps:
Storage location:
Access history:
Notes and redactions:
```

Use UTC plus the local timezone when timestamps from multiple systems are involved. Identify clock drift where possible.

