# Epic Title: User Account Management

from backend.models.user.user import User
from backend.repositories.user.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def register_user(self, email: str, password: str) -> User:
        # Logic to meet security criteria
        hashed_password = self._hash_password(password)
        new_user = User(user_id=0, email=email, hashed_password=hashed_password)  # Example ID management
        self.user_repository.add_user(new_user)
        return new_user
    
    def _hash_password(self, password: str) -> str:
        # logic to hash password according to security criteria
        pass