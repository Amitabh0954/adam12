from typing import Optional
from backend.models.users.user_login import UserLogin
from backend.repositories.users.user_repository import UserRepository

user_repository = UserRepository()

def login_user(user_login: UserLogin) -> Optional[User]:
    user = user_repository.get_by_email(user_login.email)
    if user and user.password == user_login.password:
        return user
    return None