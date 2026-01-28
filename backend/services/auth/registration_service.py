import bcrypt
from backend.models import User
from backend.utils import validate_email, send_verification_email

class RegistrationService:
    def register_user(self, username: str, password: str, email: str) -> User:
        if not validate_email(email):
            raise ValueError('Invalid email address')
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        user = User(username=username, password_hash=hashed_password.decode('utf-8'), email=email)
        
        user.save()
        
        send_verification_email(user)
        
        return user
