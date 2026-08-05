## 1. Aktuelni istraživački baseline - ponovo proveriti pre svakog audita

Ovaj baseline odražava primarne izvore dostupne 5. avgusta 2026. To je samo početna tačka. Pre svake preporuke ili izmene ponovo proveri aktuelna izdanja, periode podrške, Python ABI, dostupnost wheel paketa, Qt platformske zahteve, podršku packaging alata, politike operativnih sistema, bezbednosne advisories i pravila distribucije.

| Oblast | Baseline 5. avgusta 2026. | Obavezna provera tokom audita |
| --- | --- | --- |
| Python stable | Python 3.14.7 je aktuelni stabilni bugfix release 5. avgusta 2026; Python 3.15 je još pre-release. | Tačan interpreter patch, vendor, arhitektura, ABI, build flag-ovi, free-threaded status, JIT status, kompatibilnost ekstenzija i politika podrške. |
| Python režimi izvršavanja | Free-threaded Python je zvanično podržan ali opcion; eksperimentalni JIT binary-ji postoje na nekim platformama i nisu podrazumevana production preporuka. | Da li aplikacija i svaka native zavisnost podržavaju izabrani GIL/free-threaded/JIT režim pod realnom konkurentnošću i u zapakovanom izdanju. |
| PySide6 stable | PySide6 6.11.1 je aktuelni stabilni paket na baseline-u i deklarisano podržava CPython 3.10 do 3.14. | Tačan PySide6, shiboken6, Qt biblioteke, wheel tag-ovi, spakovani plugin-i, licenciranje, packaging podrška i OS deployment zahtevi. |
| Qt for Python | Qt for Python prati Qt 6 release familiju i isporučuje platformski specifične wheel pakete i deployment alate. | Projektom podržana Qt linija, tačan patch, dostupnost modula, deployment platform plugin-a, grafički backend, WebEngine podrška i matrica kompatibilnosti. |
| Pakovanje | PyInstaller, Nuitka, Briefcase, pyside6-deploy, cx_Freeze, installer-i i store-ovi imaju nezavisnu podršku i bezbednosno ponašanje. | Tačne verzije alata i plugin-a, hook-ovi, hidden import-i, native biblioteke, reproduktivnost, redosled potpisivanja, updater model i instalacija na čistoj mašini. |

