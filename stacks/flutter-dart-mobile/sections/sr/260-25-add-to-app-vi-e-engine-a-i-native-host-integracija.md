## 25. Add-to-app, više engine-a i native host integracija

Mešoviti Flutter/native proizvodi zahtevaju eksplicitno vlasništvo i ugovore kompatibilnosti.

- Popiši native host aplikacije, Flutter module, engine group-e, cached engine-e, rute, entrypoint-e, registraciju plugin-a i lifecycle vlasništvo.
- Proveri da native i Flutter navigacija, autentikacija, account/tenant stanje, analitika, accessibility, tema, locale i error semantika ostaju konzistentni.
- Audituj kreiranje/uništavanje engine-a, zadržane engine-e, memoriju, plugin singleton pretpostavke, channel kolizije, više view controller-a/activity-ja i background callback-ove.
- Verzioniši granicu između host-a i modula, uključujući rute, argumente, rezultate, događaje, deljeni storage, tokene i rollout kompatibilnost.
- Proveri build, pakovanje, simbole, potpisivanje, crash reporting i release vlasništvo za kombinovani artefakt.
- Testiraj old host/new module i new host/old module kombinacije gde može doći do nezavisnog rollout-a ili keširanja.
- Obezbedi da native ekrani ne mogu zaobići Flutter-side autorizaciju i da Flutter ekrani ne pretpostavljaju da su native UI provere autoritativne.
- Dokumentuj rollback i emergency disable ponašanje ako Flutter modul ili native host postanu nekompatibilni.

