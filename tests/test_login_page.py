import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@allure.title("Тест авторизации с неверными данными")
@allure.feature("Авторизация")
def test_login_with_wrong_password(page: Page):
    with allure.step("Открываем страницу логина"):
        LoginPage(page).open("https://edversemovie.ru/login")

    with allure.step("Вводим email и пароль"):
        LoginPage(page).login("test@mail.ru", "wrong_password")
        page.wait_for_timeout(1000)  # Ждем ответа

    with allure.step("Проверяем URL (остались на логине)"):
        expect(page).to_have_url("https://edversemovie.ru/login")