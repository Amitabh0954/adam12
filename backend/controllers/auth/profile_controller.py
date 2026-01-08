from flask import Blueprint, request, jsonify, session
from pydantic import ValidationError
from backend.models.users.profile import ProfileUpdate
from backend.services.auth.profile_service import update_profile

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['PUT'])
def update_user_profile():
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized"}), 401
    try:
        profile_update = ProfileUpdate(**request.json)
        updated_user = update_profile(session['user_id'], profile_update)
        return jsonify(updated_user.dict()), 200
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500