from flask import Blueprint, request, jsonify
from backend.product.catalog.models import db, Product

catalog_bp = Blueprint('catalog', __name__)

def is_admin() -> bool:
    # Placeholder function to check if the current user is an admin
    # Replace with actual admin validation logic
    return True

@catalog_bp.route('/add-product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    category = data.get('category', '')

    if not name or not description or price is None:
        return jsonify({'error': 'Missing required fields'}), 400

    if Product.query.filter_by(name=name).first():
        return jsonify({'error': 'Product name is already in use'}), 400

    if price <= 0:
        return jsonify({'error': 'Product price must be a positive number'}), 400

    new_product = Product(name=name, price=price, description=description, category=category)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product added successfully'}), 201

@catalog_bp.route('/update-product/<int:product_id>', methods=['PUT'])
def update_product(product_id: int):
    if not is_admin():
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    price = data.get('price')
    description = data.get('description')
    category = data.get('category', '')

    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404

    if price is not None:
        try:
            price = float(price)
            if price <= 0:
                return jsonify({'error': 'Product price must be a positive number'}), 400
            product.price = price
        except ValueError:
            return jsonify({'error': 'Product price must be numeric'}), 400

    if description:
        product.description = description

    if category:
        product.category = category

    db.session.commit()

    return jsonify({'message': 'Product updated successfully'}), 200