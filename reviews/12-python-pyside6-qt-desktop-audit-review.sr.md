# Revizija 12 - Python / PySide6 / Qt desktop audit prompt

Datum: 2026-08-05

## Početno stanje

- Engleska verzija je imala 156 linija, dok je srpska imala 129 linija.
- EN/SR par je imao različit broj i raspored naslova i predstavljao je poslednji poznati strukturni paritet problem u biblioteci.
- Prompt je pokrivao osnovne Qt teme, ali nije imao formalni source-to-installed-runtime lanac, evidence nivoe, package/installer/update dokaz, recovery ugovor ili sistematske platforme i failure matrice.
- Python interpreter, ABI, GIL/free-threaded/JIT režim, Shiboken/native ekstenzije i stvarno zapakovani Qt runtime nisu bili dovoljno precizno razdvojeni.

## Glavne izmene

- Obe jezičke verzije rekonstruisane su iz jednog sinhronizovanog generatora i podignute na verziju 2.0.0.
- Uvedeni su E0-E5 nivoi dokaza, P0-P3 severity, obavezni finding zapis i četiri readiness zaključka.
- Dodat je kompletan identitet od repozitorijuma, interpretera i dependency grafa do generisanog koda, native biblioteka, paketa, installer-a, potpisa, instaliranih fajlova i pokrenutog procesa.
- Detaljno su obrađeni CPython ABI, tradicionalni GIL, free-threaded režim, eksperimentalni JIT, native ekstenzije, ctypes/cffi i Shiboken granice.
- Dodati su QObject parent/Python-reference lifetime, `deleteLater`, signal/slot connection tipovi, reentrancy, nested event loop, QThread, QThreadPool, cancellation, lock order, asyncio/QtAsyncio/qasync i shutdown ugovori.
- Prošireni su Qt Widgets, model/view/delegate, QML/scene graph, Qt WebEngine/WebChannel, mreža, lokalni IPC, multiprocessing, helper-i, uređaji, plugin-i, dynamic import i unsafe serialization audit.
- Dodate su odvojene Windows, macOS i Linux matrice za native biblioteke, installer, signing/notarization, dozvole, high DPI, accessibility, update i rollback.
- Uvedeni su data migration, offline sync, corruption recovery, backup/restore, RPO/RTO, immutable artifact promotion, incident containment i trusted rebuild zahtevi.
- Dodato je 12 evidence matrica, 20 obaveznih adversarial/failure scenarija, production readiness checklist, Definition of Done, forbidden shortcuts i strogi final report.

## Aktuelizovani baseline

- Python 3.14.7 je stabilni maintenance release od 5. avgusta 2026; Python 3.15 je još pre-release.
- Free-threaded Python je zvanično podržan u 3.14, ali ostaje poseban compatibility i concurrency režim koji mora biti dokazan za PySide6 i svaku native zavisnost.
- Zvanični Windows i macOS Python 3.14 binary-ji uključuju eksperimentalni JIT, koji nije automatski production izbor.
- PySide6 6.11.1 je aktuelni stabilni paket na baseline-u i deklarisano podržava Python 3.10 do 3.14.
- Qt for Python, PySide6, Shiboken6, Essentials/Addons, Qt biblioteke, platform plugin-i i deployment alati moraju se proveravati kao stvarni resolved i packaged skup, ne samo kroz jednu verziju u manifestu.

## Rezultat

- EN: 1.051 linija i 151 naslov.
- SR: 1.051 linija i 151 naslov.
- Heading paritet: prošao.
- Line-shape paritet: 0 odstupanja.
- YAML frontmatter: validan.
- JSON baseline manifest: validan.
- Markdown code fence struktura: validna.
- Nedozvoljeni en dash, em dash i non-breaking hyphen znakovi u SR promptu: 0.
- Repository-level parity checker sada prolazi za svih 15 neversionovanih EN/SR parova koje proverava.

## Preostali repository-level rad

- Semantic EN/SR parity još nema automatski eval harness.
- Markdown lint, link checking i fixture repozitorijumi ostaju zajednički bibliotečki zadaci.
- Sledeći paket po redosledu je React Native / Expo.
