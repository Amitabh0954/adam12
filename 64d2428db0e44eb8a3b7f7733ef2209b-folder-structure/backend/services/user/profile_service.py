# Epic Title: User Account Management

from backend.models.user.profile import UserProfile
from backend.repositories.user.profile_repository import UserProfileRepository

class UserProfileService:
    def __init__(self, profile_repository: UserProfileRepository):
        self.profile_repository = profile_repository
    
    def create_profile(self, user_id: int, first_name: str, last_name: str, phone_number: str) -> UserProfile:
        new_profile = UserProfile(user_id=user_id, first_name=first_name, last_name=last_name, phone_number=phone_number)
        self.profile_repository.add_profile(new_profile)
        return new_profile

    def update_profile(self, user_id: int, first_name: str, last_name: str, phone_number: str) -> UserProfile:
        profile = self.profile_repository.get_profile_by_user_id(user_id)
        if not profile:
            raise ValueError("Profile does not exist")
        profile.update_profile(first_name, last_name, phone_number)
        self.profile_repository.update_profile(profile)
        return profile