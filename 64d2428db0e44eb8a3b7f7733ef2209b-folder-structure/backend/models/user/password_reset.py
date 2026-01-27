# Epic Title: User Account Management

from datetime import datetime, timedelta

class PasswordResetRequest:
    request_id: str
    user_id: int
    created_at: datetime
    expires_at: datetime
    is_used: bool

    def __init__(self, request_id: str, user_id: int):
        self.request_id = request_id
        self.user_id = user_id
        self.created_at = datetime.now()
        self.expires_at = self.created_at + timedelta(hours=24)
        self.is_used = False

    def mark_as_used(self):
        self.is_used = True

    def is_expired(self) -> bool:
        return datetime.now() > self.expires_at