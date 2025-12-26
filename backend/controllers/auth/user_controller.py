from flask import Blueprint, request, jsonify
from services.auth.user_service import UserService

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response = user_service.register(data)
    return jsonify(response), response['status']