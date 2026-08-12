"""Подготовительные операции: всё, что нужно сделать ДО теста."""
from api.client import ApiClient
from utils.data_generators import generate_register_user


def create_test_user() -> dict:
    """Создаёт пользователя через API и возвращает его данные.

    В возвращаемом словаре: id (UUID), email, fullName, password, token.
    token нужен для удаления юзера (DELETE /user/{id} требует авторизацию).
    """
    user = generate_register_user()
    user["email"] = user["email"].replace("_", "")  # сервер не любит подчёркивания

    client = ApiClient()
    created = client.create_user(user["email"], user["password"], user["full_name"])
    created["password"] = user["password"]
    created["token"] = client.login(user["email"], user["password"])
    return created