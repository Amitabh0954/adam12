from typing import Dict
from backend.models.users.profile import ProfileUpdate
from backend.repositories.users.user_repository import UserRepository

user_repository = UserRepository()

def update_profile(user_id: int, profile_update: ProfileUpdate) -> Dict:
    user = user_repository.get_by_id(user_id)
    if not user:
        raise ValueError("User not found")

    if profile_update.email:
        existing_user = user_repository.get_by_email(profile_update.email)
        if existing_user and existing_user.id != user_id:
            raise ValueError("Email must be unique")

    user.email = profile_update.email
    if profile_update.password:
        user.password = profile_update.password
    user.first_name = profile_update.first_name
    user.last_name = profile_update.last_name

    user_repository.save(user)
    return user.dict()