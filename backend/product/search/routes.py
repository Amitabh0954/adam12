from flask import Blueprint, request, jsonify
from .models import SearchQuery
from .schemas import PageSchema
from flask_jwt_extended import jwt_required

search_bp = Blueprint('search', __name__)
page_schema = PageSchema()

@search_bp.route('/products', methods=['GET'])
def search_products():
    query = request.args.get('q', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    if not query:
        return jsonify({'message': 'Search query is required'}), 400

    result = SearchQuery.search_products(query, page, per_page)
    result_dict = {
        'total': result.total,
        'pages': result.pages,
        'page': result.page,
        'per_page': result.per_page,
        'items': result.items
    }

    return page_schema.jsonify(result_dict), 200
