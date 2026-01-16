from flask import Blueprint, request, jsonify
from backend.product.catalog.models import db, Product

catalog_bp = Blueprint('catalog', __name__)

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