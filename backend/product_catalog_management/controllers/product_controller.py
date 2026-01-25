from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.product_catalog_management.services.product_service import ProductService
from backend.product_catalog_management.schemas.product_schema import ProductSchema

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

product_controller = Blueprint('product_controller', __name__)

# Ensure admin access is checked (this is a placeholder and should be replaced with actual admin check logic)
def admin_required(f):
    def wrap(*args, **kwargs):
        # Perform actual admin check here
        # For now, assume the check passes
        return f(*args, **kwargs)
    return wrap

@product_controller.route('/products/<int:product_id>', methods=['PUT'])
@admin_required
def update_product(product_id):
    session = Session()
    product_service = ProductService(session)

    try:
        data = request.json
        product = product_service.update_product(product_id, data)
        product_schema = ProductSchema()
        return jsonify(product_schema.dump(product)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 4. Update routes to include the endpoint for updating products