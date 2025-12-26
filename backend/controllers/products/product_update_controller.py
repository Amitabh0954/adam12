from flask import Blueprint, request, jsonify
from services.products.product_update_service import ProductUpdateService

product_update_controller = Blueprint('product_update_controller', __name__)
product_update_service = ProductUpdateService()

@product_update_controller.route('/products/<int:id>', methods=['PUT'])
def update_product(id: int):
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    response = product_update_service.update_product(id, name, price, description)
    return jsonify(response), response['status']