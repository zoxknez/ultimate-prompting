## 22. Platform channel-i, Pigeon i native granica

Tretiraj svaki Dart/native bridge kao IPC i authorization granicu.

- Popiši MethodChannel, EventChannel, BasicMessageChannel, Pigeon API-je, FFI, callback-ove, codec-e, nazive channel-a, handler-e i platformske implementacije.
- Proveri šemu, tip, nullability, opseg, enum, putanju, URI, origin, vlasništvo resursa i poslovnu autorizaciju na obe strane svakog poziva.
- Audituj redosled poziva, reentrancy, konkurentne pozive, duple callback-ove, timeout, cancellation, ponovno kreiranje procesa, engine detach i kasnu isporuku rezultata.
- Ne izlaži generičke file, shell, URL, reflection, database, keychain, clipboard, intent, process ili device operacije bez uskih allowlist-a i provere resursa.
- Proveri da greške čuvaju dovoljno dijagnostike bez curenja tajni, putanja, tokena, native stack podataka ili internih identifikatora korisniku.
- Verzioniši channel ugovore i testiraj stare/nove Dart i native kombinacije tokom rolling aplikacionih ili add-to-app upgrade-a.
- Pregledaj thread zahteve, blokiranje main thread-a, dispatch queue, coroutine/task vlasništvo, vlasništvo memorije i callback lifetime u native kodu.
- Zahtevaj negative, malformed-input, authorization, concurrency, detach/reattach, process-death i platform-version testove.

