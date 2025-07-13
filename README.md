Проект: Книжный магазин на SQLAlchemy
Этот проект демонстрирует создание и взаимодействие с базой данных книжного магазина с использованием SQLAlchemy (ORM) и PostgreSQL.

📦 Состав проекта
models.py — модели таблиц БД (Publisher, Book, Shop, Stock, Sale).

create_tables.py — создание таблиц в БД.

load_fixtures.py — заготовка для загрузки JSON-файлов.

tests_data.json — JSON-файл с тестовыми данными.

load_data.py — загрузка данных из JSON в БД.

query_publisher.py — выполнение запроса по имени или ID издателя.

create_db.py — создание БД PostgreSQL (по желанию).

README.md — описание проекта.

🔧 Используемые технологии
Python 3.12

SQLAlchemy

PostgreSQL

🚀 Как запустить
Установите зависимости:
pip install sqlalchemy psycopg2-binary

Убедитесь, что PostgreSQL запущен и создана база данных bookstore.

Создайте таблицы:
python create_tables.py

Загрузите тестовые данные:
python load_data.py

Запустите поиск книг по издателю:
python query_publisher.py

📂 Пример структуры проекта
orm_project/
├── __pycache__/                  # автоматически создаётся, можно игнорировать
├── create_db.py
├── create_tables.py
├── load_data.py
├── load_fixtures.py
├── models.py
├── query_publisher.py
├── tests_data.json
└── README.md

📌 Советы
Файл __pycache__ можно исключить из Git с помощью .gitignore.

Лучше хранить пароли и настройки подключения в .env файле или использовать переменные окружения.


