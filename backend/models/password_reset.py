from datetime import datetime, timedelta
import uuid

class PasswordResetToken:
    def __init__(self, user_id: str):
        self.token = str(uuid.uuid4())
        self.user_id = user_id
        self.created_at = datetime.utcnow()
        self.expires_at = self.created_at + timedelta(hours=24)
        self.active = True

    def is_valid(self):
        return self.active and datetime.utcnow() < self.expires_at

    def invalidate(self):
        self.active = False