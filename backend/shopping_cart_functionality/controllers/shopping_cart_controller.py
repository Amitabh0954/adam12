from flask import Blueprint, request, jsonify
from backend.shopping_cart_functionality.services.shopping_cart_service import ShoppingCartService
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///shopping_cart.db')
Session = sessionmaker(bind=engine)

shopping_cart_controller = Blueprint('shopping_cart_controller', __name__)

@shopping_cart_controller.route('/cart', methods=['GET'])
def get_cart():
    session = Session()
    shopping_cart_service = ShoppingCartService(session)
    user_id = request.args.get('user_id', type=int)

    cart = shopping_cart_service.get_cart(user_id)
    cart_schema = ShoppingCartSchema()
    return jsonify(cart_schema.dump(cart))

@shopping_cart_controller.route('/cart/add', methods=['POST'])
def add_to_cart():
    session = Session()
    shopping_cart_service = ShoppingCartService(session)
    user_id = request.json.get('user_id')

    try:
        cart = shopping_cart_service.add_item_to_cart(user_id, request.json)
        cart_schema = ShoppingCartSchema()
        return jsonify(cart_schema.dump(cart)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@shopping_cart_controller.route('/cart/remove', methods=['DELETE'])
def remove_from_cart():
    session = Session()
    shopping_cart_service = ShoppingCartService(session)
    user_id = request.json.get('user_id')
    product_id = request.json.get('product_id')

    try:
        cart = shopping_cart_service.remove_item_from_cart(user_id, product_id)
        cart_schema = ShoppingCartSchema()
        return jsonify(cart_schema.dump(cart)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 4. Ensure routes are updated to include the new functionality