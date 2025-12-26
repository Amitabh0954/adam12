from repositories.auth.user_repository import UserRepository
from repositories.auth.password_reset_token_repository import PasswordResetTokenRepository
from models.password_reset_token import PasswordResetToken

class PasswordResetService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.token_repository = PasswordResetTokenRepository()
        
    def request_password_reset(self, email: str):
        user = self.user_repository.find_by_email(email)
        if not user:
            return {"message": "Email not found", "status": 404}
        
        token = PasswordResetToken(user_id=user.id)
        self.token_repository.save(token)
        # Placeholder for sending email with token.token
        return {"message": "Password reset link sent", "status": 200}
    
    def confirm_password_reset(self, token: str, new_password: str):
        reset_token = self.token_repository.find_by_token(token)
        if not reset_token or reset_token.is_expired():
            return {"message": "Invalid or expired token", "status": 400}
        
        user = self.user_repository.find_by_id(reset_token.user_id)
        if not user:
            return {"message": "User not found", "status": 404}
        
        user.password = new_password
        self.user_repository.save(user)
        return {"message": "Password reset successfully", "status": 200}