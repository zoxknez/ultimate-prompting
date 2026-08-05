## 52. Incident response i trusted rebuild

Sačuvaj dokaze i vrati poverenje pre optimizacije normalne isporuke.

- Definiši trigger-e za aktivnu kompromitaciju, curenje kredencijala, kompromitovan signing ključ, zlonamernu zavisnost, kompromitovan update kanal, izlaganje podataka, crash loop, destruktivnu migraciju i široki outage.
- Sačuvaj stanje repozitorijuma, CI logove, dependency resolution, generisani izlaz, build artefakte, potpise, store metapodatke, update metapodatke, telemetriju, backend logove, device dokaze i timeline.
- Ograniči incident najužim bezbednim kontrolama: opozovi kredencijale, onemogući flag/rute, zaustavi rollout, ukloni zlonamerne artefakte, blokiraj verzije, izoluj servise i zaštiti korisničke podatke.
- Proceni domet client verzije, kašnjenje store propagacije, offline uređaje, stare installer-e, keširane web asset-e, background job-ove, tokene i persistirano zlonamerno stanje.
- Opozovi i rotiraj pogođene tajne, sertifikate, ključeve, tokene, signing identitete, update ključeve, push kredencijale i vendor pristup uz dependency-aware redosled.
- Ponovo build-uj iz proverenog commit-a u čistom trusted okruženju sa ponovo razrešenim zavisnostima, pregledanim generisanim kodom, novim provenance-om, novim potpisima i poređenjem artefakata.
- Validiraj eradication, backward kompatibilnost, korisničku remedijaciju, forced update ili minimum-version politiku, oporavak offline klijenata i detekciju ponavljanja.
- Dokumentuj odluke, odobrenja, komunikaciju, pravne/privacy obaveze, store/vendor koordinaciju, preostali rizik i vlasništvo follow-up-a.
- Ne uništavaj dokaze, ne čisti kompromitovane sisteme pre capture-a, ne objavljuj neproverljive popravke i ne proglašavaj zatvaranje bez trusted-build i operativnog dokaza.

