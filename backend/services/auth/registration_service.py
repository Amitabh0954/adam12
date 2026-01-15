from hashlib import sha256
from typing import Optional
from backend.models.users.user import User
from backend.repositories.users.user_repository import UserRepository

class RegistrationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, email: str, password: str) -> Optional[User]:
        if self.user_repository.get_user_by_email(email) is not None:
            return None

        hashed_password = sha256(password.encode()).hexdigest()
        user = User(id=len(self.user_repository.users) + 1, email=email, password_hash=hashed_password)
        return self.user_repository.create_user(user)