"""Единая обёртка над requests: URL, логи, ретраи, проверка статуса."""
import time

import requests


class CustomRequester:
    """Транспортный слой: собирает URL, шлёт запрос, ретраит 502/503/504."""

    base_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    def __init__(self, session: requests.Session, base_url: str):
        self.session = session
        self.base_url = base_url
        self.headers = self.base_headers.copy()

    def send_request(self, method, endpoint, data=None,
                     expected_status=200, headers=None):
        """Слать запрос. При 502/503/504 - ретраит идемпотентные методы."""
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        request_headers = {**self.headers, **(headers or {})}

        response = self.session.request(
            method, url, json=data, headers=request_headers,
        )

        # 502/503/504 - стенд "моргнул": для GET/DELETE/PUT безопасно повторить
        retryable = {"GET", "DELETE", "PUT", "HEAD", "OPTIONS"}
        transient = {502, 503, 504}
        attempt = 1
        while (method in retryable
               and response.status_code in transient
               and attempt < 5):
            time.sleep(2 ** attempt)
            response = self.session.request(
                method, url, json=data, headers=request_headers,
            )
            attempt += 1

        assert response.status_code == expected_status, (
            f"Ожидали {expected_status}, получили {response.status_code}: "
            f"{response.text[:200]}"
        )
        return response
