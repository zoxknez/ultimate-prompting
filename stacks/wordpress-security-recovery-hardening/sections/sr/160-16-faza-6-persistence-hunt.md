## 16. Faza 6 - Persistence Hunt

Tretiraj persistence kao poseban workstream. Proveri:

- MU pluginove i WordPress drop-in fajlove
- `wp-config.php` include putanje i konstante
- `auto_prepend_file` i `auto_append_file`
- `.user.ini`, `php.ini`, PHP-FPM pool konfiguraciju i vhost konfiguraciju
- `.htaccess` i Nginx/LiteSpeed include fajlove
- WordPress scheduled events
- system/user cron i systemd timer-e
- startup skripte i shell profile fajlove
- SSH `authorized_keys`
- hosting panel korisnike i API tokene
- database korisnike, grants, triggers i events
- rogue WordPress administratore i application passwords
- zlonamerne options, transients, widgets i serijalizovane payload-e
- Redis/object-cache persistence i stale cache
- CDN workers, transform pravila, redirect-e i edge funkcije
- DNS/registrar pristup
- CI/CD deploy ključeve, tajne i kompromitovane build artefakte
- izmenjene backup ili migration pakete koji mogu ponovo uneti malware

Oporavljen sajt sa neproverenom persistence putanjom nije production-safe.

