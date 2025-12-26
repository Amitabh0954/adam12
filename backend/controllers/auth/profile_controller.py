from flask import Blueprint, request, jsonify, session
from services.auth.profile_service import ProfileService

profile_controller = Blueprint('profile_controller', __name__)
profile_service = ProfileService()

@profile_controller.route('/profile', methods=['GET'])
def get_profile():
    user_id = session.get('user_id')
    response = profile_service.get_profile(user_id)
    return jsonify(response), response['status']

@profile_controller.route('/profile', methods=['PUT'])
def update_profile():
    user_id = session.get('user_id')
    data = request.get_json()
    response = profile_service.update_profile(user_id, data)
    return jsonify(response), response['status']