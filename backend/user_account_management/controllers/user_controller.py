from flask import Blueprint, request, jsonify
from backend.user_account_management.services.user_service import UserService
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

@user_controller.route('/login', methods=['POST'])
def login():
    session = Session()
    user_service = UserService(session)

    try:
        user = user_service.login_user(request.json)
        return jsonify({"id": user.id, "email": user.email}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 5. Update routes to include login functionality