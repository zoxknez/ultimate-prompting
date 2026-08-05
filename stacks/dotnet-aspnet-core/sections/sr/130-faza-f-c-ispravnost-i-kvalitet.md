## Faza F - C# Ispravnost I Kvalitet

Proveri: Nullable (globalno/parcijalno), `!` null-forgiving bez dokaza, deserialization null, `required`, model binding, EF materialization, `FirstOrDefault`/`as` cast.

Proveri records/classes/structs, equality/hashing, mutable polja u hash-u, culture-sensitive poredjenje.

Za novac: `decimal` naspram `double`, scale, rounding, currency; binarni floating point nije izvor istine za novac.

Za vreme: `DateTime`/`DateTimeOffset`/`DateOnly`/`TimeOnly`, UTC vs lokalno, time zone, clock injection, deterministicki testovi.

Za kolekcije i API ugovore: mutability, defensive copy, IAsyncEnumerable, serialization kompatibilnost, over-posting.

Ne pretvaraj sync metode u async bez stvarnog asinhronog rada. Ne koristi `Task.Run` kao univerzalnu async popravku.

