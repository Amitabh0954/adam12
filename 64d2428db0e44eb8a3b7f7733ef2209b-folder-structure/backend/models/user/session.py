# Epic Title: User Account Management

from datetime import datetime, timedelta

class Session:
    session_id: str
    user_id: int
    created_at: datetime
    last_accessed_at: datetime
    
    def __init__(self, session_id: str, user_id: int):
        self.session_id = session_id
        self.user_id = user_id
        self.created_at = datetime.now()
        self.last_accessed_at = datetime.now()
    
    def update_last_accessed(self):
        self.last_accessed_at = datetime.now()

    def is_expired(self, timeout: int) -> bool:
        return datetime.now() - self.last_accessed_at > timedelta(minutes=timeout)