from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a strong secret key
jwt = JWTManager(app)

from .account.views import account_bp
app.register_blueprint(account_bp, url_prefix='/account')

from .database import init_db
init_db()

# Blockchain Authentication Feature
from blockchain_auth import BlockchainAuth

blockchain_auth = BlockchainAuth()
app.config['BLOCKCHAIN_AUTH_KEY'] = 'your_blockchain_auth_key'  # Change this to a strong blockchain auth key
blockchain_auth.init_app(app)
