from flask import Blueprint, render_template, request

from app.models import Product


blueprint = Blueprint('product', __name__)  # url_prefix='/product'


@blueprint.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    title = 'Sukki.com'
    products = Product.query.order_by(Product.price.desc()).paginate(page=page, per_page=24)
    return render_template('product/catalog.html', title=title, products=products)


@blueprint.route('/productcard/<int:product_id>/')
def card_of_product(product_id):
    page = request.args.get('page', 1, type=int)
    product = Product.query.get_or_404(product_id)
    return render_template('product/product_card.html', product=product, page_num=page)


@blueprint.route('/echeveria/')
def echeveria():
    echeveria = Product.query.filter(Product.scientific_name == 'Echeveria').order_by(Product.price.desc()).all()
    return render_template('echeveria.html', echeveria=echeveria)