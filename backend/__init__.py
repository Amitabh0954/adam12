from flask import Flask
from flask_migrate import Migrate
from backend.account.models import db
from backend.account.views import account_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(account_bp, url_prefix='/account')

    return app