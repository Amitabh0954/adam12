from flask import Flask
from .models import db
from .routes import cart_bp

def init_app(app: Flask) -> None:
    # Register blueprint
    app.register_blueprint(cart_bp, url_prefix='/cart')

    # Initialize database
    with app.app_context():
        db.create_all()
