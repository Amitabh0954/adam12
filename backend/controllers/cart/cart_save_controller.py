from flask import Blueprint, request, jsonify
from services.cart.cart_save_service import CartSaveService

cart_save_controller = Blueprint('cart_save_controller', __name__)
cart_save_service = CartSaveService()

@cart_save_controller.route('/cart/save', methods=['POST'])
def save_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    response = cart_save_service.save_cart(user_id)
    return jsonify(response), response['status']

@cart_save_controller.route('/cart/retrieve', methods=['GET'])
def retrieve_cart():
    user_id = request.args.get('user_id')
    response = cart_save_service.retrieve_cart(user_id)
    return jsonify(response), response['status']