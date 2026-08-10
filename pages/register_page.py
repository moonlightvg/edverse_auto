from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.register_locators import RegisterLocators


class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.full_name_input = page.locator(RegisterLocators.FULL_NAME_INPUT)
        self.email_input = page.locator(RegisterLocators.EMAIL_INPUT)
        self.password_input = page.locator(RegisterLocators.PASSWORD_INPUT)
        self.password_repeat_input = page.locator(RegisterLocators.PASSWORD_REPEAT_INPUT)
        self.submit_button = page.locator(RegisterLocators.SUBMIT_BUTTON)

    def register(self, full_name: str, email: str, password: str):
        self.full_name_input.fill(full_name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.password_repeat_input.fill(password)
        self.submit_button.click()
        return self