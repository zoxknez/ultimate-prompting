## 41. Release Gate-ovi

Production se ne smatra oporavljenim dok svi primenljivi gate-ovi ne prođu.

### Gate 1 - Dokazi

- ključni dokazi su sačuvani i hash-ovani
- chain-of-custody je zabeležen
- ograničenja vremenske linije su dokumentovana

### Gate 2 - Scope

- procenjeni su WordPress, host, database, identity, edge i susedni sajtovi
- nepoznate/nepregledane oblasti su izričito navedene

### Gate 3 - Eradication

- poznati zlonamerni artefakti su uklonjeni ili izolovani van production-a
- persistence putanje su proverene i popravljene
- initial-access vektor je zatvoren ili je preostali rizik formalno prihvaćen

### Gate 4 - Identitet

- pogođeni kredencijali su rotirani
- sesije/tokeni su invalidirani
- nepoznati nalozi i ključevi su uklonjeni

### Gate 5 - Recovery

- pouzdan kod i content su vraćeni
- funkcionalni smoke testovi prolaze
- rollback putanja je potvrđena

### Gate 6 - Hardening

- kritične/visoke hardening stavke su završene
- backup i restore test su potvrđeni
- monitoring je uključen

### Gate 7 - Izveštavanje

- evidence-backed izveštaj je kompletan
- procenjene su notification i pravne obaveze
- vlasnik prihvata preostali rizik

Ako neki obavezni gate ne prolazi, navedi tačno:

`Sajt nije potpuno oporavljen niti production-safe. Neispunjeni gate-ovi: [LISTA].`

