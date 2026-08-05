## Faza Z - Active Storage, Upload-i I Obrada Fajlova

- Popisi storage servise, public ili private pristup, direct upload, proxy ili redirect serving, mirror-e i lifecycle policy-je.
- Autorizuj svaki blob, attachment, variant, preview, download, purge i signed URL na granici poslovnog resursa.
- Validiraj tip iz sadrzaja, a ne samo extension-a ili client metadata-e; primeni size, dimension, page, duration i decompression limite.
- Sandboxuj ili izoluj image, PDF, office, video i archive obradu i drzi native procesore patchovanim.
- Testiraj zlonamerna imena fajlova, path traversal, polyglot-e, zip slip, decompression bomb-e, parser crash, timeout-e i cleanup.
- Proveri da cleanup orphan i unattached upload-a ne brise podatke koje jos referencira drugi tenant, transakcija ili delayed job.

