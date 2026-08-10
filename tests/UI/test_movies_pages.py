import allure
from playwright.sync_api import Page, expect
from config import APP_BASE_URL
from locators.movies_locators import MoviesLocators


@allure.title("Каталог фильмов открывается")
@allure.feature("Каталог")
def test_movies_page_opens(page: Page):
    page.goto(APP_BASE_URL + "/movies")

    expect(page).to_have_title("Все фильмы | Cinescope")
    expect(page.locator(MoviesLocators.CARD_TITLE).first).to_be_visible()


@allure.title("Фильтр по месту меняет список")
@allure.feature("Каталог")
def test_filter_by_location(page: Page):
    page.goto(APP_BASE_URL + "/movies")

    
    page.locator(MoviesLocators.FILTER_LOCATION).click()
    page.locator(MoviesLocators.LOCATION_OPTION_MSK).click()

    expect(page.locator(MoviesLocators.CARD_TITLE).first).to_be_visible()


@allure.title("Фильтр по жанру работает")
@allure.feature("Каталог")
def test_filter_by_genre(page: Page):
    page.goto(APP_BASE_URL + "/movies")

    # у жанра нет data-qa-id, ищем кнопку по тексту
    page.locator("button:has-text('Жанр')").click()
    page.locator("[role='option']:has-text('Драма')").click()

    expect(page.locator(MoviesLocators.CARD_TITLE).first).to_be_visible()


@allure.title("Переход на вторую страницу каталога")
@allure.feature("Каталог")
def test_pagination_next_page(page: Page):
    page.goto(APP_BASE_URL + "/movies")

    page.get_by_role("link", name="Go to next page").click()

    expect(page.locator(MoviesLocators.CARD_TITLE).first).to_be_visible()
