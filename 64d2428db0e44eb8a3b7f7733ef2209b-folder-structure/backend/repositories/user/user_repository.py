# Epic Title: User Account Management

from backend.models.user.user import User

class UserRepository:
    def __init__(self):
        # Initialize database connection here
        pass
    
    def add_user(self, user: User) -> None:
        # logic to add user to the database
        pass
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        # logic to retrieve a user by email
        pass