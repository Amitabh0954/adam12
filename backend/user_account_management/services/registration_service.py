from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash
from backend.user_account_management.models.user import User
from marshmallow import ValidationError
from backend.user_account_management.schemas.user_registration_schema import UserRegistrationSchema

class RegistrationService:
    def __init__(self, session: Session):
        self.session = session

    def register_user(self, data: dict) -> User:
        try:
            valid_data = UserRegistrationSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        if self.session.query(User).filter_by(email=valid_data['email']).first():
            raise ValueError("Email already exists")

        hashed_password = generate_password_hash(valid_data['password'])
        user = User(
            email=valid_data['email'],
            password=hashed_password,
            first_name=valid_data.get('first_name'),
            last_name=valid_data.get('last_name')
        )
        
        self.session.add(user)
        self.session.commit()
        return user

##### User Registration Schema