from flask import Blueprint, request, jsonify
from .models import db, Profile
from .schemas import ProfileSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.account.models import User

profile_bp = Blueprint('profile', __name__)
profile_schema = ProfileSchema()

@profile_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_profile(user_id: int):
    profile = Profile.query.filter_by(user_id=user_id).first()
    if profile is None:
        return jsonify({'message': 'Profile not found'}), 404
    return profile_schema.jsonify(profile), 200

@profile_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_profile(user_id: int):
    user = User.query.get_or_404(user_id)

    if user.id != get_jwt_identity():
        return jsonify({'message': 'Permission denied'}), 403

    profile = Profile.query.filter_by(user_id=user_id).first()
    if profile is None:
        return jsonify({'message': 'Profile not found'}), 404

    data = request.get_json()
    errors = profile_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400
    
    profile.first_name = data.get('first_name', profile.first_name)
    profile.last_name = data.get('last_name', profile.last_name)
    profile.preferences = data.get('preferences', profile.preferences)
    
    db.session.commit()
    
    return profile_schema.jsonify(profile), 200

