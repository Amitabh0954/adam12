from backend.models.users.user import User
from backend.repositories.users.user_repository import UserRepository

user_repository = UserRepository()

def register_user(user: User):
    existing_user = user_repository.get_by_email(user.email)
    if existing_user:
        raise ValueError("Email must be unique")
    user_repository.save(user)