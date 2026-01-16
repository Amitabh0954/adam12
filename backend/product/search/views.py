from flask import Blueprint, request, jsonify
from backend.product.catalog.models import Product
from sqlalchemy import or_

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    search = '%{}%'.format(query)
    products = Product.query.filter(
        or_(
            Product.name.ilike(search),
            Product.description.ilike(search),
            Product.category.ilike(search)
        ),
        Product.is_deleted.is_(False)
    ).paginate(page, per_page, False)

    result = []
    for product in products.items:
        result.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': highlight_query(product.description, query),
            'category': highlight_query(product.category, query)
        })

    return jsonify({
        'products': result,
        'page': products.page,
        'total_pages': products.pages,
        'total_items': products.total
    }), 200

def highlight_query(text: str, query: str) -> str:
    if not text:
        return ''
    return text.replace(query, f'<em>{query}</em>')