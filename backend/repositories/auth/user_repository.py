from models.user import User
from typing import Optional, List

class UserRepository:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def find_all(self) -> List[User]:
        return self.users

    def find_by_id(self, user_id: int) -> Optional[User]:
        return next((user for user in self.users if user.id == user_id), None)

    def find_by_email(self, email: str) -> Optional[User]:
        return next((user for user in self.users if user.email == email), None)

    def save(self, user: User) -> None:
        if user.id is None:
            user.id = self.next_id
            self.next_id += 1
            self.users.append(user)
        else:
            self.users = [user if user.id == u.id else u for u in self.users]