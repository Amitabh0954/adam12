from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.models.products.product import ProductUpdate
from backend.services.products.update_product_service import update_product

update_product_bp = Blueprint('update_product', __name__)

@update_product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_existing_product(product_id: int):
    try:
        product_update = ProductUpdate(**request.json)
        updated_product = update_product(product_id, product_update)
        return jsonify(updated_product.dict()), 200
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500