from datetime import datetime, timedelta

class Session:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.login_attempts = 0
        self.is_locked = False
        self.last_login_at = datetime.utcnow()
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def login(self):
        if self.is_locked:
            return False
        self.login_attempts = 0
        self.last_login_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        return True

    def failed_login(self):
        self.login_attempts += 1
        if self.login_attempts >= 5:
            self.is_locked = True
        self.updated_at = datetime.utcnow()

    def logout(self):
        self.updated_at = datetime.utcnow()

    def is_session_active(self):
        timeout_period = timedelta(minutes=30)
        return datetime.utcnow() - self.updated_at < timeout_period