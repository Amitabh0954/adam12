from flask import Blueprint, request, jsonify
from services.products.category_service import CategoryService

category_controller = Blueprint('category_controller', __name__)
category_service = CategoryService()

@category_controller.route('/categories', methods=['POST'])
def add_category():
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')
    response = category_service.add_category(name, parent_id)
    return jsonify(response), response['status']

@category_controller.route('/categories', methods=['GET'])
def get_categories():
    response = category_service.get_categories()
    return jsonify(response), response['status']