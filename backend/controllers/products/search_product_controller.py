from flask import Blueprint, request, jsonify
from backend.services.products.search_product_service import search_products

search_product_bp = Blueprint('search_product', __name__)

@search_product_bp.route('/search', methods=['GET'])
def search_for_products():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    try:
        results = search_products(query, page, page_size)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500