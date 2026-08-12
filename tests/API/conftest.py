import pytest
from api.client import ApiClient
from utils.data_generators import generate_register_user


@pytest.fixture()
def created_user():
    """Создаёт пользователя через API и удаляет его после теста."""
    client = ApiClient()
    user = generate_register_user()
    user["email"] = user["email"].replace("_", "")  # сервер не любит подчёркивания

    created = client.create_user(user["email"], user["password"], user["full_name"])

    # пароль в ответе API нет - кладём сами, тестам он нужен для логина
    created["password"] = user["password"]

    # для чистки нужен токен: логинимся сразу после создания
    created["token"] = client.login(user["email"], user["password"])

    yield created  # тест получает созданного юзера и работает

    # а после теста - уборка (выполнится даже если тест упал!)
    client.delete_user(created["id"], created["token"])