import httplib2, os

basedir = os.path.abspath(os.path.dirname(__file__))

def save_image(image_url, name):
    file = image_url.split('/')[-1]
    h = httplib2.Http('.cache')
    response, content = h.request(image_url)
    out = open(os.path.join(basedir + '\\app\static\prod_image' + name, file + '.jpg'), 'wb')
    out.write(content)
    out.close()