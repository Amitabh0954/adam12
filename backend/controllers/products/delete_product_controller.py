from flask import Blueprint, request, jsonify
from backend.services.products.delete_product_service import delete_product

delete_product_bp = Blueprint('delete_product', __name__)

@delete_product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_existing_product(product_id: int):
    try:
        if 'user_id' not in session or not session.get('is_admin'):
            return jsonify({"message": "Unauthorized"}), 401
        delete_product(product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500