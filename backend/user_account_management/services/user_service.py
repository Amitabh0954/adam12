from sqlalchemy.orm import Session
from backend.user_account_management.models.user import User
from backend.user_account_management.schemas.user_schema import UserSchema
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash
import re

class UserService:
    def __init__(self, session: Session):
        self.session = session

    def register_user(self, data: dict) -> User:
        try:
            valid_data = UserSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        if not self.is_secure_password(valid_data['password']):
            raise ValueError("Password does not meet security criteria")

        existing_user = self.session.query(User).filter_by(email=valid_data['email']).first()
        if existing_user:
            raise ValueError("Email already exists")

        hashed_password = generate_password_hash(valid_data['password'])
        new_user = User(email=valid_data['email'], password=hashed_password)
        self.session.add(new_user)
        self.session.commit()

        return new_user

    @staticmethod
    def is_secure_password(password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[!@#$%^&*]", password):
            return False
        return True

#### 3. Implement a controller to expose the API for user registration

##### UserController