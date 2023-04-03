from flask import Blueprint, render_template, request

from app.models import Product


blueprint = Blueprint('product', __name__)

@blueprint.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    title = 'Sukki.com'
    products = Product.query.order_by(Product.price.desc()).paginate(page=page, per_page=16)
    return render_template('product/catalog.html', title=title, products=products)
