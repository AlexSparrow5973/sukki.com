import random, requests

from bs4 import BeautifulSoup
# from app.db import db
# from app.models import News
# from app.product.parsers.utils import get_html, save_news


def get_html(url):
    """Функция преобразует html в string"""
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/106.0.0.0 Safari/537.36'
        }
    try:
        result = requests.get(url, headers=headers)
        # проверка статуса соединения, выдает exception если будут ошибки
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def get_xplant_products():
    html = get_html("https://www.xplant.co.kr/ru/shop/list.php?ca_id=1010&category=10&search_str=&item_name=Echeveria&priceRange=&min_price=0&max_price=0&sort=3&q=&page=1&is_overseas=&is_xpress=")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_products = soup.find('ul', id_='product1_content').findAll('li')
        with open('xplant.html', 'w', encoding='utf-8') as fw:
            fw.write(str(all_products[0]))
        # for product in all_products[:1]:
        #     name = product.find('a', class_='textEllipsis').get_text()
        #     price = int(product.find('span', class_='amount_color').get_text()[:-1].replace(',',''))
        #     count = random.randint(1,4)
        #     image_id = product.find('img', class_="before_load_lazy").get('data-src')
        #     # description = 
        #     try:
        #         print(f'Succulent {name}. Amount: {price} rubles. Count in stock - {count}')
        #         print(f'{image_id}')
        #     except(ValueError):
        #         print("Sorry, this succulent is not find")

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
