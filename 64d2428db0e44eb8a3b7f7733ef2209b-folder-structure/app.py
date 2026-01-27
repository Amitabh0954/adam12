# Epic Title: User Account Management

from flask import Flask, request, jsonify, session
from backend.repositories.user.user_repository import UserRepository
from backend.services.user.user_service import UserService
from backend.repositories.user.session_repository import SessionRepository
from backend.services.user.session_service import SessionService

app = Flask(__name__)

user_repository = UserRepository()
user_service = UserService(user_repository)
session_repository = SessionRepository()
session_service = SessionService(session_repository, user_repository)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    user = user_service.register_user(email, password)
    return jsonify(user_id=user.user_id, email=user.email), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    # Authenticate user here and create a session
    user = user_repository.get_user_by_email(email)
    if user and user.hashed_password == user_service._hash_password(password):  # Example auth logic
        session_obj = session_service.create_session(user.user_id)
        return jsonify(session_id=session_obj.session_id), 200
    return jsonify(message="Invalid credentials"), 401

@app.route('/validate-session', methods=['POST'])
def validate_session():
    data = request.json
    session_id = data.get('session_id')
    timeout = data.get('timeout', 30)  # timeout in minutes, default to 30
    if session_service.validate_session(session_id, timeout):
        return jsonify(message="Session valid"), 200
    return jsonify(message="Session expired or invalid"), 401

if __name__ == '__main__':
    app.run(debug=True)