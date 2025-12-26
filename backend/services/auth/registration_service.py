from repositories.auth.user_repository import UserRepository
from models.user import User

class RegistrationService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register(self, email: str, password: str):
        if not email or not password:
            return {"message": "Email and password are required", "status": 400}

        if self.user_repository.find_by_email(email):
            return {"message": "Email is already registered", "status": 400}

        if len(password) < 8:  # Example password security criteria
            return {"message": "Password must be at least 8 characters long", "status": 400}

        user = User(id=None, email=email, password=password)
        self.user_repository.save(user)

        return {"message": "User registered successfully", "status": 201, "user": {"id": user.id, "email": user.email}}