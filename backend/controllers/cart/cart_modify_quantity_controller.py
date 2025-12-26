from flask import Blueprint, request, jsonify
from services.cart.cart_modify_quantity_service import CartModifyQuantityService

cart_modify_quantity_controller = Blueprint('cart_modify_quantity_controller', __name__)
cart_modify_quantity_service = CartModifyQuantityService()

@cart_modify_quantity_controller.route('/cart/modify', methods=['PUT'])
def modify_quantity():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    response = cart_modify_quantity_service.modify_quantity(user_id, product_id, quantity)
    return jsonify(response), response['status']