import os
import sqlalchemy
from models import Base

# Подключение к БД
# Можно указать напрямую или взять из переменных окружения
# Пример строки для PostgreSQL:
# postgresql://<username>:<password>@localhost:5432/<database_name>

DB_NAME = os.getenv('DB_NAME', 'bookstore')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '19071993')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

DSN = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = sqlalchemy.create_engine(DSN)

# Создание таблиц в БД
Base.metadata.create_all(engine)
print("✅ Таблицы успешно созданы.")
