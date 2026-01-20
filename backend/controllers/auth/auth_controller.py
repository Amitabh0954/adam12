from flask import Blueprint, request, jsonify
from services.auth.auth_service import AuthService

auth_controller = Blueprint('auth_controller', __name__)
auth_service = AuthService()

@auth_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response = auth_service.register_user(data)
    return jsonify(response), response['status']

@auth_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    response = auth_service.login_user(data)
    return jsonify(response), response['status']

@auth_controller.route('/password-reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    response = auth_service.request_password_reset(data)
    return jsonify(response), response['status']

@auth_controller.route('/password-reset/<token>', methods=['POST'])
def reset_password(token: str):
    data = request.get_json()
    response = auth_service.reset_password(data, token)
    return jsonify(response), response['status']

@auth_controller.route('/profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    response = auth_service.update_profile(data)
    return jsonify(response), response['status']
