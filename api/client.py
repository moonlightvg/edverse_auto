"""API-клиент проекта (урок 1: Requests).

Юзеры и логин живут на auth, фильмы - на api. Поэтому два базовых URL.
"""
import requests

AUTH_URL = "https://auth.dev-edversemovie.ru"
API_URL = "https://api.dev-edversemovie.ru"


class ApiClient:
    def create_user(self, email: str, password: str, full_name: str) -> dict:
        """Регистрация пользователя (эндпоинт /register, без токена)."""
        response = requests.post(
            f"{AUTH_URL}/register",
            json={
                "email": email,
                "fullName": full_name,
                "password": password,
                "passwordRepeat": password,
            },
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    def delete_user(self, user_id: str, token: str) -> None:
        """Удаляет пользователя. Нужен токен: удалить можно только себя."""
        requests.delete(
            f"{AUTH_URL}/user/{user_id}",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10,
        )

    def get_movies(self) -> list:
        """Список фильмов (сервис api)."""
        response = requests.get(f"{API_URL}/movies", timeout=10)
        response.raise_for_status()
        return response.json()["movies"]  # ответ обёрнут: {"movies": [...], ...}
