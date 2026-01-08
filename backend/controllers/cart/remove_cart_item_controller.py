from flask import Blueprint, request, session, jsonify
from backend.services.cart.remove_cart_item_service import remove_product_from_cart, get_cart

remove_cart_item_bp = Blueprint('remove_cart_item', __name__)

@remove_cart_item_bp.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id: int):
    user_id = session.get('user_id')
    try:
        new_cart = remove_product_from_cart(user_id, product_id)
        return jsonify({"message": "Item removed successfully", "cart": new_cart.dict()}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500