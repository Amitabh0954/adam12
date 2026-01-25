from flask import Blueprint, request, jsonify
from backend.user_account_management.services.user_service import UserService
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///user.db')
Session = sessionmaker(bind=engine)

password_reset_controller = Blueprint('password_reset_controller', __name__)

@password_reset_controller.route('/reset-password-request', methods=['POST'])
def reset_password_request():
    session = Session()
    user_service = UserService(session)

    try:
        email = request.json['email']
        token = user_service.initiate_password_reset(email)
        # Here, you would send the token to the user's email in a real application
        return jsonify({"message": "Password reset token sent", "token": token}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@password_reset_controller.route('/reset-password', methods=['POST'])
def reset_password():
    session = Session()
    user_service = UserService(session)

    try:
        token = request.json['token']
        new_password = request.json['new_password']
        user_service.reset_password(token, new_password)
        return jsonify({"message": "Password has been reset"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 5. Update routes to include password reset functionality