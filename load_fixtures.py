import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Publisher, Shop, Book, Stock, Sale

DB_USER = 'postgres'
DB_PASSWORD = '19071993'
DB_NAME = 'bookstore'
DB_HOST = 'localhost'
DB_PORT = '5432'

DSN = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

with open('tests_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

model_map = {
    'publisher': Publisher,
    'shop': Shop,
    'book': Book,
    'stock': Stock,
    'sale': Sale,
}

for record in data:
    model = model_map[record['model']]
    obj = model(id=record['pk'], **record['fields'])
    session.add(obj)

session.commit()
print("✅ Данные успешно загружены.")
