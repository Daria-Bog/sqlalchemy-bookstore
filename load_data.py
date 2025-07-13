import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Publisher, Shop, Book, Stock, Sale

# Подключение к БД
DSN = 'postgresql://postgres:19071993@localhost:5432/bookstore'
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

# Загрузка данных из JSON-файла
with open('tests_data.json', 'r', encoding='utf-8') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    
    session.add(model(id=record.get('pk'), **record.get('fields')))

session.commit()
print("✅ Данные успешно загружены.")
