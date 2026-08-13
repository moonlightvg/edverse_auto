"""API-класс для сервиса films (фильмы)."""
from api.requester import CustomRequester


class MoviesAPI(CustomRequester):
    """Работа с фильмами (сервис api.dev-edversemovie.ru)."""

    MOVIES = "/movies"

    def __init__(self, session, base_url):
        super().__init__(session=session, base_url=base_url)

    def get_movies(self, expected_status=200):
        """Список всех фильмов."""
        return self.send_request(
            "GET", self.MOVIES, expected_status=expected_status,
        )
