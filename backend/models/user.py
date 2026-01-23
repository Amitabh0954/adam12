from datetime import datetime
from werkzeug.security import generate_password_hash
import re

class PasswordStrengthError(Exception):
    pass

class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = self.set_password(password)
        self.login_attempts = 0
        self.is_locked = False
        self.last_login_at = None
        self.reset_token = None
        self.reset_token_expiry = None
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.cart_state = None
        self.is_email_authenticated = False
        self.email_auth_token = None
        self.email_auth_token_expiry = None

    def set_password(self, password: str):
        if not self.is_password_strong(password):
            raise PasswordStrengthError(
                "Password must be at least 8 characters long, include an uppercase letter, a lowercase letter, a number, and a special character."
            )
        return generate_password_hash(password)

    @staticmethod
    def is_password_strong(password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[\W_]+", password):
            return False
        return True
