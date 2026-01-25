from flask import Blueprint, request, jsonify
from backend.user_account_management.services.user_service import UserService
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///user.db')
Session = sessionmaker(bind=engine)

profile_controller = Blueprint('profile_controller', __name__)

@profile_controller.route('/update-profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    session = Session()
    user_service = UserService(session)

    try:
        user = user_service.update_profile(user_id, request.json)
        return jsonify({
            "id": user.id, 
            "email": user.email, 
            "first_name": user.first_name, 
            "last_name": user.last_name, 
            "phone_number": user.phone_number, 
            "address": user.address
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 5. Update routes to include profile management functionality