# Epic Title: Product Catalog Management

from flask import Flask, request, jsonify
from backend.repositories.user.user_repository import UserRepository
from backend.services.user.user_service import UserService
from backend.repositories.user.session_repository import SessionRepository
from backend.services.user.session_service import SessionService
from backend.repositories.user.password_reset_repository import PasswordResetRepository
from backend.services.user.password_reset_service import PasswordResetService
from backend.repositories.user.profile_repository import UserProfileRepository
from backend.services.user.profile_service import UserProfileService
from backend.repositories.product.product_repository import ProductRepository
from backend.services.product.product_service import ProductService
from backend.services.product.admin_product_service import AdminProductService
from backend.services.product.admin_delete_product_service import AdminDeleteProductService
from backend.services.product.search_product_service import SearchProductService
from backend.repositories.product.category_repository import CategoryRepository

app = Flask(__name__)

user_repository = UserRepository()
user_service = UserService(user_repository)
session_repository = SessionRepository()
session_service = SessionService(session_repository, user_repository)
password_reset_repository = PasswordResetRepository()
password_reset_service = PasswordResetService(password_reset_repository, user_repository)
profile_repository = UserProfileRepository()
profile_service = UserProfileService(profile_repository)
product_repository = ProductRepository()
product_service = ProductService(product_repository)
admin_product_service = AdminProductService(product_repository)
delete_product_service = AdminDeleteProductService(product_repository)
search_product_service = SearchProductService(product_repository)
category_repository = CategoryRepository()

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    user = user_service.register_user(email, password)
    return jsonify(user_id=user.user_id, email=user.email), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    user = user_repository.get_user_by_email(email)
    if user and user.hashed_password == user_service._hash_password(password):  # Example auth logic
        session_obj = session_service.create_session(user.user_id)
        return jsonify(session_id=session_obj.session_id), 200
    return jsonify(message="Invalid credentials"), 401

@app.route('/validate-session', methods=['POST'])
def validate_session():
    data = request.json
    session_id = data.get('session_id')
    timeout = data.get('timeout', 30)  # timeout in minutes, default to 30
    if session_service.validate_session(session_id, timeout):
        return jsonify(message="Session valid"), 200
    return jsonify(message="Session expired or invalid"), 401

@app.route('/request-password-reset', methods=['POST'])
def request_password_reset():
    data = request.json
    email = data.get('email')
    reset_request = password_reset_service.create_password_reset_request(email)
    return jsonify(request_id=reset_request.request_id), 200

@app.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.json
    request_id = data.get('request_id')
    new_password = data.get('new_password')
    try:
        password_reset_service.reset_password(request_id, new_password)
        return jsonify(message="Password reset successful"), 200
    except ValueError as e:
        return jsonify(message=str(e)), 400

@app.route('/profile', methods=['GET'])
def get_profile():
    user_id = request.args.get('user_id')
    profile = profile_repository.get_profile_by_user_id(int(user_id))
    if profile:
        return jsonify(user_id=profile.user_id, first_name=profile.first_name, last_name=profile.last_name, phone_number=profile.phone_number), 200
    return jsonify(message="Profile not found"), 404

@app.route('/profile', methods=['POST'])
def create_profile():
    data = request.json
    user_id = data.get('user_id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone_number = data.get('phone_number')
    profile = profile_service.create_profile(user_id, first_name, last_name, phone_number)
    return jsonify(user_id=profile.user_id, first_name=profile.first_name, last_name=profile.last_name, phone_number=profile.phone_number), 201

@app.route('/profile', methods=['PUT'])
def update_profile():
    data = request.json
    user_id = data.get('user_id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone_number = data.get('phone_number')
    profile = profile_service.update_profile(user_id, first_name, last_name, phone_number)
    return jsonify(user_id=profile.user_id, first_name=profile.first_name, last_name=profile.last_name, phone_number=profile.phone_number), 200

@app.route('/product', methods=['POST'])
def add_product():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    try:
        product = product_service.add_new_product(name, description, price)
        return jsonify(product_id=product.product_id, name=product.name, description=product.description, price=product.price), 201
    except ValueError as e:
        return jsonify(message=str(e)), 400

@app.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    try:
        product = admin_product_service.update_product(product_id, name, description, price)
        return jsonify(product_id=product.product_id, name=product.name, description=product.description, price=product.price), 200
    except ValueError as e:
        return jsonify(message=str(e)), 400

@app.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        success = delete_product_service.delete_product(product_id)
        if success:
            return jsonify(message="Product deleted successfully"), 200
    except ValueError as e:
        return jsonify(message=str(e)), 400

@app.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 10, type=int)
    results = search_product_service.search_products(query, page, page_size)
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)