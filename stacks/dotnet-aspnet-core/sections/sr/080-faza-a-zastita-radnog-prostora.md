## Faza A - Zastita Radnog Prostora

Pre bilo kakve izmene:

- pronadji root repozitorijuma, branch, status, necommitovane izmene, commit SHA, submodule-e;
- pronadji `.sln`/`.slnx`/`.slnf`, sve `.csproj`/`.fsproj`/`.vbproj`, `global.json`, `Directory.Build.props`/`.targets`, `Directory.Packages.props`, `nuget.config`, lock fajlove;
- pronadji User Secrets ID-jeve bez citanja tajnih vrednosti;
- pronadji certificate/PFX/key/secret fajlove bez prikazivanja sadrzaja;
- proveri da test konfiguracija ne pokazuje ka produkcionim servisima;
- zabelezi pocetno stanje generated fajlova.

Korisne komande:

```text
git status --short --branch
git rev-parse --show-toplevel
git rev-parse HEAD
git submodule status
dotnet --info
dotnet --list-sdks
dotnet --list-runtimes
```

Na Windows-u, kada je relevantno: `Get-Command dotnet`. Ne pretpostavljaj da `dotnet` iz interaktivnog shell-a odgovara SDK-u koji koristi IDE ili CI.

