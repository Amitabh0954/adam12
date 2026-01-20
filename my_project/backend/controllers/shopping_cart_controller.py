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
    total_price = 0
    for item in cart_items:
        product = Product.query.get(item.product_id)
        item_total = product.price * item.quantity
        total_price += item_total
        response.append({
            'product_id': item.product_id,
            'product_name': product.name,
            'quantity': item.quantity,
            'item_total': item_total
        })

    return jsonify({'cart': response, 'total_price': total_price})

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

@bp.route('/remove', methods=['POST'])
def remove_from_cart():
    product_id = request.json.get('product_id')
    confirm = request.json.get('confirm', False)
    user_id = session.get('user_id')
    session_id = session.sid

    if not confirm:
        return jsonify({'error': 'Confirmation is required to remove item'}), 400

    if user_id:
        cart_item = ShoppingCart.query.filter_by(user_id=user_id, product_id=product_id).first()
    else:
        cart_item = ShoppingCart.query.filter_by(session_id=session_id, product_id=product_id).first()

    if not cart_item:
        return jsonify({'error': 'Product not in cart'}), 404

    db.session.delete(cart_item)
    db.session.commit()
    
    update_cart_total(user_id=user_id, session_id=session_id, product_id=product_id)

    return jsonify({'message': 'Product removed from cart'}), 200

def update_cart_total(user_id: int, session_id: str, product_id: int) -> None:
    if user_id:
        cart_items = ShoppingCart.query.filter_by(user_id=user_id).all()
    else:
        cart_items = ShoppingCart.query.filter_by(session_id=session_id).all()

    total_price = 0
    for item in cart_items:
        product = Product.query.get(item.product_id)
        total_price += product.price * item.quantity

    # Normally, we would store the total in session or in a cart summary table if needed.
    # For simplicity, it can be included in the response of view_cart.

@bp.route('/update_quantity', methods=['POST'])
def update_quantity():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')
    user_id = session.get('user_id')
    session_id = session.sid

    if quantity <= 0:
        return jsonify({'error': 'Quantity must be a positive integer'}), 400

    if user_id:
        cart_item = ShoppingCart.query.filter_by(user_id=user_id, product_id=product_id).first()
    else:
        cart_item = ShoppingCart.query.filter_by(session_id=session_id, product_id=product_id).first()

    if not cart_item:
        return jsonify({'error': 'Product not in cart'}), 404

    cart_item.quantity = quantity
    db.session.commit()

    return update_cart_total(user_id, session_id, product_id)

@bp.route('/save', methods=['POST'])
def save_cart():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User must be logged in to save cart state'}), 401

    session_cart_items = ShoppingCart.query.filter_by(session_id=session.sid).all()
    for item in session_cart_items:
        item.user_id = user_id
        item.session_id = None

    db.session.commit()
    return jsonify({'message': 'Cart state saved'})

@bp.route('/load', methods=['GET'])
def load_cart():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User must be logged in to load cart state'}), 401
    
    cart_items = ShoppingCart.query.filter_by(user_id=user_id).all()
    for item in cart_items:
        if not item.session_id:
            item.session_id = session.sid

    db.session.commit()
    return view_cart()

### Step 3: Ensure `app.py` is registering the updated `shopping_cart_controller` blueprint (no change needed here):