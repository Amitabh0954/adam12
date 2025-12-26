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