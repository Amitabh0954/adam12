from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import User, db

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not all(key in data for key in ('username', 'password', 'email')): 
        return jsonify({'error': 'Missing required fields'}), 400
    username = data['username']
    password = data['password']
    email = data['email']

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, email=email)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201
