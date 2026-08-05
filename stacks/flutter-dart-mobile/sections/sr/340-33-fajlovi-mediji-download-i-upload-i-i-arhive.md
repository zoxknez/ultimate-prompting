## 33. Fajlovi, mediji, download-i, upload-i i arhive

Tretiraj svaki eksterni fajl kao nepoverljiv i svaku lokalnu putanju kao platform-specific.

- Popiši document picker-e, kameru/galeriju, drag/drop, share intent-e, clipboard, import, export, arhive, media decode, thumbnail-e, download-e, upload-e i privremene fajlove.
- Validiraj tip iz sadržaja gde je moguće, veličinu, dimenzije, trajanje, broj, encoding, filename, ekstenziju, putanju, strukturu arhive i parser limite.
- Spreči path traversal, symlink/reparse zloupotrebu, zip slip, decompression bomb, overwrite, izvršni sadržaj, zlonamerne metapodatke, parser crash i nebezbedno spoljašnje otvaranje.
- Koristi scoped ili user-selected storage pravilno; proveri platformske bookmark/dozvole, opoziv, sandbox putanje, removable media, cloud fajlove i file-provider semantiku.
- Definiši upload i download resume, integrity hash, content length, parcijalni fajl, cancellation, retry, kvotu, duplikat, overwrite, cleanup i low-disk ponašanje.
- Ne izlaži privatne lokalne putanje, signed URL-ove, tokene, tenant identifikatore, EXIF/GPS podatke ili korisnički sadržaj u logovima i analitici.
- Testiraj malformirane, prekinute, ogromne, enkriptovane, nested, preimenovane, zero-byte, duplirane, nepodržane i slow-stream fajlove.
- Proveri cleanup posle uspeha, greške, cancellation-a, process death-a, logout-a, brisanja naloga, app update-a i uninstall-a prema politici.

