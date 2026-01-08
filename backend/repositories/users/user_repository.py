import logging
from typing import Optional
from backend.models.users.user import User

class UserRepository:
    def __init__(self):
        self.users = []

    def get_by_email(self, email: str) -> Optional[User]:
        for user in self.users:
            if user.email == email:
                return user
        return None

    def save(self, user: User):
        self.users.append(user)
        logging.info(f"User with email {user.email} saved successfully.")