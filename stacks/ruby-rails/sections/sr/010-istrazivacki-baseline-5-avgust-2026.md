## Istrazivacki Baseline - 5. avgust 2026.

Ovaj baseline je polazna tacka, a ne dozvola za slepu nadogradnju. Neposredno pre preporuka ili izmena ponovo proveri zvanicne Ruby, Rails, RubyGems, Bundler, Puma i projektne izvore.

| Komponenta | Potvrdjeno stanje 5. avgusta 2026. | Obavezna audit provera |
| --- | --- | --- |
| Ruby CRuby | 4.0.6 je najnoviji stabilni patch u liniji 4.0; 3.4 je u normalnom odrzavanju, 3.3 u security odrzavanju, a 3.2 je EOL. | Proveri `ruby -v`, `RUBY_ENGINE`, patch, build, platformu, image i proces. |
| Rails | 8.1.3.1 je najnovije security izdanje u aktuelnoj liniji 8.1. | Proveri `Gemfile.lock`, stvarno ucitane gem verzije, period podrske i security advisories. |
| Rails politika podrske | Bugfix podrska je generalno godinu dana, a security podrska dve godine od pocetka minor linije. | Izracunaj datume iz stvarnog izdanja linije i ponovo proveri politiku. |
| Bundler | 4.0.17 je aktuelno stabilno izdanje. | Proveri Bundler, RubyGems, format lock fajla, platforme, checksum-e i deployment rezim. |
| Puma | 8.0.2 je aktuelno izdanje; podrzane aplikacije mogu namerno ostati na drugoj odrzavanoj liniji. | Proveri Rack kompatibilnost, server konfiguraciju, parser/proxy ponasanje, workere, thread-ove i graceful restart. |
| Solid Queue | Rails 8 koristi Solid Queue kao podrazumevani production Active Job backend; aktuelna gem linija mora se proveriti iz lock fajla. | Ne prenosi Sidekiq semantiku na Solid Queue. Proveri bazu, dispatcher, worker, scheduler i concurrency ponasanje. |
| Ruby modeli izvrsavanja | CRuby, JRuby i TruffleRuby imaju razlicita concurrency, GC, native extension i deployment svojstva. | Nikad ne generalizuj GVL ili native gem pretpostavke izmedju runtime-a. |

Ne mesaj source deklaracije, lokalni development, CI, image build, web proces, job proces, konzolu, scheduler i one-off task stanje. Svako je posebna granica dokaza.

