from hashlib import sha256
from typing import Optional
import uuid
from backend.models.users.user import User
from backend.repositories.users.user_repository import UserRepository

class RegistrationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, email: str, password: str) -> Optional[User]:
        if self.user_repository.get_user_by_email(email) is not None:
            return None

        hashed_password = sha256(password.encode()).hexdigest()
        verification_token = str(uuid.uuid4())
        user = User(
            id=len(self.user_repository.users) + 1,
            email=email,
            password_hash=hashed_password,
            is_verified=False,
            verification_token=verification_token
        )
        created_user = self.user_repository.create_user(user)
        self.send_verification_email(created_user)
        return created_user

    def send_verification_email(self, user: User):
        # In a real system, this would send an actual email.
        # For now, we'll just simulate the process.
        print(f"Verification email sent to {user.email} with token {user.verification_token}")

    def verify_email(self, token: str) -> bool:
        user = self.user_repository.get_user_by_verification_token(token)
        if user:
            user.is_verified = True
            user.verification_token = None
            self.user_repository.update_user(user)
            return True
        return False