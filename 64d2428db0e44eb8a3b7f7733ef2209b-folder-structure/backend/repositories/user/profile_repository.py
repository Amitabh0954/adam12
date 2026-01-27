# Epic Title: User Account Management

from backend.models.user.profile import UserProfile
from typing import Optional

class UserProfileRepository:
    def __init__(self):
        # Initialize database connection here
        pass
    
    def add_profile(self, profile: UserProfile) -> None:
        # logic to add user profile to the database
        pass
    
    def get_profile_by_user_id(self, user_id: int) -> Optional<UserProfile]:
        # logic to retrieve a user profile by user_id
        pass
    
    def update_profile(self, profile: UserProfile) -> None:
        # logic to update the user profile in the database
        pass