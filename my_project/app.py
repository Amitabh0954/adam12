from flask import Flask
from backend.models import db
from backend.controllers import user_controller

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(user_controller.bp)

if __name__ == '__main__':
    app.run(debug=True)