import csv, requests


def save_csv_file(products_list):
    fieldnames = ['name', 'price', 'count', 'file_name']
    with open('products.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(products_list)


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