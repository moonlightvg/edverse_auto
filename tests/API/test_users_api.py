import allure
from api.client import ApiClient
from utils.data_generators import generate_register_user


@allure.title("API: создание пользователя возвращает id")
@allure.feature("API")
def test_create_user():
    user = generate_register_user()          # данные из Faker
    user["email"] = user["email"].replace("_", "")

    created = ApiClient().create_user(
        user["email"], user["password"], user["full_name"]
    )

    assert created["id"], "сервер должен вернуть id созданного пользователя"
    
    allure.attach(
    str(user),
    name="зарегистрированный юзер",
    attachment_type=allure.attachment_type.JSON,
)
    
@allure.title("API: созданный пользователь существует")
@allure.feature("API")
def test_created_user_exists():
    user = generate_register_user()
    user["email"] = user["email"].replace("_", "")
    client = ApiClient()

    created = client.create_user(user["email"], user["password"], user["full_name"])

    assert created["email"] == user["email"]
    assert created["fullName"] == user["full_name"]