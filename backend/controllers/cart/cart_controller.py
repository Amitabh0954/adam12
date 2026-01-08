from flask import Blueprint, request, session, jsonify
from pydantic import ValidationError
from backend.models.cart.shopping_cart import ShoppingCart
from backend.models.cart.cart_item import CartItem
from backend.services.cart.cart_service import add_product_to_cart, get_cart, save_cart

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['GET'])
def fetch_cart():
    user_id = session.get('user_id')
    cart = get_cart(user_id)
    return jsonify(cart.dict()), 200

@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    user_id = session.get('user_id')
    try:
        cart_item = CartItem(**request.json)
        cart = add_product_to_cart(user_id, cart_item)
        save_cart(cart)
        return jsonify(cart.dict()), 200
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500