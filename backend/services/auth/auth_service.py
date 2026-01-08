import os
import uuid
from datetime import datetime, timedelta

from dotenv import load_dotenv
from werkzeug.security import check_password_hash, generate_password_hash

from models.user import User
from repositories.auth.user_repository import UserRepository


load_dotenv()  # load .env directly here


class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()

        # env variables (loaded once for testing)
        self.max_login_attempts = int(os.getenv("MAX_LOGIN_ATTEMPTS", 5))
        self.session_timeout = int(os.getenv("SESSION_TIMEOUT", 3600))
        self.reset_token_expiry = int(os.getenv("RESET_TOKEN_EXPIRY", 900))

    def register_user(self, data: dict):
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return {"message": "Email and Password are required", "status": 400}

        if not self.is_password_secure(password):
            return {"message": "Password does not meet security criteria", "status": 400}

        if self.user_repository.find_by_email(email):
            return {"message": "Email already registered", "status": 400}

        user = User(
            email=email,
            password=generate_password_hash(password),
        )

        self.user_repository.save(user)

        return {
            "message": "User registered successfully. Please verify your email.",
            "status": 201,
        }

    def login_user(self, data: dict):
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return {"message": "Email and Password are required", "status": 400}

        user = self.user_repository.find_by_email(email)
        if not user:
            return {"message": "Invalid email or password", "status": 401}

        if user.is_locked:
            return {
                "message": "Account is locked due to too many invalid login attempts",
                "status": 403,
            }

        if not check_password_hash(user.password, password):
            user.login_attempts += 1

            if user.login_attempts >= self.max_login_attempts:
                user.is_locked = True

            self.user_repository.update(user)
            return {"message": "Invalid email or password", "status": 401}

        user.login_attempts = 0
        user.last_login_at = datetime.utcnow()
        self.user_repository.update(user)

        session_expiry = datetime.utcnow() + timedelta(
            seconds=self.session_timeout
        )

        return {
            "message": "Login successful",
            "session_expiry": session_expiry.isoformat(),
            "status": 200,
        }

    def request_password_reset(self, data: dict):
        email = data.get("email")

        if not email:
            return {"message": "Email is required", "status": 400}

        user = self.user_repository.find_by_email(email)
        if not user:
            return {"message": "Invalid email", "status": 400}

        user.reset_token = str(uuid.uuid4())
        user.reset_token_expiry = datetime.utcnow() + timedelta(
            seconds=self.reset_token_expiry
        )

        self.user_repository.update(user)

        return {
            "message": "Password reset link has been sent to your email",
            "status": 200,
        }

    def reset_password(self, data: dict, token: str):
        password = data.get("password")

        if not password:
            return {"message": "Password is required", "status": 400}

        if not self.is_password_secure(password):
            return {"message": "Password does not meet security criteria", "status": 400}

        user = self.user_repository.find_by_reset_token(token)

        if (
            not user
            or not user.reset_token_expiry
            or user.reset_token_expiry < datetime.utcnow()
        ):
            return {"message": "Invalid or expired reset token", "status": 400}

        user.password = generate_password_hash(password)
        user.reset_token = None
        user.reset_token_expiry = None

        self.user_repository.update(user)

        return {"message": "Password has been reset successfully", "status": 200}

    @staticmethod
    def is_password_secure(password: str) -> bool:
        return (
            len(password) >= 8
            and any(c.isdigit() for c in password)
            and any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c in "!@#$%^&*()_+-=[]{}|;:'\",.<>?/" for c in password)
        )
