import httplib2, os, random, requests
from bs4 import BeautifulSoup
# from flask import current_app
from app import create_app
from app.db import db
from app.models import Product, ProductGroup
# from app.product.parsers.utils import get_html, save_news

basedir = os.path.abspath(os.path.dirname(__file__))
app = create_app()


def image_loading(image_url, file_name):
    # file = image_url.split('/')[-1]
    h = httplib2.Http('.cache')
    response, content = h.request(image_url)
    out = open(os.path.join(basedir + '\\app\static\prod_image\\'), 'wb')
    # out = open(current_app.config['PRODUCTS_IMAGE_DIR'], 'wb')  # , file + '.jpg'),
    out.write(content)
    out.close()


def get_html(url, scientific_name):
    """Функция преобразует html в string"""

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/106.0.0.0 Safari/537.36'
        }

    params = {
        'target_locale': 'ru',
        'ca_id': 1010,
        'category': 10,
        'item_name': scientific_name,
        'min_price': 0,
        'max_price': 0,
        'sort': 3,
        'page': 1,
    }

    try:
        result = requests.get(url, headers=headers, params=params)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def get_xplant_products():
    item_name = ['Echeveria',
            'Haworthia',
            'Agavoides',
            'Conophytum',
            'Sedum',
            'Graptoveria',
            'Crassula',
            'Lithops',
            'Graptopetalum',
            'Pachyveria',
            'Euphorbia',
            'Adromischus',
        ]
    for scientific_name in item_name:
        html = get_html("https://m.xplant.co.kr/shop/list.php", scientific_name)
        if html:
            # save_product_group(scientific_name)
            soup = BeautifulSoup(html, 'html.parser')
            all_products = soup.find('ul', id="product1_content").find_all('li', limit=100)
            for product in all_products:
                name = product.find('p', class_='pd_title').get_text().rstrip().title()
                price = float(product.find('span', class_='amount_color').get_text().replace(',','')[:-1])
                count = random.randint(1,4)
                image_url = product.find('img', class_='product_img_radius').get('data-original')
                file_name = image_url.split('/')[-1]
                image_loading(image_url, file_name)
                image = file_name + 'jpg'
                save_products(name, price, count, image)
                try:
                    print(f'Succulent name - {name}. Amount: {price} rubles. Count in stock - {count}')
                    print(f'{image_url}')
                except(ValueError):
                    print("Sorry, this succulent is not find")


def save_products(name, price, count, image):
    with app.app_context():
        # products_exists = Product.query.filter(Product.image == image)
        # if not products_exists:
        product = Product(name=name, price=price, count=count, image=image)
        db.session.add(product)
        db.session.commit()


def save_product_group(group_name):
    with app.app_context():
        # product_group_exists = ProductGroup.query.filter(ProductGroup.group_name == group_name)
        # if not product_group_exists:
        product_group = ProductGroup(group_name=group_name)
        db.session.add(product_group)
        db.session.commit()


if __name__=="__main__":
    get_xplant_products()
