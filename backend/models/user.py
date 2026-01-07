class User:
    def __init__(self, id: int, email: str, password: str, login_attempts: int = 0, is_locked: bool = False):
        self.id = id
        self.email = email
        self.password = self._hash_password(password)
        self.login_attempts = login_attempts
        self.is_locked = is_locked

    def _hash_password(self, password: str) -> str:
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()