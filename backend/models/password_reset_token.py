from datetime import datetime, timedelta
import uuid

class PasswordResetToken:
    def __init__(self, user_id: int):
        self.token = str(uuid.uuid4())
        self.user_id = user_id
        self.created_at = datetime.utcnow()
        self.expires_at = self.created_at + timedelta(hours=24)

    def is_expired(self) -> bool:
        return datetime.utcnow() > self.expires_at