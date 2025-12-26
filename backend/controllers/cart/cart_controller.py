from flask import Blueprint, request, jsonify
from services.cart.cart_service import CartService

cart_controller = Blueprint('cart_controller', __name__)
cart_service = CartService()

@cart_controller.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    response = cart_service.add_to_cart(data)
    return jsonify(response), response['status']

@cart_controller.route('/cart', methods=['GET'])
def view_cart():
    user_id = request.args.get('user_id', type=int)
    response = cart_service.view_cart(user_id)
    return jsonify(response), response['status']

@cart_controller.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id: int):
    user_id = request.args.get('user_id', type=int)
    response = cart_service.remove_from_cart(user_id, product_id)
    return jsonify(response), response['status']

@cart_controller.route('/cart/<int:product_id>', methods=['PUT'])
def modify_quantity(product_id: int):
    user_id = request.args.get('user_id', type=int)
    quantity = request.args.get('quantity', type=int)
    response = cart_service.modify_quantity(user_id, product_id, quantity)
    return jsonify(response), response['status']