from sqlalchemy.orm import Session
from backend.user_account_management.models.user import User
from backend.user_account_management.schemas.user_schema import UserSchema
from backend.user_account_management.services.password_service import PasswordService
from marshmallow import ValidationError

class RegistrationService:
    def __init__(self, session: Session):
        self.session = session
        self.password_service = PasswordService()

    def register_user(self, user_data: dict) -> User:
        try:
            valid_data = UserSchema().load(user_data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        existing_user = self.session.query(User).filter_by(email=valid_data['email']).first()
        if existing_user:
            raise ValueError("Email already registered")

        hashed_password = self.password_service.hash_password(valid_data['password'])
        new_user = User(email=valid_data['email'], hashed_password=hashed_password)
        self.session.add(new_user)
        self.session.commit()
        return new_user

#### 4. Implement registration controller to expose API for user registration