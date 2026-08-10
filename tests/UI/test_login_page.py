import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

BASE_URL = "https://edversemovie.ru" # Вынес для удобства, еще лучше вынести в конфиг, для тестов dev/test/prd

@allure.title("Тест авторизации с неверными данными")
@allure.feature("Авторизация")
def test_login_with_wrong_password(page: Page):
    with allure.step("Открываем страницу логина"):
        LoginPage(page).open(f"{BASE_URL}/login")

    with allure.step("Вводим email и пароль"):
        LoginPage(page).login("test@mail.ru", "wrong_password")
        page.wait_for_timeout(1000)  # Ждем ответа

    with allure.step("Проверяем URL (остались на логине)"):
        expect(page).to_have_url(f"{BASE_URL}/login")


@allure.title("Параметризованный тест логина: {email} / {password}")
@allure.feature("Авторизация")
@pytest.mark.parametrize("email, password", [
    ("test@mail.ru", "wrong_password"),      # неверный пароль
    ("no_such_user@mail.ru", "Password123"), # несуществующий email
    ("", ""),                                 # пустые поля
], ids=["неверный_пароль", "несуществующий_email", "пустые_поля"])

def test_login_invalid_data(page: Page, email, password):
    """Один тест, много наборов данных: остаёмся на логине во всех случаях."""
    with allure.step("Открываем страницу логина"):
        LoginPage(page).open(f"{BASE_URL}/login")

    with allure.step("Вводим данные и жмём «Войти»"):
        LoginPage(page).login(email, password)
        page.wait_for_timeout(1000)

    with allure.step("Проверяем: остались на логине"):
        expect(page).to_have_url(f"{BASE_URL}/login")
