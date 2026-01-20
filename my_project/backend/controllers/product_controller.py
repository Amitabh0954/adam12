from flask import Blueprint, request, jsonify, session
from backend.models.product_model import Product, Category, db
from sqlalchemy import or_

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/add', methods=['POST'])
def add_product():
    name = request.json.get('name')
    price = request.json.get('price')
    description = request.json.get('description')
    category_name = request.json.get('category')

    if not name or not description or not price or not category_name:
        return jsonify({'error': 'Product name, description, price, and category are required'}), 400

    if price <= 0:
        return jsonify({'error': 'Product price must be a positive number'}), 400

    if Product.query.filter_by(name=name).first():
        return jsonify({'error': 'Product name must be unique'}), 400

    category = Category.query.filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        db.session.add(category)
        db.session.commit()

    product = Product(name=name, price=price, description=description, category_id=category.id)
    db.session.add(product)
    db.session.commit()

    return jsonify({'message': 'Product added successfully'}), 201

@bp.route('/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    user_role = session.get('user_role')
    if user_role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    product = Product.query.get(product_id)
    if not product or product.deleted:
        return jsonify({'error': 'Product not found'}), 404

    data = request.json
    name = data.get('name', product.name)
    price = data.get('price', product.price)
    description = data.get('description', product.description)
    category_name = data.get('category', None)

    if not name or not description or price is None:
        return jsonify({'error': 'Product name, description, and price are required'}), 400

    if price <= 0:
        return jsonify({'error': 'Product price must be a positive number'}), 400

    if name != product.name and Product.query.filter_by(name=name).first():
        return jsonify({'error': 'Product name must be unique'}), 400

    product.name = name
    product.price = price
    product.description = description if description else product.description

    if category_name:
        category = Category.query.filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            db.session.add(category)
            db.session.commit()
        product.category_id = category.id

    db.session.commit()
    return jsonify({'message': 'Product updated successfully'}), 200

@bp.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    user_role = session.get('user_role')
    if user_role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    product = Product.query.get(product_id)
    if not product or product.deleted:
        return jsonify({'error': 'Product not found'}), 404

    confirm = request.json.get('confirm', False)
    if not confirm:
        return jsonify({'error': 'Confirmation is required'}), 400

    product.deleted = True
    db.session.commit()

    return jsonify({'message': 'Product deleted successfully'}), 200

@bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Search products by name, description, or category name
    results = Product.query.filter(
        Product.deleted == False,
        or_(
            Product.name.ilike(f'%{query}%'),
            Product.description.ilike(f'%{query}%'),
            Category.name.ilike(f'%{query}%')
        )
    ).join(Category).paginate(page=page, per_page=per_page, error_out=False)

    # Highlight the search terms in results
    def highlight(term, text):
        return text.replace(term, f'<strong>{term}</strong>')

    products = [
        {
            'id': product.id,
            'name': highlight(query, product.name),
            'price': product.price,
            'description': highlight(query, product.description),
            'category': highlight(query, product.category.name) 
        } for product in results.items
    ]

    return jsonify({
        'products': products,
        'total': results.total,
        'pages': results.pages,
        'current_page': results.page
    })

### Step 2: Update `app.py` to register the `product_controller` blueprint (no change needed here):