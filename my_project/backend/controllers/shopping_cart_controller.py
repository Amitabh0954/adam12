from flask import Blueprint, request, jsonify, session
from backend.models.shopping_cart_model import ShoppingCart, db
from backend.models.product_model import Product

bp = Blueprint('shopping_cart', __name__, url_prefix='/shopping_cart')

@bp.route('/', methods=['GET'])
def view_cart():
    user_id = session.get('user_id')
    session_id = session.sid

    if user_id:
        cart_items = ShoppingCart.query.filter_by(user_id=user_id).all()
    else:
        cart_items = ShoppingCart.query.filter_by(session_id=session_id).all()

    response = []
    for item in cart_items:
        product = Product.query.get(item.product_id)
        response.append({
            'product_id': item.product_id,
            'product_name': product.name,
            'quantity': item.quantity
        })

    return jsonify({'cart': response})

@bp.route('/add', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)
    user_id = session.get('user_id')
    session_id = session.sid

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    if user_id:
        cart_item = ShoppingCart.query.filter_by(user_id=user_id, product_id=product_id).first()
    else:
        cart_item = ShoppingCart.query.filter_by(session_id=session_id, product_id=product_id).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = ShoppingCart(user_id=user_id, session_id=session_id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()
    return jsonify({'message': 'Product added to cart'}), 201

### Step 3: Update `app.py` to register the `shopping_cart_controller` blueprint: