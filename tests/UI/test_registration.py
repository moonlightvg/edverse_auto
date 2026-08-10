import allure
import pytest
from playwright.sync_api import Page, expect
from config import APP_BASE_URL
from pages.register_page import RegisterPage
from utils.data_generators import generate_register_user
from locators.register_locators import RegisterLocators


@allure.title("TC-01 Регистрация с валидными данными")
@allure.feature("Регистрация")
def test_register_valid(page: Page):
    user = generate_register_user()
    RegisterPage(page).open(APP_BASE_URL + "/register").register(
        user["full_name"], user["email"], user["password"]
    )
    # сайт ведёт на /login после регистрации 
    expect(page).to_have_url(APP_BASE_URL + "/login")


@allure.title("TC-02 Пароли не совпадают")
@allure.feature("Регистрация")
def test_register_passwords_mismatch(page: Page):
    user = generate_register_user()
    register = RegisterPage(page).open(APP_BASE_URL + "/register")
    register.full_name_input.fill(user["full_name"])
    register.email_input.fill(user["email"])
    register.password_input.fill(user["password"])
    register.password_repeat_input.fill("Different123")
    register.submit_button.click()

    expect(page).to_have_url(APP_BASE_URL + "/register")  # остались на месте


@allure.title("TC-03 Пароль не проходит требования")
@allure.feature("Регистрация")
def test_register_weak_password(page: Page):
    user = generate_register_user()
    register = RegisterPage(page).open(APP_BASE_URL + "/register")
    register.full_name_input.fill(user["full_name"])
    register.email_input.fill(user["email"])
    register.password_input.fill("short")  # < 8 символов
    register.password_repeat_input.fill("short")
    register.submit_button.click()

    # ошибка - текст, data-qa-id у неё нет
    expect(page.get_by_text("Пароль должен содержать не менее 8 символов").first).to_be_visible()


@allure.title("TC-04 Пустые обязательные поля")
@allure.feature("Регистрация")
def test_register_empty_fields(page: Page):
    RegisterPage(page).open(APP_BASE_URL + "/register")
    page.locator(RegisterLocators.SUBMIT_BUTTON).click()

    expect(page).to_have_url(APP_BASE_URL + "/register")
