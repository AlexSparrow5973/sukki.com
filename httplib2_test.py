import httplib2, os

basedir = os.path.abspath(os.path.dirname(__file__))

url = "https://webp2.xplant.co.kr/data/thumb/item/280x300-2/1676737441"
file = url.split('/')[-1]

h = httplib2.Http('.cache')
response, content = h.request(url)
out = open(os.path.join(basedir + '\\app\static\prod_image', file + '.jpg'), 'wb')
out.write(content)
out.close()