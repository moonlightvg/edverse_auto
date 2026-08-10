"""Скрипт проверки API (практика урока «Requests»).

Запуск: python scripts/check_api.py
"""
from api.client import ApiClient
from utils.data_generators import generate_register_user


def main():
    user = generate_register_user()
    user["email"] = user["email"].replace("_", "")

    created = ApiClient().create_user(
        user["email"], user["password"], user["full_name"]
    )
    print(f"Юзер создан: id={created['id']}, email={created['email']}")

    token = ApiClient().login(user["email"], user["password"])
    print(f"Логин работает: токен получен ({len(token)} символов)")

    me = ApiClient().get_me(token)
    print(f"Профиль: {me['fullName']} <{me['email']}>")

    ApiClient().delete_user(created["id"], token)
    print("Юзер удалён - мусора в базе нет")


if __name__ == "__main__":
    main()
