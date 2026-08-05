## 16. Qt Widgets, modeli, view-ovi, delegate-i i veliki podaci

### 16.1 Obim audita

1. Inventariši prozore, dialoge, stacked stranice, dock widget-e, action-e, shortcut-e, forme, tabele, stabla, liste, proxy modele, delegate-e i custom painting.
2. Pregledaj vlasništvo layout-a, duplo dodeljivanje layout-a, parentovanje widget-a, focus chain, tab redosled, modalnost, persistence geometrije i multi-monitor ponašanje.
3. Za svaki model verifikuj validnost index-a, parent/child odnose, row i column notifikacije, persistent index-e, reset semantiku, sortiranje, filtriranje i thread vlasništvo.
4. Proceni lazy loading, pagination, virtualizaciju, fetch-more ponašanje, cache slika/ikona, veliki tekst, drag/drop, clipboard i undo/redo.
5. Pregledaj delegate editor-e, validaciju, redosled commit/close, stale index-e, selection stanje i konkurentne izmene modela.
6. Razlikuj prezentaciono formatiranje od domain vrednosti, dozvola, validacije, persistence-a i poslovnih invarijanti.

### 16.2 Obavezna verifikacija

1. Vežbaj prazne, male, velike, malformed, brzo promenljive, filtrirane, sortirane, reordered i konkurentno osvežene skupove podataka.
2. Koristi model tester-e, assertion-e, fokusirane unit testove i UI automatizaciju za validaciju redosleda notifikacija i bezbednosti index-a.
3. Izmeri scroll, resize, selekciju, editovanje, filtriranje, painting i memoriju na realnim maksimalnim veličinama podataka.
4. Testiraj keyboard-only navigaciju, screen reader nazive/stanja, high DPI, skaliranje teksta, proširenje prevoda i right-to-left layout-e.
5. Obezbedi da se izmene modela marshal-uju na GUI thread i da stale asinhroni rezultati ne mogu mutirati zamenjen model ili selekciju.

