from flask import Blueprint, request, jsonify
from .models import db, Product, Category
from .schemas import ProductSchema, CategorySchema, UpdateProductSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

catalog_bp = Blueprint('catalog', __name__)
product_schema = ProductSchema()
update_product_schema = UpdateProductSchema()
category_schema = CategorySchema()

@catalog_bp.route('/products', methods=['POST'])
@jwt_required()
def add_product():
    data = request.get_json()
    errors = product_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    new_product = Product(
        name=data['name'],
        price=data['price'],
        description=data['description']
    )

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product), 201

@catalog_bp.route('/categories', methods=['POST'])
@jwt_required()
def add_category():
    data = request.get_json()
    errors = category_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    new_category = Category(
        name=data['name'],
        product_id=data['product_id']
    )

    db.session.add(new_category)
    db.session.commit()

    return category_schema.jsonify(new_category), 201

@catalog_bp.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id: int):
    data = request.get_json()
    errors = update_product_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400

    product = Product.query.get_or_404(product_id)

    name = data.get('name', product.name)
    price = data.get('price', product.price)
    description = data.get('description', product.description)

    if data.get('name'):
        product.name = name
    if data.get('price'):
        product.price = price
    if data.get('description'):
        product.description = description

    db.session.commit()

    return product_schema.jsonify(product), 200
