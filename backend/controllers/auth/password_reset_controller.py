from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.models.users.password_reset import PasswordResetRequest, PasswordResetConfirm
from backend.services.auth.password_reset_service import request_password_reset, confirm_password_reset

password_reset_bp = Blueprint('password_reset', __name__)

@password_reset_bp.route('/password-reset', methods=['POST'])
def password_reset():
    try:
        reset_request = PasswordResetRequest(**request.json)
        request_password_reset(reset_request)
        return jsonify({"message": "Password reset link sent"}), 200
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@password_reset_bp.route('/password-reset/confirm', methods=['POST'])
def password_reset_confirm():
    try:
        reset_confirm = PasswordResetConfirm(**request.json)
        confirm_password_reset(reset_confirm)
        return jsonify({"message": "Password has been reset"}), 200
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500