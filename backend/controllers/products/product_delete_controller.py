from flask import Blueprint, request, jsonify
from services.products.product_delete_service import ProductDeleteService

product_delete_controller = Blueprint('product_delete_controller', __name__)
product_delete_service = ProductDeleteService()

@product_delete_controller.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int):
    response = product_delete_service.delete_product(product_id)
    return jsonify(response), response['status']