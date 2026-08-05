## 23. FFI, native asset-i i bezbednost memorije

Native kod može zaobići Dart bezbednost i mora biti auditovan kao odvojen bezbednosni i reliability domen.

- Popiši `dart:ffi`, native asset-e, C/C++/Rust biblioteke, dinamičke biblioteke, simbole, build skripte, download korake, licence i architecture varijante.
- Proveri provenance, hash-eve, potpise, reproduktivnost, compiler flag-ove, hardening, ABI, minimalni OS, stripovanje simbola i zadržavanje debug simbola.
- Audituj vlasništvo pointer-a, simetriju allocation/free, finalizer-e, lifetime, callback-ove, struct layout, alignment, encoding, širinu integer-a, nullability i propagaciju grešaka.
- Otkrij use-after-free, double free, leak, buffer overflow, out-of-bounds pristup, race condition, callback posle unload-a i blokirajuće native pozive.
- Validiraj sve dužine, putanje, formate fajlova, mrežne podatke i handle-ove pre prelaska native granice.
- Koristi sanitizer-e, fuzzing, statičku analizu, crash symbolication i architecture-specific testove gde toolchain dozvoljava.
- Proveri graceful fallback ili eksplicitno unsupported ponašanje kada native biblioteka, simbol, arhitektura, entitlement ili device capability nije dostupan.
- Uključi opoziv native biblioteke, hitnu zamenu, backward kompatibilnost i rollback u release plan.

