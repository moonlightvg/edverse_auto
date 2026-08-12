import random
import string
import uuid
from faker import Faker

fake = Faker()

class DataGenerator:
    """Фабрика тестовых данных: уникальные, валидные, без коллизий."""

    @staticmethod
    def random_username() -> str:
        return fake.name()

    @staticmethod
    def random_password() -> str:
        """Пароль, который точно пройдёт валидацию API.

        Наш API требует: заглавная + цифра, минимум 8 символов.
        Собираем гарантированно: по одному символу каждого класса + хвост.
        """
        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        special = random.choice("@#$%&*-_+=.")
        alphabet = string.ascii_letters + string.digits + "@#$%&*-_+=."
        rest = "".join(random.choices(alphabet, k=random.randint(8, 14)))
        parts = list(lower + upper + digit + special + rest)
        random.shuffle(parts)
        return "".join(parts)

    @staticmethod
    def unique_email(domain: str = "mail.ru") -> str:
        """Уникальный email без коллизий.

        Faker умеет генерить одинаковые email (у него пул данных),
        а повторный email в нашем API даёт 409. Добавляем uuid-хвост.
        """
        return f"autotest-{uuid.uuid4().hex[:12]}@{domain}"

    @staticmethod
    def unique_username(prefix: str = "Тест") -> str:
        """Полное имя: два слова, только буквы (fullName цифры не любит)."""
        return f"{prefix} {fake.last_name()}"

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
