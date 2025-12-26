from repositories.auth.password_reset_repository import PasswordResetRepository
from repositories.auth.user_repository import UserRepository
from models.password_reset import PasswordResetToken
import hashlib

class PasswordResetService:
    def __init__(self):
        self.password_reset_repository = PasswordResetRepository()
        self.user_repository = UserRepository()

    def request_password_reset(self, data: dict):
        email = data.get('email')

        if not email:
            return {"message": "Email is required", "status": 400}

        user = self.user_repository.find_by_email(email)
        if not user:
            return {"message": "Email not found", "status": 404}

        if self.password_reset_repository.find_by_token(user.id):
            return {"message": "A password reset request is already pending", "status": 400}

        reset_token = PasswordResetToken(user_id=user.id)
        self.password_reset_repository.save(reset_token)

        # Send email with reset_token.token

        return {"message": "Password reset email sent", "status": 200}

    def verify_password_reset(self, data: dict):
        token = data.get('token')
        new_password = data.get('new_password')

        if not token or not new_password:
            return {"message": "Invalid request", "status": 400}

        reset_token = self.password_reset_repository.find_by_token(token)
        if not reset_token or not reset_token.is_valid():
            return {"message": "Invalid or expired token", "status": 400}

        user = self.user_repository.find_by_id(reset_token.user_id)
        encoded_password = hashlib.sha256(new_password.encode()).hexdigest()
        user.password = encoded_password

        self.user_repository.save(user)
        self.password_reset_repository.invalidate_token(token)

        return {"message": "Password reset successfully", "status": 200}