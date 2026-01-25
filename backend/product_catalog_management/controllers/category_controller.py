from flask import Blueprint, request, jsonify
from backend.product_catalog_management.services.category_service import CategoryService
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///product_catalog.db')
Session = sessionmaker(bind=engine)

category_controller = Blueprint('category_controller', __name__)

@category_controller.route('/categories', methods=['POST'])
def create_category():
    session = Session()
    category_service = CategoryService(session)

    try:
        category = category_service.create_category(request.json)
        return jsonify({
            "id": category.id,
            "name": category.name,
            "parent_id": category.parent_id
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@category_controller.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    session = Session()
    category_service = CategoryService(session)

    try:
        category = category_service.update_category(category_id, request.json)
        return jsonify({
            "id": category.id,
            "name": category.name,
            "parent_id": category.parent_id
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@category_controller.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    session = Session()
    category_service = CategoryService(session)

    try:
        category_service.delete_category(category_id)
        return jsonify({"message": "Category deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 6. Update routes to include category management