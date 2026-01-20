from flask import Flask, session
from backend.models import db
from backend.controllers import user_controller
from flask_session import Session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minutes

db.init_app(app)
Session(app)
app.register_blueprint(user_controller.bp)

if __name__ == '__main__':
    app.run(debug=True)