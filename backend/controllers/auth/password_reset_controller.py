from flask import Blueprint, request, jsonify
from services.auth.password_reset_service import PasswordResetService

password_reset_controller = Blueprint('password_reset_controller', __name__)
password_reset_service = PasswordResetService()

@password_reset_controller.route('/password_reset/request', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')
    response = password_reset_service.request_password_reset(email)
    return jsonify(response), response['status']

@password_reset_controller.route('/password_reset/confirm', methods=['POST'])
def confirm_password_reset():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')
    response = password_reset_service.confirm_password_reset(token, new_password)
    return jsonify(response), response['status']