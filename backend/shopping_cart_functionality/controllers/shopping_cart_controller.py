from flask import Blueprint, request, jsonify, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.shopping_cart_functionality.services.shopping_cart_service import ShoppingCartService

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

shopping_cart_controller = Blueprint('shopping_cart_controller', __name__)

@shopping_cart_controller.route('/cart', methods=['POST'])
def add_product_to_cart():
    session_db = Session()
    cart_service = ShoppingCartService(session_db)
    
    user_id = request.json.get('user_id')  # For authenticated users
    session_id = session.get('session_id')  # For guest users, ensuring session persists

    if not session_id:
        session_id = request.json.get('session_id')
        session['session_id'] = session_id

    product_id = request.json['product_id']
    quantity = request.json['quantity']

    cart = cart_service.create_or_get_cart(user_id=user_id, session_id=session_id)

    try:
        cart_item = cart_service.add_product_to_cart(cart, product_id, quantity)
        return jsonify({
            "cart_id": cart.id,
            "product_id": cart_item.product_id,
            "quantity": cart_item.quantity
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@shopping_cart_controller.route('/cart', methods=['GET'])
def get_cart_items():
    session_db = Session()
    cart_service = ShoppingCartService(session_db)
    
    user_id = request.args.get('user_id')  # For authenticated users
    session_id = session.get('session_id')  # For guest users

    if not session_id:
        session_id = request.args.get('session_id')
        session['session_id'] = session_id

    cart = cart_service.create_or_get_cart(user_id=user_id, session_id=session_id)

    cart_items = cart_service.get_cart_items(cart)
    return jsonify(cart_items), 200

@shopping_cart_controller.route('/cart', methods=['DELETE'])
def remove_product_from_cart():
    session_db = Session()
    cart_service = ShoppingCartService(session_db)
    
    user_id = request.json.get('user_id')  # For authenticated users
    session_id = session.get('session_id')  # For guest users

    if not session_id:
        session_id = request.json.get('session_id')
        session['session_id'] = session_id

    product_id = request.json['product_id']

    cart = cart_service.create_or_get_cart(user_id=user_id, session_id=session_id)

    confirmation = request.json.get('confirmation')
    if not confirmation or confirmation != "yes":
        return jsonify({"error": "Removal needs confirmation"}), 400

    try:
        cart_service.remove_product_from_cart(cart, product_id)
        cart_items = cart_service.get_cart_items(cart)
        return jsonify(cart_items), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@shopping_cart_controller.route('/cart/modify', methods=['PUT'])
def modify_product_quantity():
    session_db = Session()
    cart_service = ShoppingCartService(session_db)
    
    user_id = request.json.get('user_id')  # For authenticated users
    session_id = session.get('session_id')  # For guest users

    if not session_id:
        session_id = request.json.get('session_id')
        session['session_id'] = session_id

    product_id = request.json['product_id']
    quantity = request.json['quantity']

    cart = cart_service.create_or_get_cart(user_id=user_id, session_id=session_id)

    try:
        cart_item = cart_service.modify_product_quantity(cart, product_id, quantity)
        cart_items = cart_service.get_cart_items(cart)
        return jsonify(cart_items), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 3. Update routes to include the new shopping cart management endpoint for quantity modification

##### Updated Routes