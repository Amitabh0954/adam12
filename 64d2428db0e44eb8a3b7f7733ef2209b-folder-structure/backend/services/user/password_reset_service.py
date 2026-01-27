# Epic Title: User Account Management

from backend.models.user.password_reset import PasswordResetRequest
from backend.repositories.user.password_reset_repository import PasswordResetRepository
from backend.repositories.user.user_repository import UserRepository

class PasswordResetService:
    def __init__(self, password_reset_repository: PasswordResetRepository, user_repository: UserRepository):
        self.password_reset_repository = password_reset_repository
        self.user_repository = user_repository
    
    def create_password_reset_request(self, email: str) -> PasswordResetRequest:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise ValueError("User with given email does not exist")
        new_request = PasswordResetRequest(request_id="generated_request_id", user_id=user.user_id)  # Example ID management
        self.password_reset_repository.add_password_reset_request(new_request)
        # logic to send email with the reset link
        return new_request
    
    def validate_password_reset_request(self, request_id: str) -> bool:
        reset_request = self.password_reset_repository.get_password_reset_request_by_id(request_id)
        if reset_request and not reset_request.is_expired():
            return True
        return False

    def reset_password(self, request_id: str, new_password: str):
        reset_request = self.password_reset_repository.get_password_reset_request_by_id(request_id)
        if reset_request and not reset_request.is_expired() and not reset_request.is_used:
            user = self.user_repository.get_user_by_id(reset_request.user_id)
            user.set_password(new_password)
            reset_request.mark_as_used()
            self.password_reset_repository.mark_request_as_used(reset_request.request_id)
            # Update user password logic in repository
        else:
            raise ValueError("Invalid or expired password reset request")