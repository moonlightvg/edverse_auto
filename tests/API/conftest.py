import os
import pytest
import psycopg2
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from api.api_manager import ApiManager
from config import AUTH_URL, API_URL
from db.client import DbClient
from utils.data_generators import generate_register_user


@pytest.fixture(autouse=True)
def check_db_access():
    """Пропускает тест если БД недоступна."""
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"), connect_timeout=3, sslmode='disable',
        )
        conn.close()
    except Exception as e:
        print(f"\n=== DB ERROR: {e} ===\n")
        pytest.skip(f"DB недоступна: {e}")


@pytest.fixture(scope="session")
def session():
    import requests
    s = requests.Session()
    retries = Retry(total=3, backoff_factor=1,
                    allowed_methods=["GET", "DELETE", "PUT", "HEAD", "OPTIONS"])
    s.mount("https://", HTTPAdapter(max_retries=retries))
    yield s
    s.close()


@pytest.fixture()
def api_manager(session):
    manager = ApiManager(session, AUTH_URL, API_URL)
    yield manager
    manager.close()


@pytest.fixture()
def created_user(api_manager):
    user = generate_register_user()
    user["email"] = user["email"].replace("_", "")
    response = api_manager.auth.register_user({
        "email": user["email"],
        "fullName": user["full_name"],
        "password": user["password"],
        "passwordRepeat": user["password"],
    })
    created = response.json()
    created["password"] = user["password"]
    login_response = api_manager.auth.login({
        "email": user["email"],
        "password": user["password"],
    })
    created["token"] = login_response.json()["accessToken"]
    yield created
    api_manager.auth.delete_user(created["id"], created["token"])


@pytest.fixture()
def db():
    client = DbClient()
    yield client
    client.close()
