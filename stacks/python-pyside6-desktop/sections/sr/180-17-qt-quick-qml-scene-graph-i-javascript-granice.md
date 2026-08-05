## 17. Qt Quick, QML, scene graph i JavaScript granice

### 17.1 Obim audita

1. Inventariši QML module, engine-e, context-e, singleton-e, registrovane Python tipove, image provider-e, JavaScript, shader-e, animacije, loader-e i remote/local poreklo resursa.
2. Pregledaj QML ownership režime, lifetime context property-ja, binding loop-ove, signal handler-e, dinamičko kreiranje objekata, destrukciju loader-a i teardown engine-a.
3. Proceni Python objekte izložene QML-u, invokable metode, property-je, signale, input validaciju, autorizaciju, thread affinity i propagation izuzetaka.
4. Pregledaj interakcije scene-graph render thread-a, custom QQuickItem kod, grafičke resurse, dekodiranje slika, shader-e i razlike platformskih backend-a.
5. Pregledaj JavaScript `eval`, dinamički import, network-loaded QML, pristup lokalnim fajlovima, URL handling i nepoverljive podatke koji stižu do executable izraza.
6. Izmeri binding churn, overdraw, texture memoriju, trošak animacija, frame pacing, startup kompilaciju i QML cache ponašanje.

### 17.2 Obavezna verifikacija

1. Tretiraj QML upozorenja kao pad testa za kritične tokove i pregledaj zapakovane import putanje, plugin-e, cache i ponašanje missing module-a.
2. Testiraj rekreiranje engine-a, logout, promene teme/locale-a, dinamičko učitavanje stranice, destrukciju objekata, reset grafičkog uređaja i shutdown aplikacije.
3. Fuzz-uj ili validiraj svaku Python-QML granicu sa malformed, oversized, stale, unauthorized i cross-tenant podacima gde je primenljivo.
4. Profiliraj render i GUI thread na svakom podržanom grafičkom backend-u i realnom low-end hardveru.
5. Obezbedi da remote ili user-controlled sadržaj ne može učitati QML, JavaScript, plugin-e, shader-e ili lokalne resurse izvan eksplicitne trust politike.

