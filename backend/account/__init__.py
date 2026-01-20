from flask import Flask
from flask_session import Session
from .models import db
from .routes import account_bp
from flask_mail import Mail
from flask_jwt_extended import JWTManager

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
    app.config['MAIL_SERVER'] = 'smtp.example.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'your-email@example.com'
    app.config['MAIL_PASSWORD'] = 'your-email-password'
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'

    db.init_app(app)
    Session(app)
    mail.init_app(app)
    jwt = JWTManager(app)
    
    app.register_blueprint(account_bp, url_prefix='/account')
    
    with app.app_context():
        db.create_all()
    
    return app
