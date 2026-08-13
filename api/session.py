"""Сессия с транспортными ретраями (только сетевые сбои, не HTTP-статусы)."""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def session_with_retries() -> requests.Session:
    """Сессия, которая переживает ConnectionError и таймауты."""
    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=1,
        allowed_methods=["GET", "DELETE", "PUT", "HEAD", "OPTIONS"],
        # status_forcelist НЕ задаём: статусными ретраями занимается реквестер
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session
