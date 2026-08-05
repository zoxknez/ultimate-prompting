## 7. Greske, Timeout, Real-Time I Gasenje

Proveri inbound/header/body limite, database statement timeout, external deadline, job timeout, stream idle timeout, retry budzet i shutdown deadline. Propagiraj cancellation/interrupt signale kako treba; nikada ne gutaj interrupt. Diskonektovan klijent treba da otkaze nepotreban bezbedan rad, a timeout ne sme ostaviti nepracene side effecte.

Koristi stabilnu error taksonomiju: validation, unauthenticated, forbidden, not found, conflict, rate limited, dependency unavailable, timeout i internal failure. Svaka greska zahteva bezbednu poruku, stabilan kod, tacan HTTP/gRPC status, retryability, correlation ID i bezbedne opcione detalje. Sacuvaj uzroke za dijagnostiku bez ponavljanog error logovanja na svakom sloju.

Za WebSocket, SSE i gRPC streaming validiraj konekciju i autorizaciju svake poruke, origin/tenant opseg, reconnect, heartbeat, idle timeout, message/connection limite, backpressure, cleanup, replay/sequence ID-jeve, oporavak propustenih dogadjaja, slow consumere i deployment ponasanje. Autorizacija pocetne konekcije nije dovoljna za svaku poruku/resurs.

Testiraj platform shutdown. Aplikacija treba da postane unready, odbije nov saobracaj, drainuje ili bezbedno otkaze aktivan rad, prestane da preuzima jobove, zatvori streamove, flushuje telemetriju/logove, oslobodi database/cache/broker resurse i zavrsi pre eksplicitnog platform roka. Testiraj gasenje tokom dugih citanja, kriticnih upisa, jobova, uploada, streamova i deploymenta migracije.

