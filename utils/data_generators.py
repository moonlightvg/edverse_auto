from faker import Faker  # Импортируем Faker для генерации фейковых данных

fake = Faker()  # Создаем экземпляр генератора
# Faker() - создает генератор с английской локализацией по умолчанию
# Можно указать локализацию: Faker('ru_RU') для русских данных

def generate_user():  # Функция генерации пользователя
    """Генерирует тестового пользователя"""  # Докстринг
    return {  # Возвращаем словарь с данными
        "email": fake.email(),  # Генерируем фейковый email
        "password": fake.password(length=12),  # Генерируем пароль длиной 12 символов
        # fake.password() - генерирует случайный пароль
        # length=12 - длина пароля
        "first_name": fake.first_name(),  # Генерируем имя
        "last_name": fake.last_name()  # Генерируем фамилию
    }
    
def generate_login_page_user():
    return {
        "email":fake.email(),
        "password": fake.password(length=12)
    }
    