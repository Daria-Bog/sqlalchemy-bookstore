import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Shop, Sale, Stock

# Параметры подключения
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '19071993')
DB_NAME = os.getenv('DB_NAME', 'bookstore')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

DSN = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

# Ввод имени или ID издателя
publisher_input = input("Введите имя или ID издателя: ")

if publisher_input.isdigit():
    publisher = session.query(Publisher).filter(Publisher.id == int(publisher_input)).first()
else:
    publisher = session.query(Publisher).filter(Publisher.name.ilike(f"%{publisher_input}%")).first()

if not publisher:
    print("Издатель не найден.")
else:
    print(f"\n📚 Книги издателя: {publisher.name}\n")
    query = (
        session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
        .join(Stock, Stock.id_book == Book.id)
        .join(Sale, Sale.id_stock == Stock.id)
        .join(Shop, Shop.id == Stock.id_shop)
        .filter(Book.id_publisher == publisher.id)
        .order_by(Sale.date_sale)
    )

    for title, shop_name, price, date_sale in query.all():
        print(f"{title:25} | {shop_name:15} | {int(price)} | {date_sale.strftime('%d-%m-%Y')}")

session.close()
