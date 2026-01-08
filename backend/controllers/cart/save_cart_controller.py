from flask import Blueprint, session, jsonify
from backend.services.cart.save_cart_service import save_cart_for_user, get_saved_cart_for_user

save_cart_bp = Blueprint('save_cart', __name__)

@save_cart_bp.route('/cart/save', methods=['POST'])
def save_cart():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "User must be logged in"}), 401
    try:
        save_cart_for_user(user_id)
        return jsonify({"message": "Cart saved successfully"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@save_cart_bp.route('/cart/load', methods=['GET'])
def load_cart():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "User must be logged in"}), 401
    try:
        saved_cart = get_saved_cart_for_user(user_id)
        return jsonify(saved_cart.dict()), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500