## 17. Apple platform production audit

### 17.1 iOS i iPadOS build
- Razresi Xcode, Swift, deployment target, arhitekture, CocoaPods, Swift package, framework, build setting, linker flag i legacy pretpostavke povezane sa bitcode-om.
- Pregledaj Info.plist, entitlement-e, privacy manifest, required-reason API-je, associated domain, background mode, URL type, app group i keychain grupu.
- Proveri bundle identifier, verziju, build broj, scheme, konfiguraciju, signing identitet, provisioning profile, capabilities i export options.
- Pregledaj archive, IPA, dSYM, BCSymbolMap gde je relevantan, embedded framework, extension, resurse, privacy fajlove, potpise i debug artefakte.
- Proveri svaki bundlovani third-party SDK po potpisu, privacy manifest-u, arhitekturi, minimalnom OS-u, licenci, symbolication-u i store uskladjenosti.
- Instaliraj kroz stvarni TestFlight, App Store, enterprise ili ad hoc put i testiraj upgrade, fresh install, restore, migraciju i uninstall.

### 17.2 Apple runtime i uredjaji
- Testiraj scene lifecycle, background suspenziju, termination, state restoration, memory warning, protected data, zakljucavanje uredjaja i low-power mode.
- Testiraj iPhone i iPad layout, Stage Manager, split view, rotaciju, Dynamic Type, safe area, tastaturu, pointer, external display i podrzane klase uredjaja.
- Proveri universal link, custom scheme, authentication session, handoff, push akcije, widget, extension i app clip gde postoje.
- Auditiraj Keychain accessibility, biometric policy, data protection, app group, background URL session i file coordination.
- Testiraj promenu dozvole, ogranicen photo pristup, pribliznu lokaciju, Bluetooth, lokalnu mrezu, tracking autorizaciju i managed-device ogranicenja.
- Sacuvaj watchdog termination, jetsam, native crash, hang, memoriju, energiju, launch, animaciju, networking i symbolication dokaz iz release build-a.

