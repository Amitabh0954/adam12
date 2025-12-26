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