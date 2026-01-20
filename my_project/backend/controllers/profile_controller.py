from flask import Blueprint, request, jsonify, session
from backend.models.user_model import User, db

bp = Blueprint('profile', __name__, url_prefix='/profile')

@bp.route('/update', methods=['PUT'])
def update_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    user.email = data.get('email', user.email)

    # Add additional profile fields as needed
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.preferences = data.get('preferences', user.preferences)

    db.session.commit()
    return jsonify({'message': 'Profile updated successfully'}), 200

### Step 2: Update `user_model.py`: