from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.user_account_management.services.user_service import UserService
from backend.user_account_management.schemas.user_schema import UserSchema

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/register', methods=['POST'])
def register_user():
    session = Session()
    user_service = UserService(session)

    try:
        user = user_service.register_user(request.json)
        user_schema = UserSchema()
        return jsonify(user_schema.dump(user)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

##### User Schema