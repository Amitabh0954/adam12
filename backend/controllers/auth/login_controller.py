from flask import Blueprint, request, jsonify
from datetime import datetime
from backend.services.auth.authentication_service import AuthenticationService
from backend.repositories.users.user_repository import UserRepository
from backend.repositories.users.session_repository import SessionRepository

login_bp = Blueprint('login', __name__)
user_repository = UserRepository()
session_repository = SessionRepository()
authentication_service = AuthenticationService(user_repository, session_repository)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    session = authentication_service.login_user(email, password)

    if session is None:
        return jsonify({'error': 'Invalid email or password'}), 401

    return jsonify({'session_id': session.id, 'expires_at': session.expires_at}), 200