## Zabranjeno Ponasanje

Nemoj:

- izmisljati output komandi, fajlove, klase, endpointe, migracije, CVE ili test rezultate;
- tvrditi da testovi prolaze ako nisu izvrseni; sakriti neuspesan test; skip-ovati test da bi pipeline prosao;
- iskljucivati analyzere bez analize; dodavati `!` samo da uklonis nullable warning;
- koristiti `catch (Exception) { }`; `Task.Run` kao univerzalnu async popravku; pretvarati sync I/O u lazni async;
- koristiti isti DbContext paralelno; registrovati scoped kao singleton da bi DI greska nestala;
- iskljucivati authorization ili antiforgery; wildcard CORS sa credentialima; verovati svakom forwarded headeru;
- logovati tajne; retry-ovati non-idempotent side effect bez zastite;
- dodavati in-memory lock kao zastitu izmedju vise replika;
- automatski pokretati destruktivne migracije; koristiti EF InMemory kao dokaz relational ispravnosti;
- prebacivati sve upite na `AsNoTracking`; dodavati Include svuda radi skrivanja lazy-loading problema;
- ukljucivati cache bez invalidacione strategije; povecavati pool/thread limite bez capacity analize;
- prelaziti na Native AOT/Minimal APIs/MediatR/CQRS/microservices samo zbog popularnosti;
- koristiti preview .NET/C# u productionu bez eksplicitnog odobrenja;
- brisati korisnicke necommitovane izmene; formatirati ceo solution da sakrijes relevantan diff;
- proglasiti projekat "savrsenim" ili production-ready bez dokaza.

