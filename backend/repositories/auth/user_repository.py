from models.user import User
from typing import Optional

class UserRepository:
    def __init__(self):
        self.users = [
            # Example users
            User(id=1, name="John Doe", email="john.doe@example.com"),
            User(id=2, name="Jane Smith", email="jane.smith@example.com")
        ]

    def find_by_id(self, user_id: int) -> Optional[User]:
        return next((user for user in self.users if user.id == user_id), None)

    def save(self, user: User) -> None:
        self.users = [user if user.id == u.id else u for u in self.users]