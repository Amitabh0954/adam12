from backend.user_account_management.models.user import User
from backend.user_account_management.schemas.user_schema import UserSchema
from backend.user_account_management.schemas.login_schema import LoginSchema
from sqlalchemy.orm import Session
from marshmallow import ValidationError
from werkzeug.security import check_password_hash
from datetime import datetime

class UserService:
    MAX_INVALID_ATTEMPTS = 5
    
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, data: dict) -> User:
        try:
            user_data = UserSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        new_user = User(**user_data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def login_user(self, data: dict) -> User:
        try:
            login_data = LoginSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        user = self.session.query(User).filter_by(email=login_data['email']).first()
        if not user:
            raise ValueError("User not found")

        if user.login_attempts >= self.MAX_INVALID_ATTEMPTS:
            raise ValueError("Account locked due to too many invalid login attempts")

        if not check_password_hash(user.password, login_data['password']):
            user.login_attempts += 1
            self.session.commit()
            raise ValueError("Invalid password")

        user.login_attempts = 0
        user.last_login = datetime.utcnow()
        self.session.commit()
        return user

#### 4. Implement login controller