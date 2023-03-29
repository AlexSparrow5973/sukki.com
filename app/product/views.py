from flask import Blueprint, render_template

from app.models import Product


blueprint = Blueprint('product', __name__)

@blueprint.route('/')
def index():
    title = 'Sukki.com'
    product_list = Product.query.all()
    return render_template('product/catalog.html', title=title, product_list=product_list)
