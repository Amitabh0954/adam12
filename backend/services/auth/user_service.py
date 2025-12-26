from repositories.auth.user_repository import UserRepository
from models.user import User
from typing import Optional
import re

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register(self, email: str, password: str):
        if not email or not password:
            return {"message": "Email and password are required", "status": 400}
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return {"message": "Invalid email format", "status": 400}
        
        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password):
            return {
                "message": "Password must be at least 8 characters long, contain at least one number and one uppercase letter",
                "status": 400
            }

        if self.user_repository.find_by_email(email):
            return {"message": "Email is already registered", "status": 400}

        user = User(id=None, email=email, password=password)
        self.user_repository.save(user)
        return {"message": "User registered successfully", "status": 201, "user": {"id": user.id, "email": user.email}}

    def login(self, email: str, password: str):
        user = self.user_repository.find_by_email(email)
        if not user:
            return {"message": "Invalid email or password", "status": 400}
        
        if user.is_locked:
            return {"message": "Account locked due to multiple failed login attempts", "status": 403}

        if user.password != password:
            user.login_attempts += 1
            if user.login_attempts >= 5:
                user.is_locked = True
            self.user_repository.save(user)
            return {"message": "Invalid email or password", "status": 400}

        user.login_attempts = 0
        self.user_repository.save(user)
        return {"message": "Login successful", "status": 200, "user": {"id": user.id, "email": user.email}}