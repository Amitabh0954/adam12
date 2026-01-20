from flask import Blueprint, request, jsonify
from .models import db, Cart, CartItem
from .schemas import CartSchema, CartItemSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

cart_bp = Blueprint('cart', __name__)
cart_schema = CartSchema()
cart_item_schema = CartItemSchema()

@cart_bp.route('/cart', methods=['GET'])
@jwt_required(optional=True)
def get_cart():
    user_id = get_jwt_identity()
    if user_id:
        cart = Cart.query.filter_by(user_id=user_id).first()
    else:
        cart_id = request.cookies.get('cart_id')
        cart = Cart.query.get(cart_id)

    if not cart:
        return jsonify({'message': 'Cart not found'}), 404

    return cart_schema.jsonify(cart), 200

@cart_bp.route('/cart', methods=['POST'])
@jwt_required(optional=True)
def add_to_cart():
    data = request.get_json()
    errors = cart_item_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    user_id = get_jwt_identity()
    if user_id:
        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart:
            cart = Cart(user_id=user_id)
            db.session.add(cart)
            db.session.commit()
    else {
        cart_id = request.cookies.get('cart_id')
        if cart_id:
            cart = Cart.query.get(cart_id)
        else:
            cart = Cart()
            db.session.add(cart)
            db.session.commit()

    existing_item = CartItem.query.filter_by(cart_id=cart.id, product_id=data['product_id']).first()
    if existing_item:
        existing_item.quantity += data['quantity']
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=data['product_id'], quantity=data['quantity'])
        db.session.add(cart_item)

    db.session.commit()

    response = jsonify({'message': 'Product added to cart', 'cart': cart_schema.dump(cart)})
    if not user_id:
        response.set_cookie('cart_id', str(cart.id))

    return response, 201
