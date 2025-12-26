from flask import Blueprint, request, jsonify
from services.auth.registration_service import RegistrationService

registration_controller = Blueprint('registration_controller', __name__)
registration_service = RegistrationService()

@registration_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    response = registration_service.register(email, password)
    return jsonify(response), response['status']