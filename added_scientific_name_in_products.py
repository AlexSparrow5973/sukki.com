from app import create_app
from app.models import db, Product

app = create_app()


item_name = ['Haworthia',
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


def added_scientific_name(item_name):
    with app.app_context():
        products = Product.query.all()
        for product in products:
            print(product.name)
            for item in item_name:
                if item in product.name:
                    product.scientific_name=item
                    db.session.commit()
                    break
                    print('recorded')
                # else:
                #     pass
                    # product.scientific_name="Echeveria"
                    # db.session.commit()


if __name__=='__main__':
    added_scientific_name(item_name)
