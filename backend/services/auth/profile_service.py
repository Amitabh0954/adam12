from repositories.auth.profile_repository import ProfileRepository
from models.profile import Profile

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()

    def get_profile(self, user_id: str):
        if not user_id:
            return {"message": "User is not logged in", "status": 401}

        profile = self.profile_repository.find_by_user_id(user_id)
        if not profile:
            return {"message": "Profile not found", "status": 404}

        return {"message": "Profile retrieved successfully", "status": 200, "profile": profile.__dict__}

    def update_profile(self, user_id: str, data: dict):
        if not user_id:
            return {"message": "User is not logged in", "status": 401}

        profile = self.profile_repository.update(user_id, data)
        if not profile:
            return {"message": "Profile not found", "status": 404}

        return {"message": "Profile updated successfully", "status": 200, "profile": profile.__dict__}