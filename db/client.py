import os                       # os.getenv - читаем переменные окружения (.env)
import psycopg2                 # библиотека для работы с PostgreSQL
from dotenv import load_dotenv  # функция, которая загружает .env в окружение

load_dotenv()                   # вызываем загрузку .env сразу при импорте модуля


class DbClient:                 # класс-обёртка над подключением к БД
    """Обёртка над psycopg2: подключение и простые запросы."""

    def __init__(self):                                     # конструктор: вызывается при создании DbClient()
        self.conn = psycopg2.connect(                       # устанавливаем соединение с PostgreSQL
            host=os.getenv("DB_HOST"),                      # адрес сервера - берём из .env
            port=os.getenv("DB_PORT"),                      # порт - из .env
            dbname=os.getenv("DB_NAME"),                    # имя базы - из .env
            user=os.getenv("DB_USER"),                      # пользователь - из .env
            password=os.getenv("DB_PASS"), sslmode='disable',                  # пароль - из .env
        )
        self.conn.autocommit = True  # не ждём commit вручную - проще для SELECT

    def fetch_one(self, query: str, params: tuple = ()) -> tuple | None:
        """Одна строка результата (или None, если строк нет)."""
        with self.conn.cursor() as cur:  # создаём курсор (через него выполняются запросы)
            cur.execute(query, params)   # выполняем запрос; значения из params подставляет psycopg2
            return cur.fetchone()        # забираем первую строку результата

    def fetch_all(self, query: str, params: tuple = ()) -> list[tuple]:
        """Все строки результата списком."""
        with self.conn.cursor() as cur:  # новый курсор для этого запроса
            cur.execute(query, params)   # выполняем запрос
            return cur.fetchall()        # забираем все строки

    def close(self) -> None:        # закрываем соединение
        self.conn.close()