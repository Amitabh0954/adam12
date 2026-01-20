from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from .models import db, User
from .schemas import UserSchema

account_bp = Blueprint('account', __name__)
user_schema = UserSchema()

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
