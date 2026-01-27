from typing import Optional
from backend.models.users.user import User

class UserRepository:
    def __init__(self):
        self.users = []

    def create_user(self, user: User) -> User:
        self.users.append(user)
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        return next((user for user in self.users if user.email == email), None)

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(email)
        if user and user.check_password(password):
            return user
        return None

    def login(self, email: str, password: str) -> Optional[User]:
        return self.authenticate_user(email, password)
