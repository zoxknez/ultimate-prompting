<!-- section:CORE-SEVERITY-MODEL -->
# Jezgro — Model Ozbiljnosti (P0–P3)

| Prioritet | Značenje |
| --------- | -------- |
| **P0** | Neovlašćeni pristup / pristup između zakupaca, RCE/injekcija, izložene produkcione tajne, ireverzibilan gubitak/korupcija podataka, destruktivno neuvežbano puštanje, neoporavljiv jaz bekapa za kritične podatke |
| **P1** | Zaobilaženje autorizacije u kritičnom toku, greška u trci/transakciji/idempotenciji, neograničeni resursi, dupliranje radnika, prekid puštanja kritičnih operacija, nebezbedna migracija pod opterećenjem |
| **P2** | Lokalizovan funkcionalni/UX problem, izmeren problem performansi, slaba opservabilnost, izbežan rizik dostupnosti, tehnički dug sa konkretnom posledicom |
| **P3** | Dokumentacija, imenovanje, konzistentnost, mala izmerena čišćenja |

Ozbiljnost je uticaj × verovatnoća, a ne estetika.
