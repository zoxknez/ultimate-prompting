## Definition Of Done

- [ ] Sve aktivne runtime, server, job, database i deployment putanje su identifikovane.
- [ ] Odluke o verzijama i podrsci zasnovane su na aktuelnim zvanicnim izvorima i stvarnom lock/runtime dokazu.
- [ ] Svaki P0 i P1 je popravljen, mitigovan sa eksplicitnim prihvatanjem ili blokira release.
- [ ] Kriticne poslovne invarijante imaju application, database, concurrency i reconciliation dokaz.
- [ ] Autorizacija i tenant izolacija imaju negativne testove kroz HTTP, jobove, cache, fajlove i realtime.
- [ ] Release artefakti, migracije, jobovi i process shutdown su provereni u production-like uslovima.
- [ ] Performance i capacity tvrdnje su izmerene ili eksplicitno oznacene kao neproverene.
- [ ] Rollback ili forward repair i izolovani restore su izvrsivi, a ne samo dokumentovani.
- [ ] Command logovi, evidence linkovi, izmenjeni fajlovi, testovi, deployment uticaj i preostali rizik su ukljuceni.
- [ ] Zavrsna presuda je `READY`, `READY_WITH_CONDITIONS`, `NOT_READY` ili `INCIDENT`, sa blokatorima i vlasnicima.

Ako bilo koja obavezna stavka nedostaje, navedi: **Ruby on Rails sistem nije potpuno production-ready u auditovanom scope-u.**

