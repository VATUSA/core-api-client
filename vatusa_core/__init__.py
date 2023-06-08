import logging

from vatusa_core.config import APIConfig
from vatusa_core import transfer


def set_token(token: str):
    APIConfig.token = token


def set_url(url: str):
    if url.endswith('/'):
        raise Exception("Malformed URL - Must NOT end with /")
    APIConfig.url = url


def set_log_level(level):
    log = logging.getLogger('vatusa_core')
    log.setLevel(level)
