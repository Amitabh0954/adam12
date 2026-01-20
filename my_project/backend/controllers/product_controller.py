from flask import Blueprint, request, jsonify, session
from backend.models.product_model import Product, Category, db

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/add', methods=['POST'])
def add_product():
    name = request.json.get('name')
    price = request.json.get('price')
    description = request.json.get('description')
    category_name = request.json.get('category')

    if not name or not description or not price or not category_name:
        return jsonify({'error': 'Product name, description, price, and category are required'}), 400

    if price <= 0:
        return jsonify({'error': 'Product price must be a positive number'}), 400

    if Product.query.filter_by(name=name).first():
        return jsonify({'error': 'Product name must be unique'}), 400

    category = Category.query.filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        db.session.add(category)
        db.session.commit()

    product = Product(name=name, price=price, description=description, category_id=category.id)
    db.session.add(product)
    db.session.commit()

    return jsonify({'message': 'Product added successfully'}), 201

@bp.route('/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # Assume user_role session key determines if the user is an admin or not
    user_role = session.get('user_role')
    if user_role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    data = request.json
    name = data.get('name', product.name)
    price = data.get('price', product.price)
    description = data.get('description', product.description)
    category_name = data.get('category', None)

    if not name or not description or price is None:
        return jsonify({'error': 'Product name, description, and price are required'}), 400

    if price <= 0:
        return jsonify({'error': 'Product price must be a positive number'}), 400

    # Check if updated name is already taken by another product
    if name != product.name and Product.query.filter_by(name=name).first():
        return jsonify({'error': 'Product name must be unique'}), 400

    product.name = name
    product.price = price
    product.description = description if description else product.description

    if category_name:
        category = Category.query.filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            db.session.add(category)
            db.session.commit()
        product.category_id = category.id

    db.session.commit()
    return jsonify({'message': 'Product updated successfully'}), 200

### Step 2: Update `app.py` to ensure proper session and admin check: