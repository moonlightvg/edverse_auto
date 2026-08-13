def assert_status(response, expected: int) -> None:
    """Проверяет статус-код ответа с понятным сообщением."""
    assert response.status_code == expected, (
        f"Ожидали {expected}, получили {response.status_code}: "
        f"{response.text[:200]}"
    )


def assert_has_fields(obj: dict, fields: list[str]) -> None:
    """Проверяет, что в объекте есть все нужные поля."""
    missing = [f for f in fields if f not in obj]
    assert not missing, f"В ответе нет полей: {missing}"