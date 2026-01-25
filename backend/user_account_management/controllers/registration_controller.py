from flask import Blueprint, request, jsonify
from backend.user_account_management.services.registration_service import RegistrationService
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

registration_controller = Blueprint('registration_controller', __name__)

@registration_controller.route('/register', methods=['POST'])
def register():
    session = Session()
    registration_service = RegistrationService(session)

    try:
        user = registration_service.register_user(request.json)
        return jsonify({"id": user.id, "email": user.email, "created_at": user.created_at}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 5. Update routes to include the new registration endpoint