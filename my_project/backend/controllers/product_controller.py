from flask import Blueprint, request, jsonify
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

### Step 3: Update the database schema to include the new tables: