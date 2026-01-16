from flask import Flask
from flask_migrate import Migrate
from flask_mail import Mail
from flask_session import Session
from backend.account.models import db
from backend.account.views import account_bp, mail

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # Session timeout 30 minutes.
    app.config['MAIL_SERVER'] = 'smtp.example.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your-email@example.com'
    app.config['MAIL_PASSWORD'] = 'your-email-password'

    db.init_app(app)
    Migrate(app, db)
    Session(app)
    mail.init_app(app)

    app.register_blueprint(account_bp, url_prefix='/account')

    return app