## 40. Faza 30 - WordPress Incident Acceptance Kriterijumi

Najjača dostupna odluka ograničena je pregledanim scope-om i kvalitetom dokaza.

### READY kriterijumi

Svi primenljivi uslovi moraju biti tačni:

- dokumentovani su authorization, scope i vlasnici odluka
- dokazi su sačuvani sa hash-evima i chain-of-custody zapisom
- aktivna zloupotreba je contained
- pregledani su WordPress bootstrap, izvršivi kod, database, identiteti, scheduler-i, host i edge persistence
- source i provenance su utvrđeni za svaku zadržanu izvršivu komponentu
- initial access je otklonjen ili je nerešena putanja eksplicitno prihvaćena uz kompenzujuće kontrole
- kredencijali, session-i, application password-i i relevantni eksterni ključevi su rotirani ili opozvani
- čist rebuild ili verifikovani restore su završeni
- kritični poslovni tokovi i security assertion-i prolaze
- cache, OPcache, CDN i worker-i serviraju nameravani release
- dokazani su backup restore, rollback/forward-repair i monitoring
- nema otvorenog P0 ili P1 nalaza

### Uslovni ili blokirani ishodi

Koristi:

- `CONDITIONALLY SAFE - ACCEPTED RESIDUAL RISK` samo kada vlasnik eksplicitno prihvati dokumentovan preostali rizik koji nije P0/P1
- `NOT PRODUCTION-SAFE` kada ostanu aktivna kompromitacija, persistence, nepoznat privileged pristup, nepoverljiv kod, neuspešan recovery ili otvoren P0/P1
- `INSUFFICIENT EVIDENCE` kada kritični scope ili dokaz nisu dostupni

Nikada ne pretvaraj nedostatak dokaza u prolazan rezultat.

