from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User, LoginAttempt
from .schemas import UserSchema, LoginAttemptSchema
from datetime import timedelta, datetime

account_bp = Blueprint('account', __name__)
user_schema = UserSchema()
login_attempt_schema = LoginAttemptSchema()

@account_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    email = data['email']
    password = generate_password_hash(data['password'])
    
    new_user = User(email=email, password_hash=password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return user_schema.jsonify(new_user), 201

@account_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        attempt = LoginAttempt(user_id=user.id if user else None, success=False)
        db.session.add(attempt)
        db.session.commit()
        return jsonify({'message': 'Invalid credentials'}), 401

    attempt = LoginAttempt(user_id=user.id, success=True)
    db.session.add(attempt)
    db.session.commit()
    
    session['user_id'] = user.id
    session.permanent = True
    session.modified = True

    return jsonify({'message': 'Login successful', 'user_id': user.id}), 200

@account_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200

@account_bp.before_request
def session_timeout():
    session.permanent = True
    account_bp.permanent_session_lifetime = timedelta(minutes=30)
    session.modified = True
