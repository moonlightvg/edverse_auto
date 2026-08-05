import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@allure.title("Демо: LoginPage работает")
def test_login_page_demo(page: Page):
    LoginPage(page).open("https://edversemovie.ru/login")\
        .login("test@mail.ru", "password123")

    # креды учебные, такого юзера нет - остаёмся на логине.
    # Здесь проверяем механику: страница открылась, форма заполнилась и отправилась.
    expect(page).to_have_url("https://edversemovie.ru/login")