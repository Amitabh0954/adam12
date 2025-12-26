from flask import Blueprint, request, jsonify
from services.user.user_service import UserService

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/user/<int:user_id>/cart', methods=['POST'])
def save_cart_state(user_id: int):
    data = request.get_json()
    response = user_service.save_cart_state(user_id, data)
    return jsonify(response), response['status']

@user_controller.route('/user/<int:user_id>/cart', methods=['GET'])
def retrieve_cart_state(user_id: int):
    response = user_service.retrieve_cart_state(user_id)
    return jsonify(response), response['status']