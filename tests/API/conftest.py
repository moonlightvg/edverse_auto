import pytest
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from api.api_manager import ApiManager
from config import AUTH_URL, API_URL
from utils.data_generators import generate_register_user

@pytest.fixture(scope="session")
def session():
    """Сессия с ретраями на сетевые сбои. Живёт один прогон."""
    import requests
    s = requests.Session()
    retries = Retry(total=3, backoff_factor=1,
                    allowed_methods=["GET", "DELETE", "PUT", "HEAD", "OPTIONS"])
    s.mount("https://", HTTPAdapter(max_retries=retries))
    yield s
    s.close()


@pytest.fixture()
def api_manager(session):
    """ApiManager - единая точка входа для всех API."""
    manager = ApiManager(session, AUTH_URL, API_URL)
    yield manager
    manager.close()

@pytest.fixture()
def created_user(api_manager):
    """Создаёт пользователя через API и удаляет его после теста."""
    user = generate_register_user()
    user["email"] = user["email"].replace("_", "")  # сервер не любит подчёркивания

    response = api_manager.auth.register_user({
        "email": user["email"],
        "fullName": user["full_name"],
        "password": user["password"],
        "passwordRepeat": user["password"],
    })
    created = response.json()

    # пароль в ответе API нет - кладём сами, тестам он нужен для логина
    created["password"] = user["password"]

    # для чистки нужен токен: логинимся сразу после создания
    login_response = api_manager.auth.login({
        "email": user["email"],
        "password": user["password"],
    })
    created["token"] = login_response.json()["accessToken"]

    yield created  # тест получает созданного юзера и работает

    # а после теста - уборка (выполнится даже если тест упал!)
    api_manager.auth.delete_user(created["id"], created["token"])
