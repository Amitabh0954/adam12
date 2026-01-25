from backend.user_account_management.models.user import User
from backend.user_account_management.schemas.user_schema import UserSchema
from backend.user_account_management.schemas.login_schema import LoginSchema
from backend.user_account_management.schemas.password_reset_schema import PasswordResetRequestSchema, PasswordResetSchema
from backend.user_account_management.schemas.profile_update_schema import ProfileUpdateSchema
from sqlalchemy.orm import Session
from marshmallow import ValidationError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
import secrets

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

    def initiate_password_reset(self, email: str) -> str:
        user = self.session.query(User).filter_by(email=email).first()
        if not user:
            raise ValueError("User not found")

        user.reset_token = secrets.token_urlsafe()
        user.reset_token_expires_at = datetime.utcnow() + timedelta(hours=24)
        self.session.commit()
        return user.reset_token

    def reset_password(self, token: str, new_password: str):
        user = self.session.query(User).filter_by(reset_token=token).first()
        if not user or user.reset_token_expires_at < datetime.utcnow():
            raise ValueError("Invalid or expired token")

        user.password = generate_password_hash(new_password)
        user.reset_token = None
        user.reset_token_expires_at = None
        self.session.commit()

    def update_profile(self, user_id: int, data: dict) -> User:
        try:
            update_data = ProfileUpdateSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        user = self.session.query(User).filter_by(id=user_id).first()
        if not user:
            raise ValueError("User not found")

        for key, value in update_data.items():
            setattr(user, key, value)

        self.session.commit()
        return user

#### 4. Implement profile management controller