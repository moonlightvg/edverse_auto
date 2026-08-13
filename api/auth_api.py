"""API-класс для сервиса auth (юзеры, логин, профиль)."""
from api.requester import CustomRequester


class AuthAPI(CustomRequester):
    """Работа с юзерами и логином (сервис auth.dev-edversemovie.ru)."""

    REGISTER = "/register"
    LOGIN = "/login"
    ME = "/user/me"
    USER_BY_ID = "/user/{user_id}"

    def __init__(self, session, base_url):
        super().__init__(session=session, base_url=base_url)

    def register_user(self, user_data, expected_status=201):
        """Регистрация нового пользователя."""
        return self.send_request(
            "POST", self.REGISTER, data=user_data,
            expected_status=expected_status,
        )

    def login(self, login_data, expected_status=200):
        """Логин, возвращает ответ с accessToken."""
        return self.send_request(
            "POST", self.LOGIN, data=login_data,
            expected_status=expected_status,
        )

    def get_me(self, token, expected_status=200):
        """Свой профиль с Bearer-токеном."""
        return self.send_request(
            "GET", self.ME,
            headers={"Authorization": f"Bearer {token}"},
            expected_status=expected_status,
        )

    def delete_user(self, user_id, token, expected_status=200):
        """Удаление пользователя (только своего)."""
        endpoint = self.USER_BY_ID.format(user_id=user_id)
        return self.send_request(
            "DELETE", endpoint,
            headers={"Authorization": f"Bearer {token}"},
            expected_status=expected_status,
        )
