from flask import Blueprint, request, jsonify, session
from backend.models.user_model import User, db

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email is already registered'}), 400

    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()

    if user is None or not user.check_password(password):
        if user:
            user.login_attempts += 1
            db.session.commit()
        return jsonify({'error': 'Invalid email or password'}), 400

    if user.login_attempts >= 5:
        return jsonify({'error': 'Account locked. Too many failed login attempts'}), 403

    session['user_id'] = user.id
    session.permanent = True  # Set session to use permanent lifetime

    user.login_attempts = 0
    db.session.commit()

    return jsonify({'message': 'Login successful'}), 200