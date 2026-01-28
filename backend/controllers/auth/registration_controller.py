from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models.user import User
from db import db


registration_bp = Blueprint('registration_bp', __name__)


@registration_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    if User.query.filter_by(email=data['email']).first() is not None:
        return jsonify({'message': 'User with that email already exists.'}), 409

    new_user = User(
        email=data['email'],
        password=generate_password_hash(data['password'], method='sha256')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registered successfully!'}), 201
