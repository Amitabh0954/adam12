from datetime import datetime
import uuid

class User:
    def __init__(self, email: str, password: str):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password  # In a real-world scenario, ensure password hashing
        self.created_at = datetime.utcnow()