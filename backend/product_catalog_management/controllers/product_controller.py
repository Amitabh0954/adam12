from flask import Blueprint, request, jsonify
from backend.product_catalog_management.services.product_service import ProductService
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///product_catalog.db')
Session = sessionmaker(bind=engine)

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/add-product', methods=['POST'])
def add_product():
    session = Session()
    product_service = ProductService(session)

    try:
        product = product_service.add_product(request.json)
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@product_controller.route('/update-product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    session = Session()
    product_service = ProductService(session)

    try:
        product = product_service.update_product(product_id, request.json)
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@product_controller.route('/delete-product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    session = Session()
    product_service = ProductService(session)
    user_id = request.json.get('user_id')

    try:
        product_service.delete_product(user_id, product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except PermissionError as e:
        return jsonify({"error": str(e)}), 403
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@product_controller.route('/search-products', methods=['GET'])
def search_products():
    session = Session()
    product_service = ProductService(session)
    try:
        query_params = request.args.to_dict()
        products = product_service.search_products(query_params)
        return jsonify([{
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        } for product in products]), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 5. Update routes to include product search