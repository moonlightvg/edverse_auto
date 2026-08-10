import re
import allure
from playwright.sync_api import Page, expect
from config import APP_BASE_URL
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from utils.data_generators import generate_register_user
from locators.movies_locators import MoviesLocators
from locators.header_locators import HeaderLocators


@allure.title("Сквозной сценарий: регистрация → логин → каталог → фильм → выход")
@allure.feature("E2E")
def test_e2e_flow(page: Page):
    user = generate_register_user()

    with allure.step("Регистрация нового пользователя"):
        RegisterPage(page).open(APP_BASE_URL + "/register").register(
            user["full_name"], user["email"], user["password"]
        )
        # после регистрации сайт ведёт на /login
        expect(page).to_have_url(APP_BASE_URL + "/login")

    with allure.step("Логин тем же пользователем"):
        LoginPage(page).login(user["email"], user["password"])
        expect(page).to_have_url(APP_BASE_URL + "/")

    with allure.step("Открываем каталог"):
        page.goto(APP_BASE_URL + "/movies")
        expect(page.locator(MoviesLocators.CARD_TITLE).first).to_be_visible()

    with allure.step("Переходим на страницу фильма"):
        page.locator(MoviesLocators.MORE_BUTTON).first.click()
        expect(page).to_have_url(re.compile(r"/movies/\d+"))
        expect(page.locator("h2").first).to_be_visible()

    with allure.step("Скриншот финального состояния"):
        allure.attach(
            page.screenshot(),
            name="Сквозной сценарий",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Выход из аккаунта"):
        page.goto(APP_BASE_URL + "/profile")
        page.locator(HeaderLocators.LOGOUT_BUTTON).click()
        expect(page.locator(HeaderLocators.LOGIN_BUTTON)).to_be_visible()