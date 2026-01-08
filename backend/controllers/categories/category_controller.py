from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.models.products.category import Category
from backend.services.categories.category_service import add_category, get_all_categories

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['POST'])
def add_new_category():
    try:
        category = Category(**request.json)
        add_category(category)
        return jsonify({"message": "Category added successfully"}), 201
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@category_bp.route('/categories', methods=['GET'])
def fetch_all_categories():
    try:
        categories = get_all_categories()
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500