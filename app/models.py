import os
from flask import url_for
from flask_login import UserMixin
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from markupsafe import Markup
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == "admin"

    def __repr__(self):
        return f'<User {self.id} - {self.name}>'


class ProductGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)
    image = db.Column(db.Unicode(128), nullable=True)

    def __repr__(self):
        return f'ProductGroup {self.id} - {self.group_name}'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer)
    count = db.Column(db.Integer)
    description = db.Column(db.String, nullable=True)
    image = db.Column(db.Unicode(128), nullable=True)
    productgroup_id = db.Column(
        db.Integer,
        db.ForeignKey('productgroup.id', ondelete='CASCADE'),
        nullable=True,
        index=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        nullable=True,
        index=True
    )

    productgroup = relationship('ProductGroup', backref='products')
    user = relationship('User', backref='products')

    def __repr__(self):
        return f'<Product {self.id} - {self.name}>'


cart_product = db.Table(
    "cart_product",
    db.Column("cart_id", db.Integer, db.ForeignKey("cart.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        nullable=True,
        index=True
    )

    def __repr__(self):
        return f'<Cart {self.id}>'


class ProductModelView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ""

        filename = form.thumbgen_filename(model.path)
        url = url_for('static', filename=filename)

        return Markup(f'<img src="{url}">')

    column_formatters = {"path": _list_thumbnail}

    form_extra_fields = {
        'image': form.ImageUploadField(
            'Image',
            base_path=os.path.join(os.path.dirname(__file__), 'static/img'),
            thumbnail_size=(120, 120, True),
        )
    }