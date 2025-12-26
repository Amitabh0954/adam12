from flask import Blueprint, request, jsonify
from services.cart.cart_remove_service import CartRemoveService

cart_remove_controller = Blueprint('cart_remove_controller', __name__)
cart_remove_service = CartRemoveService()

@cart_remove_controller.route('/cart', methods=['DELETE'])
def remove_from_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    response = cart_remove_service.remove_from_cart(user_id, product_id)
    return jsonify(response), response['status']