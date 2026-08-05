## 11. Qt application lifecycle, QObject vlasništvo i destrukcija

### 11.1 Obim audita

1. Mapiraj kreiranje `QApplication` ili `QGuiApplication`, singleton inicijalizaciju, startup faze, splash, konstrukciju zavisnosti, ulazak u event loop, shutdown i restart.
2. Za svaki kritični QObject zabeleži kreatora, parent-a, vlasnika Python reference, thread affinity, potrošače, trigger destrukcije, `deleteLater` ponašanje i shutdown redosled.
3. Identifikuj neusaglašeno vlasništvo između Python garbage collection-a i Qt parent-child brisanja, dangling wrapper-e, oživljene reference i use-after-delete rizike.
4. Pregledaj top-level prozore, dialoge, tray ikone, timer-e, network objekte, thread-ove, modele, delegate-e, action-e i native resurse radi determinističkog cleanup-a.
5. Pregledaj promene application stanja, session restore, suspend/resume, logout, promenu korisnika i OS termination putanje.
6. Razlikuj normalno zatvaranje, hide-to-tray, forced termination, crash, update restart, installer shutdown i OS logout semantiku.

### 11.2 Obavezna verifikacija

1. Instrumentuj kreiranje, affinity, signal konekcije, destrukciju, finalizaciju i shutdown za reprezentativne kritične objekte.
2. Testiraj ponovljeno open/close, login/logout, promenu workspace-a, rekreiranje prozora, tray restore, update restart i izlazak aplikacije radi leak-ova i stale callback-ova.
3. Koristi weak reference-e, `QPointer`, destroyed signale, debug assertion-e i platformske alate gde je prikladno da dokažeš lifetime pretpostavke.
4. Verifikuj da shutdown zaustavlja novi rad, otkazuje ili drenira postojeći rad, flush-uje kritične podatke, oslobađa lock-ove i uređaje i izlazi u definisanom roku.
5. Odbaci popravke koje samo globalno održavaju objekte živim ili pozivaju garbage collection bez ispravljanja vlasništva.

