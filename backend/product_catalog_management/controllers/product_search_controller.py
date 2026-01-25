from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.product_catalog_management.services.product_search_service import ProductSearchService
from backend.product_catalog_management.schemas.product_schema import ProductSchema

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

product_search_controller = Blueprint('product_search_controller', __name__)

@product_search_controller.route('/search', methods=['GET'])
def search_products():
    session = Session()
    product_search_service = ProductSearchService(session)

    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    search_results = product_search_service.search_products(query, page, per_page)

    product_schema = ProductSchema(many=True)
    results = product_schema.dump(search_results['results'])

    # Highlight search terms
    for product in results:
        product['name'] = product_search_service.highlight_search_term(product['name'], query)
        product['description'] = product_search_service.highlight_search_term(product['description'], query)

    return jsonify({
        "page": search_results['page'],
        "per_page": search_results['per_page'],
        "total_results": search_results['total_results'],
        "results": results
    }), 200

#### 4. Update routes to include the new search endpoint