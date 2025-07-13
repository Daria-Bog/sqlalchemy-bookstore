import sqlalchemy
from models import Base

# Настройки подключения к БД
DB_USER = 'postgres'
DB_PASSWORD = '19071993'  # замени на свой пароль
DB_NAME = 'bookstore'
DB_HOST = 'localhost'
DB_PORT = '5432'

DSN = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = sqlalchemy.create_engine(DSN)

# Создание таблиц в базе данных
Base.metadata.create_all(engine)
print("Таблицы успешно созданы.")
