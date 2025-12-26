from flask import Blueprint, request, jsonify
from services.products.product_service import ProductService

product_controller = Blueprint('product_controller', __name__)
product_service = ProductService()

@product_controller.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_id = data.get('category_id')
    response = product_service.add_product(name, description, price, category_id)
    return jsonify(response), response['status']

@product_controller.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id: int):
    data = request.get_json()
    name = data.get('name', None)
    description = data.get('description', None)
    price = data.get('price', None)
    response = product_service.update_product(product_id, name, description, price)
    return jsonify(response), response['status']

@product_controller.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int):
    response = product_service.delete_product(product_id)
    return jsonify(response), response['status']