import csv, httplib2, os

basedir = os.path.abspath(os.path.dirname(__file__))


def reading_csv_file():
    fieldnames = ['name', 'price', 'count', 'file_name']
    with open('products.csv', 'r', encoding='UTF8') as f:
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=';')
        next(reader)
        for row in reader:
            image_loading(row['file_name'])


def image_loading(file_name):
    image_url = 'https://webp2.xplant.co.kr/data/thumb/item/600x600-2/' + file_name
    h = httplib2.Http('.cache')
    response, content = h.request(image_url)
    out = open(os.path.join(basedir + '\\app\static\prod_image\\', file_name + '.jpg'), 'wb')
    out.write(content)
    out.close()


if __name__=="__main__":
    reading_csv_file()