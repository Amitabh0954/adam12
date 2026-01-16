from flask import Blueprint, request, jsonify, session
from backend.cart.models import db, Cart, CartItem
from backend.product.catalog.models import Product

cart_bp = Blueprint('cart', __name__)

def get_cart() -> Cart:
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