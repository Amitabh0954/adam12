from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
from .models import User
from ..database import db_session

account_bp = Blueprint('account', __name__)

@account_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400
    
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    
    try:
        db_session.add(new_user)
        db_session.commit()
    except IntegrityError:
        db_session.rollback()
        return jsonify({"error": "Username or Email already exists"}), 400
    
    return jsonify({"message": "User registered successfully"}), 201