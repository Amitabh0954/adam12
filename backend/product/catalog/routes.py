from flask import Blueprint, request, jsonify
from .models import db, Product, Category
from .schemas import ProductSchema, CategorySchema

catalog_bp = Blueprint('catalog', __name__)
product_schema = ProductSchema()
category_schema = CategorySchema()

@catalog_bp.route('/products', methods=['POST'])
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
