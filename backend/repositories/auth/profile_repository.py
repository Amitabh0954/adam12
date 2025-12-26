from models.profile import Profile
from typing import Optional

class ProfileRepository:
    def __init__(self):
        self.profiles = []

    def find_by_user_id(self, user_id: str) -> Optional[Profile]:
        return next((profile for profile in self.profiles if profile.user_id == user_id), None)

    def save(self, profile: Profile) -> None:
        self.profiles = [profile if profile.user_id == p.user_id else p for p in self.profiles]

    def update(self, user_id: str, data: dict) -> Optional[Profile]:
        profile = self.find_by_user_id(user_id)
        if profile:
            profile.name = data.get('name', profile.name)
            profile.email = data.get('email', profile.email)
            profile.preferences = data.get('preferences', profile.preferences)
            profile.updated_at = datetime.utcnow()
            self.save(profile)
            return profile
        return None