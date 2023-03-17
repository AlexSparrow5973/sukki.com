import random
from bs4 import BeautifulSoup
from utils import get_html, save_csv_file


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
    products_list = []
    for scientific_name in item_name:
        html = get_html("https://m.xplant.co.kr/shop/list.php", scientific_name)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            all_products = soup.find('ul', id="product1_content").find_all('li', limit=100)
            for product in all_products:
                name = product.find('p', class_='pd_title').get_text().rstrip().title()
                price = float(product.find('span', class_='amount_color').get_text().replace(',','')[:-1])
                count = random.randint(1,4)
                file_name = product.find('img', class_='product_img_radius').get('data-original').split('/')[-1]
                product_dict = {'name': name, 'price': price, 'count': count, 'file_name': file_name}
                products_list.append(product_dict)
    save_csv_file(products_list)


if __name__=="__main__":
    get_xplant_products()
