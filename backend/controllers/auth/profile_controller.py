from flask import Blueprint, request, jsonify
from services.auth.profile_service import ProfileService

profile_controller = Blueprint('profile_controller', __name__)
profile_service = ProfileService()

@profile_controller.route('/profile/update', methods=['PUT'])
def update_profile():
    data = request.get_json()
    user_id = data.get('user_id')
    name = data.get('name')
    email = data.get('email')
    response = profile_service.update_profile(user_id, name, email)
    return jsonify(response), response['status']

@profile_controller.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id: int):
    response = profile_service.get_profile(user_id)
    return jsonify(response), response['status']