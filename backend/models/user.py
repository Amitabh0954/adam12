from hashlib import sha256

class User:
    def __init__(self, id: int, email: str, password: str, login_attempts: int = 0, is_locked: bool = False):
        self.id = id
        self.email = email
        self.password = User.hash_password(password)
        self.login_attempts = login_attempts
        self.is_locked = is_locked

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password using SHA256."""
        return sha256(password.encode('utf-8')).hexdigest()