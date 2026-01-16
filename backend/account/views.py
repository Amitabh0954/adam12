from flask import Blueprint, request, jsonify, session, url_for
from flask_mail import Message, Mail
from datetime import datetime
from backend.account.models import db, User, PasswordResetToken
from flask_session import Session

account_bp = Blueprint('account', __name__)
mail = Mail()

@account_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email is already in use'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username is already in use'}), 400

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@account_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    user = User.query.filter_by(email=email).first()

    if user is None or not user.check_password(password):
        return jsonify({'error': 'Invalid email or password'}), 400

    session['user_id'] = user.id

    return jsonify({'message': 'Login successful'}), 200

@account_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

@account_bp.route('/password-reset-request', methods=['POST'])
def password_reset_request():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'error': 'Email is required'}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'error': 'User not found'}), 400

    reset_token = PasswordResetToken(user=user)
    db.session.add(reset_token)
    db.session.commit()

    reset_link = url_for('account.reset_password', token=reset_token.token, _external=True)
    msg = Message('Password Reset Request', recipients=[user.email])
    msg.body = f'Please use the following link to reset your password: {reset_link}'
    mail.send(msg)

    return jsonify({'message': 'Password reset link sent to your email'}), 200

@account_bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    data = request.get_json()
    new_password = data.get('new_password')

    if not new_password:
        return jsonify({'error': 'New password is required'}), 400

    reset_token = PasswordResetToken.validate_token(token)

    if reset_token is None:
        return jsonify({'error': 'Invalid or expired token'}), 400

    user = reset_token.user
    user.password_hash = generate_password_hash(new_password)
    db.session.commit()

    return jsonify({'message': 'Password reset successful'}), 200