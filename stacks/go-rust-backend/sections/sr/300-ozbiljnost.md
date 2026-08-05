## Ozbiljnost

| Prioritet | Definicija |
| --- | --- |
| P0 | Neautorizovan/cross-tenant pristup, RCE/injekcija, potvrdjen data race u kriticnom toku, unsound unsafe/FFI sa realnim UB rizikom, otkrivena produkciona tajna, nepovratan gubitak/korupcija podataka, destruktivan deployment, neproveren recovery kriticnih podataka. |
| P1 | Authz bypass u kriticnom toku, goroutine/task leak pod opterecenjem, broken cancellation/timeout, broken idempotency/transakcija, neograniceni resursi, nebezbedna deserijalizacija, supply-chain sa reachability, prekid kriticne operacije pri deploy-u. |
| P2 | Lokalizovan API problem, spor upit, slaba observabilnost, nedosledan error ugovor, izbegljiv availability rizik, tehnicki dug sa konkretnom posledicom. |
| P3 | Ciscenje, dokumentacija, imenovanje, doslednost, malo izmereno poboljsanje. |

