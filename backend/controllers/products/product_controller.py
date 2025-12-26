from flask import Blueprint, request, jsonify
from services.products.product_service import ProductService

product_controller = Blueprint('product_controller', __name__)
product_service = ProductService()

@product_controller.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    response = product_service.add_product(data)
    return jsonify(response), response['status']

@product_controller.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id: int):
    response = product_service.get_product(product_id)
    return jsonify(response), response['status']

@product_controller.route('/products', methods=['GET'])
def get_all_products():
    response = product_service.get_all_products()
    return jsonify(response), response['status']