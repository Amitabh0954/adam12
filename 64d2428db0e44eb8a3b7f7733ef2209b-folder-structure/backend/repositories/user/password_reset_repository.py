# Epic Title: User Account Management

from backend.models.user.password_reset import PasswordResetRequest
from typing import Optional

class PasswordResetRepository:
    def __init__(self):
        # Initialize database connection here
        pass
    
    def add_password_reset_request(self, request: PasswordResetRequest) -> None:
        # logic to add password reset request to the database
        pass
    
    def get_password_reset_request_by_id(self, request_id: str) -> Optional[PasswordResetRequest]:
        # logic to retrieve a password reset request by id
        pass
    
    def mark_request_as_used(self, request_id: str) -> None:
        # logic to mark the request as used
        pass