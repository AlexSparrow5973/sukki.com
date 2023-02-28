import os
# from flask import current_app


basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'app.db')

# PRODUCTS_IMAGE_DIR = os.path.join(basedir + '\\app\static\prod_image\\')

if __name__=="__main__":
    print(os.path.join(basedir + '\\app\static\prod_image\\'))