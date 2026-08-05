## Tehnološki Overlay-i I Konačna Produkciona Odluka

### Obavezan Izbor Overlay-a

- Primeni Servlet MVC overlay kada sistem koristi Tomcat, Jetty, WAR deployment, blocking controller-e, servlet filter-e ili tradicionalnu JDBC request obradu.
- Primeni WebFlux/Reactor overlay kada sistem koristi Netty, reactive controller-e, reactive klijente, R2DBC, streaming ili mešane imperative/reactive tokove.
- Primeni messaging/worker overlay kada ispravnost zavisi od listener-a, consumer-a, scheduler-a, Spring Batch-a, Quartz-a, integration flow-ova ili dugotrajnih job-ova.
- Primeni library/starter overlay kada se objavljuje reusable auto-konfiguracija, BOM, annotation, procesor, plugin ili API koji koriste nepoznate aplikacije.
- Primeni native-image overlay kad god GraalVM, AOT, CDS, CRaC ili startup-optimized packaging menja runtime ponašanje ili recovery pretpostavke.

### Evidence-Driven Tok Popravke

- Kreiraj finding pre materijalne popravke sa severity-jem, nivoom dokaza, pogođenom invarijantom, exploit ili failure putanjom, scope-om, root cause-om, owner-om i acceptance testom.
- Preferiraj najmanju arhitektonsku popravku koja vraća prekršeni ugovor bez skrivanja simptoma, slabljenja bezbednosti ili stvaranja tihog fallback ponašanja.
- Posle svake popravke pokreni prvo fokusirane testove, zatim pogođene integration i migration testove, pa security, concurrency, performance, packaging i rollback regresije proporcionalne riziku.
- Zabeleži komande, izlaze, artifact identitet, okruženje, before/after dokaze, preostalu neizvesnost i svaki odloženi rad sa owner-om i rokom.
- Ne zatvaraj finding zato što je kod promenjen; zatvori ga tek kada je failure putanja opovrgnuta ili kontrolisana ponovljivim dokazom.

### Pravilo Produkcione Odluke

- Vrati `NOT READY` kada bilo koji nerazrešeni P0 ili P1 finding, netestirana kritična invarijanta, neproverena tenant granica, nekontrolisana migracija, nepoznat artifact identitet ili nedokazan restore blokira bezbedan release.
- Vrati `CONDITIONALLY READY` samo kada su preostali rizici eksplicitno ograničeni, imaju owner-a, rok, monitoring, mogućnost povratka i prihvatanje odgovarajućeg autoriteta.
- Vrati `READY` samo kada su kritične evidence matrice kompletne, obavezni failure scenariji prolaze, release i rollback su uvežbani, restore je dokazan i runtime identitet korelisan.
- Navedi odvojeno poverenje za source ispravnost, build integritet, runtime bezbednost, integritet podataka, operativnu otpornost, bezbednost migracije i recovery spremnost.
- Nikada ne zameni nedostajući dokaz jezikom samopouzdanja, prestižom alata, framework default-ima, scanner skorom, brojem testova ili zelenim pipeline-om.

