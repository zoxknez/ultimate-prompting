## 12. Ispravnost Dart jezika i runtime-a

Pregledaj jezičku semantiku i runtime ponašanje koje može poništiti poslovnu logiku.

- Audituj null safety, nebezbedne cast-ove, `dynamic`, late inicijalizaciju, non-null assertion-e, covariance, generic constraints, kolizije extension-a i exhaustiveness.
- Pregledaj equality, hashCode, identity, immutable modele, copy semantiku, mutaciju kolekcija, redosled, deduplikaciju i ispravnost cache key-eva.
- Proveri integer, double, decimal-money, datum/vreme, vremensku zonu, locale, Unicode, normalizaciju, regex, parsiranje, zaokruživanje, overflow i precision ponašanje.
- Pregledaj taksonomiju exception-a, `Error` naspram `Exception`, zone ponašanje, neuhvaćene async greške, očuvanje stack-a, retry, cancellation i bezbedno mapiranje za korisnika.
- Audituj JSON, protobuf, GraphQL, binary, XML, platform-channel, database i cache serializaciju radi verzionisanja, nepoznatih polja, default vrednosti, malformiranog ulaza i backward kompatibilnosti.
- Traži skriveno globalno stanje, statičke singleton-e, promenljive service locator-e, zavisnost od redosleda testova, environment leakage i isolate-unsafe pretpostavke.
- Proveri tree-shaking i release-mode razlike za assertion-e, reflection-like generisanje koda, runtime type name-ove, stack trace-ove i conditional import-e.
- Zahtevaj testove na granicama, nevalidnim ulazima, minimum/maximum vrednostima, malformiranim payload-ima, promenama sata, locale promenama i starim sačuvanim podacima.

