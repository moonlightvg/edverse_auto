class LoginLocators:
    """Локаторы для страницы логина"""
    # Поля ввода
    EMAIL_INPUT = "[data-qa-id='login_email_input']"
    PASSWORD_INPUT = "[data-qa-id='login_password_input']"
    # Кнопки
    LOGIN_BUTTON = "[data-qa-id='login_submit_button']"
    # Регистрация
    REGISTER_LINK = "a:has-text('Зарегистрироваться')"