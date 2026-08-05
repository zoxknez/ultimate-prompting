## Faza E - GO STAZA: Struktura, Idiomi, Concurrency

### Paketi i greske

Proveri: package cohesion, `internal`, public API, import direction, global state, `init`, side-effect import, interface ownership. Interface obicno na strani potrosaca kada to odgovara; ne uvoditi interface samo radi mockovanja.

Greske: ignorisan error, wrapping `%w`, `errors.Is`/`As`, sentinel/typed error, poredjenje poruke, log+return iste greske, leaking internih detalja, presirok panic, recover koji skriva corruption. Ne koristi panic kao normalan poslovni tok. Ne dodaj recover na svaki sloj.

Nil: nil interface sa non-nil dynamic type, nil map/slice/channel, typed nil error, nil receiver.

Slice/map: aliasing backing array, zadrzavanje velikog backing array-a, concurrent map access, append invalidacija, map iteration nondeterminism, defensive copy, pool reuse koji izlaze stare podatke.

### Goroutine, channel, context

Proveri:

- ko pokrece goroutine, ko je vlasnik lifecycle-a, kako se zavrsava;
- `context.Context` propagaciju, timeout/deadline/cancel, derived context;
- channel: buffered/unbuffered, close ownership, send na zatvoren channel, nil channel deadlock, unbounded growth;
- `errgroup`, worker pool, semaphore, bounded concurrency;
- select sa default koji guta backpressure;
- leak: goroutine ceka na channel/mutex/IO koji nikad ne zavrsava;
- panic u goroutine van main-a.

Koristi `go test -race` gde je primenljivo. Race detector nije zamena za design review, ali potvrdjuje stvarne data race-ove.

Ne dodaj goroutine samo da funkcija izgleda neblokirajuce. Ne koristi unbounded channel bez memory analize. Ne deli mapu bez sinhronizacije.

