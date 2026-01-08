from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.models.products.product import Product
from backend.services.products.product_service import add_product

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
def add_new_product():
    try:
        product = Product(**request.json)
        add_product(product)
        return jsonify({"message": "Product added successfully"}), 201
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500