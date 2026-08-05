## Faza E - Arhitektura I Kriticni Tokovi

Mapiraj: HTTP/gRPC/SignalR ulaze, message consumere, background workere, schedulere, application/use-case sloj, domain, persistence, integration adaptere, cache, evente, security i transaction granice, deployment jedinice.

Za svaki kritican tok: `ulaz -> autentikacija -> validacija -> autorizacija -> use case -> transakcija -> baza/cache/broker/spoljni servis -> odgovor -> telemetry`.

Utvrdi stvarno stanje (monolit / modularni monolit / servisi). Ne preporucuj microservices samo zato sto ima mnogo projekata. Proveri cikluse, domain -> infrastructure zavisnost, shared database izmedju servisa, deployment coupling i nejasno vlasnistvo podataka/dogadjaja.

Controller/Minimal API handler ne sme sadrzati poslovnu logiku, direktno upravljati transakcijama, vracati EF entity ili verovati poljima koja klijent ne sme da odredjuje - osim ako je to eksplicitno i testirano. Ne uvoditi mediator/CQRS/Minimal APIs/Native AOT samo zato sto su popularni.

