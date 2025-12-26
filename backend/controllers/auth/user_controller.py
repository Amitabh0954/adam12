from flask import Blueprint, request, jsonify
from services.auth.user_service import UserService

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    response = user_service.register(email, password)
    return jsonify(response), response['status']

@user_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    response = user_service.login(email, password)
    return jsonify(response), response['status']

@user_controller.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    email = data.get('email')
    response = user_service.forgot_password(email)
    return jsonify(response), response['status']

@user_controller.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')
    response = user_service.reset_password(token, new_password)
    return jsonify(response), response['status']

@user_controller.route('/update-profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    user_id = data.get('user_id')
    email = data.get('email', None)
    new_password = data.get('new_password', None)
    response = user_service.update_profile(user_id, email, new_password)
    return jsonify(response), response['status']