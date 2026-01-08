from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.models.users.user import User
from backend.services.auth.registration_service import register_user

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/register', methods=['POST'])
def register():
    try:
        user = User(**request.json)
        register_user(user)
        return jsonify({"message": "User registered successfully"}), 201
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500