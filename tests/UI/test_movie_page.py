import re #Для работы с регулярками (RegEx)
import allure
from playwright.sync_api import Page, expect
from config import APP_BASE_URL
from locators.movies_locators import MoviesLocators


@allure.title("Переход на страницу фильма по «Подробнее»")
@allure.feature("Фильм")
def test_open_movie_details(page: Page):
    page.goto(APP_BASE_URL + "/movies")

    page.locator(MoviesLocators.MORE_BUTTON).first.click()

    expect(page).to_have_url(re.compile(r"/movies/\d+"))

    with allure.step("Контент страницы фильма виден"):
        expect(page.locator("h2").first).to_be_visible()

    with allure.step("Скриншот страницы фильма"):
        allure.attach(
            page.screenshot(),
            name="Страница фильма",
            attachment_type=allure.attachment_type.PNG,
        )