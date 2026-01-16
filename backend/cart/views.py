from flask import Blueprint, request, jsonify, session
from backend.cart.models import db, Cart, CartItem
from backend.product.catalog.models import Product
from backend.account.models import User

cart_bp = Blueprint('cart', __name__)

def get_cart() -> Cart:
    user_id = session.get('user_id')
    if user_id:
        cart = Cart.query.filter_by(user_id=user_id).first()
        if cart:
            return cart
        else:
            new_cart = Cart(user_id=user_id)
            db.session.add(new_cart)
            db.session.commit()
            return new_cart
    else:
        if 'cart_id' in session:
            return Cart.query.get(session['cart_id'])
        else:
            new_cart = Cart()
            db.session.add(new_cart)
            db.session.commit()
            session['cart_id'] = new_cart.id
            return new_cart

@cart_bp.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    if not product_id:
        return jsonify({'error': 'Product ID is required'}), 400

    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404

    if quantity <= 0:
        return jsonify({'error': 'Quantity must be a positive integer'}), 400

    cart = get_cart()
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
        db.session.commit()
    else:
        new_cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        db.session.add(new_cart_item)
        db.session.commit()

    return jsonify({'message': 'Product added to cart'}), 201

@cart_bp.route('/remove-from-cart', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')

    if not product_id:
        return jsonify({'error': 'Product ID is required'}), 400

    cart = get_cart()
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item is None:
        return jsonify({'error': 'Product not found in cart'}), 404

    db.session.delete(cart_item)
    db.session.commit()

    return jsonify({'message': 'Product removed from cart'}), 200

@cart_bp.route('/modify-cart-item', methods=['POST'])
def modify_cart_item():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or quantity is None:
        return jsonify({'error': 'Product ID and quantity are required'}), 400

    if quantity <= 0:
        return jsonify({'error': 'Quantity must be a positive integer'}), 400

    cart = get_cart()
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item is None:
        return jsonify({'error': 'Product not found in cart'}), 404

    cart_item.quantity = quantity
    db.session.commit()

    return jsonify({'message': 'Product quantity updated'}), 200

@cart_bp.route('/cart-total', methods=['GET'])
def cart_total():
    cart = get_cart()
    total_price = sum(item.get_total_price() for item in cart.items)
    return jsonify({'total_price': total_price}), 200