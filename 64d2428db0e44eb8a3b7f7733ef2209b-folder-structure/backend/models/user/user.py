# Epic Title: User Account Management

from typing import Optional

class User:
    user_id: int
    email: str
    hashed_password: str
    
    def __init__(self, user_id: int, email: str, hashed_password: str):
        self.user_id = user_id
        self.email = email
        self.hashed_password = hashed_password
        
    def update_email(self, new_email: str):
        # logic to update email
        pass
    
    def set_password(self, new_password: str):
        # logic to set new password
        pass