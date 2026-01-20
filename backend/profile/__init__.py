from flask import Blueprint

from .models import db
from .routes import profile_bp

def init_app(app):
    # Register blueprint
    app.register_blueprint(profile_bp, url_prefix='/profile')

    # Create tables
    with app.app_context():
        db.create_all()
