## Pravilo finalne odluke

- READY zahteva da nema otvorenih P0/P1, da nema kriticne UNVERIFIED celije, da su kriticni artifact/failure testovi uspesni i da su rollout/recovery demonstrirani.
- READY_WITH_CONDITIONS zahteva da nema otvorenog P0, da su P1 ili gap-ovi contained i bounded, da postoje owner-i, rokovi, monitoring, approval i iskrena ogranicenja.
- NOT_READY se primenjuje kada P0/P1 nije resen, evidence nedostaje, release/recovery nije bezbedan ili data/tenant integritet nije izvestan.
- INCIDENT se primenjuje kada se sumnja ili potvrdi aktivna eksploatacija, secret exposure, cross-tenant disclosure, korupcija, kompromitovan artefakt ili nekontrolisan outage.

