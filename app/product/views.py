from flask import Blueprint, render_template

from app.db import db

blueprint = Blueprint('product', __name__)

@blueprint.route('/')
def index():
    title = 'Sukki.com'
    return render_template('index.html', title=title)
