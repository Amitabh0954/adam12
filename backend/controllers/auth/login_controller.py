from flask import Blueprint, request, jsonify, session
from pydantic import ValidationError
from backend.models.users.user import UserLogin
from backend.services.auth.login_service import login_user

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    try:
        user_login = UserLogin(**request.json)
        user = login_user(user_login)
        if user:
            session['user_id'] = user.id
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500