"""Фасад: один объект даёт доступ ко всем API-ресурсам."""
from api.auth_api import AuthAPI
from api.movies_api import MoviesAPI


class ApiManager:
    """Одна точка входа для всех API."""

    def __init__(self, session, auth_url, api_url):
        self.session = session
        self.auth = AuthAPI(session, auth_url)
        self.movies = MoviesAPI(session, api_url)

    def close(self):
        """Закрыть сессию после всех тестов."""
        self.session.close()
