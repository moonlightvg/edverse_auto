import allure                    # Allure-декораторы (название, раздел отчёта)
from db.client import DbClient   # наш клиент БД из шага 2


@allure.title("API: созданный пользователь есть в БД")  # как тест будет называться в отчёте
@allure.feature("БД")                                   # раздел, куда попадёт тест в отчёте
def test_created_user_in_db(created_user):              # created_user - фикстура из tests/api/conftest.py
    db = DbClient()                        # создаём подключение к БД
    try:                                   # try/finally: закрыть соединение при ЛЮБОМ исходе
        row = db.fetch_one(                # ищем нашего юзера в БД по email
            "SELECT id, email FROM users WHERE email = %s",  # %s - «дырка» для параметра
            (created_user["email"],),      # параметр передаётся кортежем; запятая обязательна!
        )
        assert row, "пользователь не найден в БД"  # row = None (не нашли)? → тест падает
        assert row[0] == created_user["id"], "id в БД не совпадает с id из API"  # сверяем id
    finally:
        db.close()                         # закрываем соединение (выполнится всегда)
