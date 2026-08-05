## 14. State management i reaktivna konzistentnost

Audituj stvarni state machine bez obzira da li projekat koristi Provider, Riverpod, Bloc, Cubit, Redux, MobX, Signals, GetX, ValueNotifier, custom controller-e ili mešovite pristupe.

- Popiši source of truth, derived stanje, prolazno UI stanje, persistirano stanje, server stanje, cache stanje, navigation stanje i platformsko stanje.
- Proveri redosled događaja, potiskivanje zastarelih rezultata, spajanje duplih zahteva, rollback optimističkog update-a, paginaciju, refresh, retry i promenu naloga.
- Testiraj istovremene korisničke akcije, ponovljene tap-ove, promenu rute tokom zahteva, background/foreground tranzicije, reconnect, logout i promenu tenant-a.
- Proveri provider/bloc/controller scope, disposal, auto-dispose, keep-alive, restoration, nested override-e, test override-e i cross-route vlasništvo.
- Otkrij nekonzistentne loading/error/empty/success modele, skrivene zastarele podatke, parcijalne greške, beskonačne refresh petlje, duple listener-e i notification storm-ove.
- Obezbedi čišćenje osetljivog stanja pri logout-u, uklanjanju naloga, promeni tenant-a, resetu aplikacije, odgovoru na kompromitovan uređaj i isteku retention-a.
- Izmeri granularnost rebuild-a i ponašanje selector-a; optimizuj tek kada profiling potvrdi nepotreban rad.
- Zahtevaj determinističke testove state tranzicija za kritične tokove, uključujući nevalidne, prekinute, duplirane, promenjenog redosleda i replay-ovane događaje.

