## Ozbiljnost

| Prioritet | Definicija |
| --- | --- |
| P0 | Neautorizovan ili medju-tenant pristup, RCE/injekcija, otkrivena produkciona tajna, nepovratan gubitak/korupcija podataka, duplo placanje, destruktivan deployment ili neproveren oporavak kriticnih podataka. |
| P1 | Zaobilazenje autorizacije u kriticnom toku, race/transakciona greska, losa idempotentnost, nedostajuci kriticni timeout, neograniceni resursi, nebezbedna deserijalizacija, dupliran worker ili prekid kriticne operacije pri deploymentu. |
| P2 | Lokalizovan API/UI problem, spor upit, slaba observabilnost, nedosledan error ugovor, izbegljiv rizik dostupnosti ili tehnicki dug sa konkretnom posledicom. |
| P3 | Ciscenje, dokumentacija, imenovanje, doslednost ili malo izmereno poboljsanje. |

Severity zasnuj na uticaju i verovatnoci, ne na estetskoj preferenciji.

