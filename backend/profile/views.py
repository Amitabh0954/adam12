from flask import Blueprint, request, jsonify, session
from backend.profile.models import db, Profile

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/update', methods=['POST'])
def update_profile():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    user_id = session['user_id']

    profile = Profile.query.filter_by(user_id=user_id).first()

    if not profile:
        profile = Profile(user_id=user_id)

    profile.first_name = data.get('first_name', profile.first_name)
    profile.last_name = data.get('last_name', profile.last_name)
    profile.preferences = data.get('preferences', profile.preferences)

    db.session.add(profile)
    db.session.commit()

    return jsonify({'message': 'Profile updated successfully'}), 200