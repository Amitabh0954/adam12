from flask import Blueprint, request, jsonify
from services.user_service import UserService
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///user.db')
Session = sessionmaker(bind=engine)

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/register', methods=['POST'])
def register():
    session = Session()
    user_service = UserService(session)

    try:
        user = user_service.create_user(request.json)
        return jsonify({"id": user.id, "email": user.email}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 5. Build the main app entry and wire everything in `app.py`