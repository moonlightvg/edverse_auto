from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.locator(LoginLocators.EMAIL_INPUT)
        self.password_input = page.locator(LoginLocators.PASSWORD_INPUT)
        self.login_button = page.locator(LoginLocators.LOGIN_BUTTON)
    
    def login(self, email: str, password: str):
        """Заполняет форму и нажимает «Войти»."""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        return self