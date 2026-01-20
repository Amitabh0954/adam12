from flask import Blueprint

from .models import db
from .routes import catalog_bp

def init_app(app):
    # Register blueprint
    app.register_blueprint(catalog_bp, url_prefix='/catalog')

    # Create tables
    with app.app_context():
        db.create_all()