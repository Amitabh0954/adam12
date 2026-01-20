from flask import Blueprint, request, jsonify, session
from backend.models.category_model import Category, db

bp = Blueprint('categories', __name__, url_prefix='/categories')

@bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{
        'id': category.id,
        'name': category.name,
        'parent_id': category.parent_id
    } for category in categories])

@bp.route('/add', methods=['POST'])
def add_category():
    user_role = session.get('user_role')
    if user_role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    name = request.json.get('name')
    parent_id = request.json.get('parent_id')

    if not name:
        return jsonify({'error': 'Category name is required'}), 400

    if Category.query.filter_by(name=name).first():
        return jsonify({'error': 'Category name must be unique'}), 400

    category = Category(name=name, parent_id=parent_id)
    db.session.add(category)
    db.session.commit()

    return jsonify({'message': 'Category added successfully'}), 201

@bp.route('/update/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    user_role = session.get('user_role')
    if user_role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404

    data = request.json
    name = data.get('name', category.name)
    parent_id = data.get('parent_id', category.parent_id)

    if not name:
        return jsonify({'error': 'Category name is required'}), 400

    if name != category.name and Category.query.filter_by(name=name).first():
        return jsonify({'error': 'Category name must be unique'}), 400

    category.name = name
    category.parent_id = parent_id
    db.session.commit()

    return jsonify({'message': 'Category updated successfully'}), 200

@bp.route('/delete/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    user_role = session.get('user_role')
    if user_role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404

    db.session.delete(category)
    db.session.commit()

    return jsonify({'message': 'Category deleted successfully'}), 200

### Step 3: Ensure `Product` model uses category relationships from the updated `Category` model: