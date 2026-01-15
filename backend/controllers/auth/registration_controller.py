from flask import Blueprint, request, jsonify
from backend.services.auth.registration_service import RegistrationService
from backend.repositories.users.user_repository import UserRepository

registration_bp = Blueprint('registration', __name__)
user_repository = UserRepository()
registration_service = RegistrationService(user_repository)

@registration_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = registration_service.register_user(email, password)

    if user is None:
        return jsonify({'error': 'Email already exists'}), 400

    return jsonify({'id': user.id, 'email': user.email, 'created_at': user.created_at}), 201