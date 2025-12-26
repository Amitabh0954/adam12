from repositories.auth.user_repository import UserRepository
from models.user import User
from typing import Optional
import re
import uuid
from datetime import datetime, timedelta

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.reset_tokens = {}

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
    
    def forgot_password(self, email: str):
        user = self.user_repository.find_by_email(email)
        if not user:
            return {"message": "Invalid email", "status": 400}
        
        token = str(uuid.uuid4())
        expiry_time = datetime.utcnow() + timedelta(hours=24)
        self.reset_tokens[token] = {"email": email, "expiry_time": expiry_time}
        # Here, an actual email should be sent containing the reset link with the token
        return {"message": "Password reset link has been sent to your email", "status": 200, "token": token}

    def reset_password(self, token: str, new_password: str):
        token_data = self.reset_tokens.get(token)

        if not token_data or token_data['expiry_time'] < datetime.utcnow():
            return {"message": "Token is invalid or expired", "status": 400}

        email = token_data['email']
        user = self.user_repository.find_by_email(email)
        if not user:
            return {"message": "Invalid token", "status": 400}

        if len(new_password) < 8 or not any(char.isdigit() for char in new_password) or not any(char.isupper() for char in new_password):
            return {
                "message": "Password must be at least 8 characters long, contain at least one number and one uppercase letter",
                "status": 400
            }

        user.password = new_password
        self.user_repository.save(user)
        del self.reset_tokens[token]
        return {"message": "Password has been reset successfully", "status": 200}