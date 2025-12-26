from repositories.auth.user_repository import UserRepository
from models.user import User

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register(self, data: dict):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return {"message": "Email and password are required", "status": 400}

        if self.user_repository.find_by_email(email):
            return {"message": "Email already registered", "status": 400}

        # Perform password validation here (e.g., length, complexity, etc.)

        user = User(email=email, password=password)
        self.user_repository.save(user)

        return {"message": "User registered successfully", "status": 201}