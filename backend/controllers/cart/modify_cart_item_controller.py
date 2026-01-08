from flask import Blueprint, request, session, jsonify
from backend.services.cart.modify_cart_item_service import modify_product_quantity_in_cart

modify_cart_item_bp = Blueprint('modify_cart_item', __name__)

@modify_cart_item_bp.route('/cart/<int:product_id>', methods=['PUT'])
def modify_cart_item(product_id: int):
    user_id = session.get('user_id')
    try:
        quantity = request.json.get('quantity')
        if quantity is None or quantity <= 0:
            return jsonify({"message": "Quantity must be a positive integer"}), 400
        updated_cart = modify_product_quantity_in_cart(user_id, product_id, quantity)
        return jsonify({"message": "Cart updated successfully", "cart": updated_cart.dict()}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500