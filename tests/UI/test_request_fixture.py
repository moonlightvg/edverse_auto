"""Урок «Фикстура request»: параметры из parametrize попадают в фикстуру.

request - встроенная фикстура pytest: даёт фикстуре информацию о текущем
тесте (имя, параметры, конфиг, другие фикстуры).
Самый частый сценарий: фикстура получает данные из параметризации
через request.param + indirect=True.
"""
import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

BASE_URL = "https://edversemovie.ru"


@pytest.fixture()
def login_credentials(request) -> tuple[str, str]: # <---request 
    """Берёт пару (email, password) из параметризации теста."""
    email, password = request.param
    print(f"Фикстура получила: {email} / {password}")
    return email, password


@allure.title("Фикстура request: логин с данными {email} / {password}")
@allure.feature("Авторизация")
@pytest.mark.parametrize("login_credentials", [
    ("test@mail.ru", "wrong_password"),      # неверный пароль
    ("no_such_user@mail.ru", "Password123"), # несуществующий email
], indirect=True, ids=["неверный_пароль", "несуществующий_email"])
def test_login_via_fixture(page: Page, login_credentials):
    email, password = login_credentials

    with allure.step("Открываем страницу логина"):
        LoginPage(page).open(f"{BASE_URL}/login")

    with allure.step("Логинимся данными из фикстуры"):
        LoginPage(page).login(email, password)
        page.wait_for_timeout(1000)

    with allure.step("Остались на логине (негативный кейс)"):
        expect(page).to_have_url(f"{BASE_URL}/login")
