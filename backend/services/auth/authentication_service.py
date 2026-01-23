from hashlib import sha256
from datetime import datetime, timedelta
from typing import Optional
from backend.models.users.user import User
from backend.models.users.session import Session
from backend.repositories.users.user_repository import UserRepository
from backend.repositories.users.session_repository import SessionRepository

class AuthenticationService:
    def __init__(self, user_repository: UserRepository, session_repository: SessionRepository):
        self.user_repository = user_repository
        self.session_repository = session_repository
        self.failed_attempts = {}

    def login_user(self, email: str, password: str) -> Optional[Session]:
        user = self.user_repository.get_user_by_email(email)
        if user is None or user.password_hash != sha256(password.encode()).hexdigest():
            self._track_failed_attempt(email)
            return None
        
        if self._is_account_locked(email):
            return None

        # Create a new session
        expires_at = datetime.utcnow() + timedelta(hours=1)
        session = Session(id=len(self.session_repository.sessions) + 1, user_id=user.id, expires_at=expires_at)
        return self.session_repository.create_session(session)

    def _track_failed_attempt(self, email: str) -> None:
        if email not in self.failed_attempts:
            self.failed_attempts[email] = 0
        self.failed_attempts[email] += 1

    def _is_account_locked(self, email: str) -> bool:
        return self.failed_attempts.get(email, 0) >= 5

    def hash_password(self, password: str) -> str:
        return sha256(password.encode()).hexdigest()

    def verify_password(self, password: str, hashed: str) -> bool:
        return hashed == sha256(password.encode()).hexdigest()