from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.user_account_management.services.auth_service import AuthService

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

auth_controller = Blueprint('auth_controller', __name__)

@auth_controller.route('/login', methods=['POST'])
def login_user():
    session = Session()
    auth_service = AuthService(session)

    try:
        email = request.json['email']
        password = request.json['password']
        user_session = auth_service.login_user(email, password)
        return jsonify({"session_token": user_session.session_token}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@auth_controller.route('/validate-session', methods=['POST'])
def validate_session():
    session = Session()
    auth_service = AuthService(session)

    session_token = request.json['session_token']
    
    is_valid = auth_service.validate_session(session_token)
    if is_valid:
        return jsonify({"status": "Session is valid"}), 200
    else:
        return jsonify({"error": "Session is invalid"}), 401

#### 4. Update routes to include the new user login endpoint