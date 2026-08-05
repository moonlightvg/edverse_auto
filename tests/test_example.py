import pytest  # Импортируем pytest для создания фикстур
from playwright.sync_api import Page, expect
import allure  # Добавляем импорт

@allure.title("Проверка открытия главной страницы Edversemovie")  # Добавляем название в отчет
@allure.feature("Навигация")  # Группируем по функциональности
def test_open_edversemovie(page: Page):
    """Проверяем, что открывается edversemovie."""

    with allure.step("Открываем сайт"):  # Шаг для отчета
        page.goto("https://edversemovie.ru/")

    with allure.step("Проверяем заголовок"):  # Еще один шаг
        expect(page).to_have_title("Cinescope")

    # Добавляем скриншот в отчет
    allure.attach(
        page.screenshot(),
        name="Скриншот страницы",
        attachment_type=allure.attachment_type.PNG
    )