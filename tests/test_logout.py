import allure
import pytest
from playwright.sync_api import Page, expect
from config import APP_BASE_URL
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from utils.data_generators import generate_register_user
from locators.header_locators import HeaderLocators


@pytest.fixture()
def registered_user(page: Page) -> dict:
    """Регистрирует пользователя и проверяет, что регистрация прошла."""
    user = generate_register_user()
    RegisterPage(page).open(APP_BASE_URL + "/register").register(
        user["full_name"], user["email"], user["password"]
    )
    expect(page).to_have_url(APP_BASE_URL + "/login")
    expect(page.get_by_text("Подтвердите свою почту")).to_be_visible()

    return user


@allure.title("Выход из аккаунта возвращает к «Войти»")
@allure.feature("Авторизация")
def test_logout(page: Page, registered_user):
    # 1. Логинимся зарегистрированным пользователем
    LoginPage(page).open(APP_BASE_URL + "/login").login(
        registered_user["email"], registered_user["password"]
    )
    expect(page).to_have_url(APP_BASE_URL + "/")

    # 2. Выходим: кнопка на странице профиля /profile
    page.goto(APP_BASE_URL + "/profile")
    page.locator(HeaderLocators.LOGOUT_BUTTON).click()

    # 3. Снова видно «Войти»
    expect(page.locator(HeaderLocators.LOGIN_BUTTON)).to_be_visible()
