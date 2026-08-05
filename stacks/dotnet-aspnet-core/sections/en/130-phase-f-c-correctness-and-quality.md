## Phase F - C# Correctness And Quality

Check: Nullable (global/partial), unjustified `!` null-forgiving, deserialization nulls, `required`, model binding, EF materialization, `FirstOrDefault`/`as` casts.

Check records/classes/structs, equality/hashing, mutable fields in hashes, culture-sensitive comparison.

For money: `decimal` vs `double`, scale, rounding, currency; binary floating point is not a money source of truth.

For time: `DateTime`/`DateTimeOffset`/`DateOnly`/`TimeOnly`, UTC vs local, time zones, clock injection, deterministic tests.

For collections and API contracts: mutability, defensive copy, IAsyncEnumerable, serialization compatibility, over-posting.

Do not convert sync methods to async without real asynchronous work. Do not use `Task.Run` as a universal async fix.

