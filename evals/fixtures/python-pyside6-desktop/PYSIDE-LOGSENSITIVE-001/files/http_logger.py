import logging

logger = logging.getLogger("api")
logging.basicConfig(filename="debug.log", level=logging.DEBUG)


def log_request(method: str, url: str, headers: dict, body: str) -> None:
    """Debug helper wired into every outgoing API call for troubleshooting.

    Vulnerable: the full request is logged verbatim, including the
    Authorization header (a bearer token or API key) and the raw body
    (which can contain the user's password on a login call). debug.log is
    created with the process's default file permissions in the user's home
    directory - readable by any other local account on a shared machine,
    and commonly attached whole to support tickets or bug reports without
    anyone noticing the embedded credentials.
    """
    logger.debug("%s %s\nHeaders: %s\nBody: %s", method, url, headers, body)
