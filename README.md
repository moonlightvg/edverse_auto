# AUTO_EDVERSE

Учебный проект по автоматизации тестирования: UI, API и проверки базы данных
на примере сайта [edversemovie.ru](https://edversemovie.ru). Проект создан
в рамках курса «Автоматизация тестирования на Python» и растёт вместе с ним:
после каждого урока ты добавляешь в него новые тесты и коммитишь результат.

## Стек

- Python 3.11+
- Pytest (фикстуры, параметризация, метки)
- Playwright (UI-тесты)
- Requests (API-тесты)
- Allure (отчёты: степы, скриншоты, артефакты)
- Faker (генерация тестовых данных)
- psycopg2 (проверки в PostgreSQL)
- Jenkins (автоматический запуск по расписанию)

## Структура

```text
AUTO_EDVERSE/
├── locators/          # локаторы по страницам (не в тестах!)
├── pages/             # Page Object: BasePage и страницы сайта
├── api/               # API-клиент (ApiClient) и проверки ответов
├── db/                # клиент базы данных (DbClient)
├── utils/             # хелперы: Faker-генераторы, ожидания, Allure, видео
├── tests/
│   ├── ui/            # UI-тесты
│   └── api/           # API-тесты и проверки БД
├── data/              # тестовые данные
├── conftest.py        # общие фикстуры (browser, page, хуки)
├── pytest.ini         # конфигурация pytest (метки, Allure)
├── requirements.txt
└── .env               # секреты, в git не попадает (см. .gitignore)
```

## Установка

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Создай `.env` в корне проекта (шаблон - в уроке про данные):

```bash
LOGIN_EMAIL=...
LOGIN_PASSWORD=...
DB_HOST=...
DB_PORT=...
DB_NAME=db_movies
DB_USER=...
DB_PASS=...
```

## Запуск тестов

```bash
pytest                           # все тесты
pytest -m smoke                  # только быстрые
pytest tests/api/                # только API
pytest --alluredir=allure-results  # с отчётом Allure
allure serve allure-results      # посмотреть отчёт
```

## CI/CD

Автоматический запуск тестов - Jenkins (ночная сборка в 3:00, публикация
Allure-отчёта). Каждый ученик работает в своей папке Jenkins, чужие джобы
не трогает.

## Правило проекта

После каждого урока - коммит с описанием того, что сделал:

```bash
git add .
git commit -m "Урок N: что сделано"
git push
```

История репозитория - твой дневник: в любой момент видно, что и когда появилось.

## Автор

Курс «Автоматизация тестирования на Python». Проект предназначен для
обучения: пиши код сам, разбирай ошибки, коммить результат.
