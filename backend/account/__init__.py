from flask import Flask
from flask_session import Session
from .models import db
from .routes import account_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
    
    db.init_app(app)
    Session(app)
    
    app.register_blueprint(account_bp, url_prefix='/account')
    
    with app.app_context():
        db.create_all()
    
    return app
