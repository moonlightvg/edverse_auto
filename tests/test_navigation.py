import allure
from playwright.sync_api import Page, expect
from config import APP_BASE_URL
from locators.header_locators import HeaderLocators


@allure.title("Главная открывается, фильмы видны")
@allure.feature("Навигация")
def test_main_page_shows_movies(page: Page):
    page.goto(APP_BASE_URL + "/")

    expect(page).to_have_title("Cinescope")
    expect(page.locator("h3").first).to_be_visible()


@allure.title("Клик по «Войти» ведёт на /login")
@allure.feature("Навигация")
def test_go_to_login_from_header(page: Page):
    page.goto(APP_BASE_URL + "/")

    page.locator(HeaderLocators.LOGIN_BUTTON).click()

    expect(page).to_have_url(APP_BASE_URL + "/login")