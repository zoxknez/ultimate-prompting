## Obavezni Adversarial I Failure Scenariji

### S1

Dva konkurentna zahteva izvrsavaju istu kriticnu mutaciju.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S2

Klijent ponavlja zahtev nakon database commit-a, ali pre nego sto je odgovor stigao.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S3

Authorization kontekst se menja dok stale stranica, job ili websocket ostaje aktivan.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S4

Tenant identifikator se menja u ruti, nested parametru, GlobalID-u, cache kljucu ili argumentu joba.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S5

Baza postaje spora ili nedostupna dok web i jobovi nastavljaju da primaju rad.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S6

Cache ili Redis backend gubi podatke, evictuje kljuceve ili vraca stale vrednosti.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S7

Worker pada pre, tokom ili posle spoljnog side effect-a.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S8

Isti job se isporucuje dva puta, van redosleda ili nakon brisanja njegovog resursa.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S9

Stari worker obradjuje job koji je enqueue-ovao novi release.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S10

Novi worker obradjuje payload koji je kreirao stari release.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S11

Deployment prekida web, Cable ili job proces sa in-flight radom.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S12

Migracija se delimicno zavrsava, timeout-uje ili se ponavlja.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S13

Direct upload, file parser ili image processor prima zlonameran ili prevelik sadrzaj.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S14

Webhook se replay-uje, reorder-uje, kasni ili je potpisan rotiranim kljucem.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S15

Tajna, cookie kljuc, database credential ili deployment token je kompromitovan.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S16

Sistem dozivljava burst koji saturira thread-ove, pool-ove, redove ili memoriju.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S17

Clock skew ili DST utice na token expiry, periodicni rad ili poslovne datume.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S18

Izolovani restore pocinje sa starim podacima dok spoljni sistemi sadrze novije efekte.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S19

Rollback se desava nakon promene cache-a, job payload-a, encrypted polja ili schema formata.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

### S20

Kompromitovan gem ili base image zahteva opoziv i trusted rebuild.

- Obavezni dokaz: setup, tacni koraci, posmatran rezultat, invarijanta, telemetry, cleanup i preostali rizik.

