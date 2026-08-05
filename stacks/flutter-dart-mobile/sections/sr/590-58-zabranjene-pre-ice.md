## 58. Zabranjene prečice

- Ne rešavaj analyzer ili compiler greške širokim ignore-ima, blanket suppression-ima, nebezbednim cast-ovima, `dynamic`, uklonjenim testovima ili obrisanim kodom osim ako je ponašanje dokazano zastarelo i uklanjanje odobreno.
- Ne nadograđuj masovno Flutter, Dart, pakete, native zavisnosti, minimalne OS verzije, renderer-e, state management, arhitekturu ili platforme da audit deluje moderno.
- Ne proširuj dozvole, entitlement-e, exported komponente, WebView bridge-eve, platform channel-e, filesystem pristup, mrežne izuzetke, CORS, CSP ili tenant scope da funkcija prođe.
- Ne ugrađuj tajne, ne isključuj validaciju sertifikata, ne prihvataj svaki URL, ne veruj notification/deep-link payload-ima, ne preskači proveru potpisa i ne oslanjaj se na obfuscation.
- Ne nazivaj debug, emulator, simulator, one-device, one-browser, unsigned, locally rebuilt ili parcijalno deploy-ovane rezultate production dokazom.
- Ne briši korisničke podatke, cache, migracije, stare šeme, compatibility putanje, simbole, source map-e, stare artefakte ili forenzičke dokaze samo da testovi prođu.
- Ne skrivaj flaky testove retry-jima, ne popuštaj golden pragove široko, ne utišavaj platformska upozorenja i ne isključuj nepodržane ciljeve bez promene tvrdnje o podršci.
- Ne izmišljaj merenja, coverage, device rezultate, store status, potpise, RPO/RTO ili zatvaranje incidenta.
- Ne objavljuj, submit-uj, potpisuj, notarizuj, rotiraj production materijal, šalji stvarne notifikacije ili menjaj live servise bez eksplicitnog ovlašćenja.
- Ne zaustavljaj se na checklist-i. Reprodukuj, proveri, popravi u okviru scope-a, ponovo testiraj, pregledaj artefakte i prijavi preostali rizik.

