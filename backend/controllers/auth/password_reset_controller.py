from flask import Blueprint, request, jsonify
from services.auth.password_reset_service import PasswordResetService

password_reset_controller = Blueprint('password_reset_controller', __name__)
password_reset_service = PasswordResetService()

@password_reset_controller.route('/password_reset/request', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    response = password_reset_service.request_password_reset(data)
    return jsonify(response), response['status']

@password_reset_controller.route('/password_reset/verify', methods=['POST'])
def verify_password_reset():
    data = request.get_json()
    response = password_reset_service.verify_password_reset(data)
    return jsonify(response), response['status']