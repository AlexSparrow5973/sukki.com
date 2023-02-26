import httplib2, os, random, requests
from bs4 import BeautifulSoup
# from app.db import db
# from app.models import News
# from app.product.parsers.utils import get_html, save_news

basedir = os.path.abspath(os.path.dirname(__file__))
prod_image_dir = '\\app\static\prod_image\\'


def save_image(image_url, name):
    file = image_url.split('/')[-1]
    h = httplib2.Http('.cache')
    response, content = h.request(image_url)
    try:
        os.mkdir(basedir + prod_image_dir + name, mode=0o777, dir_fd=None)
    except(FileExistsError):
        pass
    out = open(os.path.join(basedir + prod_image_dir + name, file + '.jpg'), 'wb')
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
        result.raise_for_status()  # проверка статуса соединения, выдает exception если будут ошибки
        # print(result.url)
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
            soup = BeautifulSoup(html, 'html.parser')
            all_products = soup.find('ul', id="product1_content").find_all('li', limit=100)
            for product in all_products:
                name = product.find('p', class_='pd_title').get_text().rstrip().title()
                price = float(product.find('span', class_='amount_color').get_text().replace(',','')[:-1])
                count = random.randint(1,4)
                image_url = product.find('img', class_='product_img_radius').get('data-original')
                save_image(image_url, scientific_name)
                # description = 
                try:
                    print(f'Succulent name - {name}. Amount: {price} rubles. Count in stock - {count}')
                    print(f'{image_url}')
                except(ValueError):
                    print("Sorry, this succulent is not find")

'''
            title = news_item.find('span').text
            url = "https://habr.com" + news_item['href']
            published = news.find('time')['title']
            try:
                published = datetime.strptime(published, '%Y-%m-%d, %H:%M')
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)
'''


# def get_habr_content_news():
#     news_without_text = News.query.filter(News.text.is_(None))
#     for news in news_without_text:
#         html = get_html(news.url)
#         if html:
#             soup = BeautifulSoup(html, "html.parser")
#             news_content = soup.find('div', class_="article-formatted-body").decode_contents()
#             if news_content:
#                 news.text = news_content
#                 db.session.add(news)
#                 db.session.commit()

if __name__=="__main__":
    get_xplant_products()
