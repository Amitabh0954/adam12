from repositories.auth.user_repository import UserRepository

class ProfileService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_profile(self, user_id: int):
        user = self.user_repository.find_by_id(user_id)
        if not user:
            return {"message": "User not found", "status": 404}
        return {"message": "User profile retrieved successfully", "status": 200, "user": {"id": user.id, "name": user.name, "email": user.email}}

    def update_profile(self, user_id: int, name: str, email: str):
        user = self.user_repository.find_by_id(user_id)
        if not user:
            return {"message": "User not found", "status": 404}

        if email and self.user_repository.find_by_email(email) and self.user_repository.find_by_email(email).id != user_id:
            return {"message": "Email is already registered", "status": 400}

        user.name = name if name else user.name
        user.email = email if email else user.email
        self.user_repository.save(user)
        return {"message": "User profile updated successfully", "status": 200}