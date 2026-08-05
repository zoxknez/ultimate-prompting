## 9. Expo Module, native modul, JSI i native memorija

### 9.1 Autorizacija i validacija native API-ja
- Popisi svaki metod, property, event, view, funkciju, konstantu, callback, promise i sinhroni poziv izlozen JavaScript-u.
- Validiraj oblik, velicinu, opseg, putanju, URL, identifikator, dozvolu, tenant, ownership i lifecycle stanje na native granici.
- Ne veruj JavaScript proverama za privilegovane native operacije, filesystem pristup, kontrolu uredjaja, kredencijale, placanja ili korisnicke podatke.
- Eksplicitno definisi main-thread, module-queue, background-thread, coroutine, dispatcher i actor zahteve.
- Navedi cancellation, timeout, dupli poziv, reentrancy, stale callback, serializaciju greske i shutdown ponasanje.
- Testiraj direktne pozive sa malformed i adversarial vrednostima cak i kada bi ih normalan JavaScript wrapper odbio.

### 9.2 JSI, C++, JNI, Objective-C++ i ABI
- Popisi raw pointer, host object, shared ownership, weak ownership, global reference, JNI reference, block, closure i finalizer.
- Dokazi zivotni vek objekta kroz JavaScript garbage collection, React instance reload, unistenje surface-a, rekreiranje activity-ja, background aplikacije i gasenje procesa.
- Proveri thread affinity, sinhronizaciju, memory ordering, validnost callback-a, prevod exception-a i cross-language unwind ponasanje.
- Auditiraj duzinu buffer-a, offset, encoding, alignment, konverziju integer-a, transfer ownership-a, allocator pairing i use-after-free rizik.
- Proveri svaku native biblioteku po podrzanom ABI-ju, minimalnom OS-u, 16 KB page-size kompatibilnosti gde je primenljivo, vidljivosti simbola i pakovanju.
- Koristi sanitizer, native crash, symbolication, stress, repeated reload i lifecycle testove gde je izvodljivo.

