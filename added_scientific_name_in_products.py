from app import create_app
from app.models import db, Product

app = create_app()

item_name = ['Echeveria',
        'Haworthia',
        'Agavoides',
        'Conophytum',
        'Sedum',
        'Graptoveria',
        'Crassula',
        'Lithops',
        'Graptopetalum',
        'Pachyveria',
        'Euphorbia',
        'Adromischus',
    ]

def added_scientific_name():
    with app.app_context():
        products = Product.query.all()
        for product in products:
            if "E." in product.name:
                product.scientific_name="Echeveria"
                db.session.commit()
            else:
                pass


if __name__=='__main__':
    added_scientific_name()


