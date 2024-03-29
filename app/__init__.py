from flask import Flask
from flask_migrate import Migrate

from app.db import db
from app.models import db
from app.product.views import blueprint as prod_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(prod_blueprint)

    return app
