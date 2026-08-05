## 6. Lanac identiteta od source-a do runtime-a

Dokaži koji source i zavisnosti su proizveli tačan artefakt koji korisnici izvršavaju.

- Zabeleži URL repozitorijuma, commit, branch ili tag, dirty stanje, submodule-e, Git LFS objekte, patch-eve i generisane fajlove.
- Razreši Flutter SDK kanal, verziju, engine reviziju, Dart verziju, ponašanje package manager-a i platformske toolchain-e u lokalnom i CI okruženju.
- Sačuvaj `pubspec.yaml`, `pubspec.lock`, dependency override-e, workspace konfiguraciju, path/git zavisnosti, platformske implementacije plugin-a i native package lock-ove.
- Prati build-time konfiguraciju, `--dart-define`, environment fajlove, flavor, ciljni entrypoint, opcije generisanja koda, native build podešavanja i signing identitet.
- Zabeleži immutable hash ili ID za proizvedene APK/AAB, IPA/archive, web bundle, MSIX/installer, app bundle, Linux paket, simbole, source map-e i SBOM.
- Proveri package name, bundle identifier, application ID, verziju, build broj, kanal, signing sertifikat, provisioning profile, entitlement-e i publisher identitet.
- Instaliraj ili deploy-uj tačan artefakt i dokaži runtime verziju, flavor, backend okruženje, feature konfiguraciju i učitani native/plugin kod.
- Otkrij rebuild-ove, promenljive artefakte, store reprocessing, environment drift, zastarele generisane fajlove, pogrešne simbole, pogrešne source map-e i pogrešno backend targetiranje.
- Ne prihvataj release ocenu dok source, artifact, signing, installation, runtime, telemetry i recovery identiteti nisu usklađeni ili eksplicitno ostavljeni kao nerešeni.

