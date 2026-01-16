from flask import Blueprint, request, jsonify
from backend.product.catalog.models import db, Product, Category
from sqlalchemy import or_

catalog_bp = Blueprint('catalog', __name__)

def is_admin() -> bool:
    return True

@catalog_bp.route('/add-product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    category_id = data.get('category_id')

    if not name or not description or price is None or not category_id:
        return jsonify({'error': 'Missing required fields'}), 400

    if Product.query.filter_by(name=name).first():
        return jsonify({'error': 'Product name is already in use'}), 400

    if price <= 0:
        return jsonify({'error': 'Product price must be a positive number'}), 400

    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Invalid category_id'}), 400

    new_product = Product(name=name, price=price, description=description, category_id=category_id)
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
    category_id = data.get('category_id', None)

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

    if category_id:
        category = Category.query.get(category_id)
        if not category:
            return jsonify({'error': 'Invalid category_id'}), 400
        product.category_id = category_id

    db.session.commit()

    return jsonify({'message': 'Product updated successfully'}), 200

@catalog_bp.route('/delete-product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int):
    if not is_admin():
        return jsonify({'error': 'Unauthorized'}), 403

    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404

    product.is_deleted = True
    db.session.commit()

    return jsonify({'message': 'Product deleted successfully'}), 200

@catalog_bp.route('/add-category', methods=['POST'])
def add_category():
    if not is_admin():
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        return jsonify({'error': 'Category name is required'}), 400

    if Category.query.filter_by(name=name).first():
        return jsonify({'error': 'Category name is already in use'}), 400

    if parent_id:
        parent_category = Category.query.get(parent_id)
        if not parent_category:
            return jsonify({'error': 'Invalid parent_id'}), 400

    new_category = Category(name=name, parent_id=parent_id)
    db.session.add(new_category)
    db.session.commit()

    return jsonify({'message': 'Category added successfully'}), 201

@catalog_bp.route('/update-category/<int:category_id>', methods=['PUT'])
def update_category(category_id: int):
    if not is_admin():
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    category = Category.query.get(category_id)
    if category is None:
        return jsonify({'error': 'Category not found'}), 404

    if name:
        if Category.query.filter(Category.id != category.id, Category.name == name).first():
            return jsonify({'error': 'Category name is already in use'}), 400
        category.name = name

    if parent_id:
        parent_category = Category.query.get(parent_id)
        if not parent_category:
            return jsonify({'error': 'Invalid parent_id'}), 400
        category.parent_id = parent_id

    db.session.commit()

    return jsonify({'message': 'Category updated successfully'}), 200