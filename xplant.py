import requests

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
    html = get_html("https://www.xplant.co.kr/shop/list.php?ca_id=10&category=10&search_str=&item_name=Echeveria&min_price=&max_price=&sort=0&q=&page=1&is_overseas=false&is_xpress=false")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_products = soup.find('ul', class_='item_list').findAll('li', class_='itemTd')
        print(all_products[0])
        # with open('xplant.html', 'w', encoding='utf-8') as fw:
        #     writer = fw.write()
        #     for row in writer:
        #         writerow



        # for product in all_products:
        #     product_img_url = product.find()
        #     product_text = product.find('a', class_="tm-article-snippet__title-link")



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
