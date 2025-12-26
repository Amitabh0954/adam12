from datetime import datetime

class Profile:
    def __init__(self, user_id: str, name: str, email: str, preferences: dict):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.preferences = preferences
        self.updated_at = datetime.utcnow()