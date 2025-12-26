from flask import Blueprint, request, jsonify, session
from services.auth.auth_service import AuthService

auth_controller = Blueprint('auth_controller', __name__)
auth_service = AuthService()

@auth_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    response = auth_service.login(data)
    if response['status'] == 200:
        session['user_id'] = response['user']['id']
    return jsonify(response), response['status']