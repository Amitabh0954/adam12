from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.user_account_management.services.password_reset_service import PasswordResetService

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

password_reset_controller = Blueprint('password_reset_controller', __name__)

@password_reset_controller.route('/password-reset', methods=['POST'])
def generate_reset_token():
    session = Session()
    password_reset_service = PasswordResetService(session)

    try:
        email = request.json['email']
        token = password_reset_service.generate_reset_token(email)
        return jsonify({"message": "Password reset token sent"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@password_reset_controller.route('/password-reset/<token>', methods=['POST'])
def reset_password(token):
    session = Session()
    password_reset_service = PasswordResetService(session)

    try:
        new_password = request.json['new_password']
        password_reset_service.reset_password(token, new_password)
        return jsonify({"message": "Password has been reset"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 4. Update routes to include the new password reset endpoint

##### Updated Routes