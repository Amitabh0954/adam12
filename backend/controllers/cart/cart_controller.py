from flask import Blueprint, request, jsonify, session
from services.cart.cart_service import CartService

cart_controller = Blueprint('cart_controller', __name__)
cart_service = CartService()

@cart_controller.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = session.get('user_id')
    response = cart_service.add_to_cart(user_id, data)
    return jsonify(response), response['status']

@cart_controller.route('/cart', methods=['GET'])
def view_cart():
    user_id = session.get('user_id')
    response = cart_service.view_cart(user_id)
    return jsonify(response), response['status']

@cart_controller.route('/cart', methods=['DELETE'])
def remove_from_cart():
    data = request.get_json()
    user_id = session.get('user_id')
    response = cart_service.remove_from_cart(user_id, data)
    return jsonify(response), response['status']

@cart_controller.route('/cart', methods=['PUT'])
def update_cart_item():
    data = request.get_json()
    user_id = session.get('user_id')
    response = cart_service.update_cart_item(user_id, data)
    return jsonify(response), response['status']

@cart_controller.route('/cart/save', methods=['POST'])
def save_cart():
    user_id = session.get('user_id')
    response = cart_service.save_cart(user_id)
    return jsonify(response), response['status']