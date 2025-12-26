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
    response = cart_service.view_cart()
    return jsonify(response), response['status']

@cart_controller.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id: int):
    response = cart_service.remove_from_cart(product_id)
    return jsonify(response), response['status']