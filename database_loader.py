import csv
from app import create_app
from app.models import db, Product


app = create_app()


def reading_csv_file():
    fieldnames = ['name', 'price', 'count', 'file_name']
    with open('products.csv', 'r', encoding='UTF8') as f:
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=';')
        next(reader)
        for row in reader:
            save_products(row['name'], row['price'], row['count'], row['file_name'])


def save_products(name, price, count, file_name):
    with app.app_context():
        product = Product(name=name, price=price, count=count, file_name=file_name)
        db.session.add(product)
        db.session.commit()


if __name__=='__main__':
    reading_csv_file()