import allure
from api.client import ApiClient
from utils.data_generators import generate_register_user


@allure.title("API: пользователь существует после создания")
@allure.feature("API")
def test_created_user_exists(created_user):
    assert created_user["email"], "у юзера должен быть email"

    # а то, что он реально может залогиниться, - лучшее подтверждение
    token = ApiClient().login(created_user["email"], created_user["password"])
    assert token