from flask import Blueprint, request, jsonify
from services.user.user_service import UserService

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    response = user_service.update_profile(data)
    return jsonify(response), response['status']