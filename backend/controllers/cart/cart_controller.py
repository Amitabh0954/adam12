from flask import Blueprint, request, jsonify
from services.cart.cart_service import CartService

cart_controller = Blueprint('cart_controller', __name__)
cart_service = CartService()

@cart_controller.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    response = cart_service.add_to_cart(user_id, product_id, quantity)
    return jsonify(response), response['status']

@cart_controller.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id: int):
    response = cart_service.get_cart(user_id)
    return jsonify(response), response['status']

@cart_controller.route('/cart', methods=['DELETE'])
def remove_from_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    response = cart_service.remove_from_cart(user_id, product_id)
    return jsonify(response), response['status']

@cart_controller.route('/cart', methods=['PUT'])
def modify_cart_quantity():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    response = cart_service.modify_cart_quantity(user_id, product_id, quantity)
    return jsonify(response), response['status']