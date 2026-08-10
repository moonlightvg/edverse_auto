import pytest
import allure
from playwright.sync_api import Page, expect
from config import APP_BASE_URL
from locators.header_locators import HeaderLocators


@pytest.mark.parametrize("path, expected_title", [
    ("/", "Cinescope"),
    ("/movies", "Все фильмы | Cinescope"),
    ("/login", "Cinescope"),
    ("/register", "Cinescope"),
], ids=["главная", "каталог", "логин", "регистрация"])
@allure.title("Открытие {path} - заголовок {expected_title}")
@allure.feature("Навигация")
def test_page_opens(page: Page, path, expected_title):
    page.goto(APP_BASE_URL + path)

    expect(page).to_have_title(expected_title)


@pytest.mark.parametrize("path", ["/", "/movies"], ids=["главная", "каталог"])
@allure.title("Кнопка «Войти» видна на {path}")
@allure.feature("Навигация")
def test_header_login_button_visible(page: Page, path):
    page.goto(APP_BASE_URL + path)

    expect(page.locator(HeaderLocators.LOGIN_BUTTON)).to_be_visible()