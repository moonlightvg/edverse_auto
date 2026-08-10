from faker import Faker

fake = Faker()


def generate_register_user() -> dict:
    """Генерирует данные нового пользователя для регистрации."""
    return {
        "full_name": fake.name(),
        "email": fake.email().replace("_", ""),  # API отклоняет email с подчёркиванием
        "password": fake.password(length=12, special_chars=False),  # сайт не любит = и {}
    }
    


def generate_user() -> dict:
    """Генерирует тестового пользователя (имя/фамилия раздельно)."""
    return {
        "email": fake.email(),
        "password": fake.password(length=12),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
    }


def generate_login_page_user() -> dict:
    """Данные для формы логина."""
    return {
        "email": fake.email(),
        "password": fake.password(length=12),
    }
