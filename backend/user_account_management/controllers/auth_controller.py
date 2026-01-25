from flask import Blueprint, request, jsonify
from backend.user_account_management.services.auth_service import AuthService
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

auth_controller = Blueprint('auth_controller', __name__)

@auth_controller.route('/login', methods=['POST'])
def login():
    session = Session()
    auth_service = AuthService(session)

    email = request.json.get('email')
    password = request.json.get('password')

    try:
        session_token = auth_service.authenticate_user(email, password)
        return jsonify({"session_token": session_token}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@auth_controller.route('/validate-session', methods=['POST'])
def validate_session():
    session = Session()
    auth_service = AuthService(session)

    session_token = request.json.get('session_token')

    is_valid = auth_service.validate_session(session_token)
    return jsonify({"is_valid": is_valid}), 200

#### 5. Update routes to include the new login and session management endpoint