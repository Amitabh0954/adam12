from flask import Blueprint, request, jsonify
from services.products.product_search_service import ProductSearchService

product_search_controller = Blueprint('product_search_controller', __name__)
product_search_service = ProductSearchService()

@product_search_controller.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    response = product_search_service.search_products(query, page, per_page)
    return jsonify(response), response['status']