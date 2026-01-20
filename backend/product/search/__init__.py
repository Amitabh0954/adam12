from flask import Blueprint

from .routes import search_bp

def init_app(app):
    # Register blueprint
    app.register_blueprint(search_bp, url_prefix='/search')
