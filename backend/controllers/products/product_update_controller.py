from flask import Blueprint, request, jsonify
from services.products.product_update_service import ProductUpdateService

product_update_controller = Blueprint('product_update_controller', __name__)
product_update_service = ProductUpdateService()

@product_update_controller.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id: int):
    data = request.get_json()
    response = product_update_service.update_product(product_id, data)
    return jsonify(response), response['status']