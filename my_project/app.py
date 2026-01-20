from flask import Flask, session
from backend.models import db
from backend.controllers import user_controller, password_reset_controller
from flask_session import Session
from flask_mail import Mail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minutes

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@example.com'

db.init_app(app)
Session(app)
mail = Mail(app)

app.register_blueprint(user_controller.bp)
app.register_blueprint(password_reset_controller.bp)

if __name__ == '__main__':
    app.run(debug=True)