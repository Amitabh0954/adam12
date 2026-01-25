from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.user_account_management.services.profile_service import ProfileService
from backend.user_account_management.schemas.user_schema import UserSchema

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

profile_controller = Blueprint('profile_controller', __name__)

@profile_controller.route('/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    session = Session()
    profile_service = ProfileService(session)
    
    try:
        data = request.json
        user = profile_service.update_profile(user_id, data)
        user_schema = UserSchema()
        return jsonify(user_schema.dump(user)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 4. Update routes to include the profile management endpoint

##### Updated Routes