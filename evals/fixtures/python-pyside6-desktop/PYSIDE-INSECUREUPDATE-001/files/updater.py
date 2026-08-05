import subprocess
import urllib.request


def check_and_install_update(update_url: str, install_path: str) -> None:
    """Download the latest build and run it to install the update.

    Vulnerable: the update package is fetched over plain HTTP and executed
    with no signature or checksum verification. Anyone in a position to
    intercept or redirect this request - a hostile Wi-Fi network, a
    compromised router, a DNS spoof - can serve an attacker-controlled
    binary that this function then runs with the current user's privileges.
    """
    urllib.request.urlretrieve(update_url, install_path)
    subprocess.run([install_path], check=True)
