from flask import Blueprint, request, jsonify
from services.auth.login_service import LoginService

login_controller = Blueprint('login_controller', __name__)
login_service = LoginService()

@login_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    response = login_service.login(email, password)
    return jsonify(response), response['status']

@login_controller.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    user_id = data.get('user_id')
    response = login_service.logout(user_id)
    return jsonify(response), response['status']