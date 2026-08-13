import allure
import pytest
import requests

from api.client import AUTH_URL, ApiClient
from api.validation import assert_has_fields, assert_status
from utils.data_generators import generate_register_user


@allure.title("API: пользователь существует после создания")
@allure.feature("API")
def test_created_user_exists(created_user):
    """Фикстура created_user создаёт юзера через Faker и удаляет после теста."""
    assert created_user["email"], "у юзера должен быть email"

    # логин - лучшее подтверждение что юзер реален
    token = ApiClient().login(created_user["email"], created_user["password"])
    assert token


@allure.title("API: регистрация возвращает полный объект")
@allure.feature("API")
def test_create_user_returns_expected_shape(created_user):
    """Проверяем форму ответа - обязательные поля на месте."""
    assert_has_fields(created_user, ["id", "email", "fullName"])

# Негативные кейсы тестируют ОШИБОЧНЫЕ данные - хардкод намеренный.
# Faker генерирует валидные данные, для негативных тестов не подходит.

@allure.title("API: регистрация с невалидными данными")
@allure.feature("API")
@pytest.mark.parametrize("payload", [
    # кривой email - нет @, сервер должен отклонить
    {"email": "не_email", "fullName": "Тест Тестов",
     "password": "Password123", "passwordRepeat": "Password123"},
    # слабый пароль - 3 символа, меньше минимума (8)
    {"email": "test@mail.ru", "fullName": "Тест Тестов", "password": "123"},
    # пустой payload - ничего не передано
    {},
], ids=["кривой_email", "слабый_пароль", "пустой_payload"])
def test_register_invalid_data(payload):
    """Параметризация: три ошибочных payload - три отдельных прогона в отчёте."""
    response = requests.post(f"{AUTH_URL}/register", json=payload, timeout=10)
    assert_status(response, 400)


@allure.title("API: дубль email - конфликт")
@allure.feature("API")
def test_register_duplicate_email(created_user):
    """Тот же email (из Faker) второй раз - 409 Conflict.
    Пароль и email берём из фикстуры - они уже валидные."""
    response = requests.post(
        f"{AUTH_URL}/register",
        json={
            "email": created_user["email"],       # email из фикстуры (Faker)
            "fullName": "Дубль Дубль",
            "password": created_user["password"],  # пароль из фикстуры (Faker)
            "passwordRepeat": created_user["password"],
        },
        timeout=10,
    )
    assert_status(response, 409)


@allure.title("API: логин с неверным паролем")
@allure.feature("API")
def test_login_wrong_password(created_user):
    """Правильный email (из Faker), неправильный пароль - 401.
    Пароль намеренно другой - хардкод, потому что нам нужен именно неверный."""
    response = requests.post(
        f"{AUTH_URL}/login",
        json={"email": created_user["email"], "password": "WrongPass1"},
        timeout=10,
    )
    assert_status(response, 401)
